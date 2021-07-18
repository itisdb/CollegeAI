from typing import Any

from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd
from bs4 import NavigableString, Comment
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from college.models import College
from reviews.models import Review

all_reviews = Review.objects.all()

# Generic Scraper Class

class Scraper:

    def __init__(self, url = None):
        self.url = url
        self.colleges = College.objects.all()

    def invoke(self, college):
        urls = college.scraping_urls
        if urls is not None:
            for url in urls:
                self.identify_and_trigger(url, college)

    def store_review(self, college: College, review: Any, source: int):
        existing_review = Review.objects.filter(
            college=college,
            source=source,
            comment=review.contents[0] if not isinstance(review, str) else review
        )
        if not existing_review.exists():
            new_review = Review.objects.create(
                college=college,
                comment=review.contents[0] if not isinstance(review, str) else review,
                source=source
            )
            print(f'Storing new Review from [{new_review.get_source_display()}]')

    # getmyuni Scraper
    def getmyuni(self, url: str, college: College):
        driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        try:
            driver.get(url)
            try:
                wait = WebDriverWait(driver, 10)
                last = wait.until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "li.pagination_btn_other.pagination_btn_last > a.btn.pagination_btn_all")))
                driver.execute_script("arguments[0].scrollIntoView();", last)
                driver.execute_script("arguments[0].click();", last)
                offset = int(driver.current_url[-1])
            except:
                buttons = driver.find_elements_by_class_name("pagination_btn_all")
                offset = int(buttons[-2].text)
            # print(offset)

            # Scrape all reviews
            reviews_complete = []
            for page_no in range(1, offset + 1):
                url_per_page = f'{url}?page={page_no}'
                url_content = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}).text
                soup = bs(url_content, 'html.parser')
                main_divs = soup.find_all('div', class_='review-card')
                all_reviews = []
                for div in main_divs:
                    div_child = div.find_all('div', class_='category-wrapper')
                    full_review = []
                    for review_div in div_child:
                        review_text_div = review_div.find('div', class_='review-text-wrapper')
                        full_review.append(review_text_div.text)
                    all_reviews.append("".join(full_review))
                reviews_complete.extend(all_reviews)

                for review in reviews_complete:
                    filter = all_reviews.filter(comment = review.contents[0] if not isinstance(review, str) else review).exists()
                    if not filter:
                        self.store_review(college, review, Review.ReviewSources.GET_MY_UNI.value)
        except:
            pass

# College Search Scraper
    def collegesearch(self,url: str, college: College):
        try:
            url_request = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}).text
            soup = bs(url_request, 'html.parser')
            review_divs = soup.find_all('div', class_='row indi-review')
            reviews_all = []
            for review_block in review_divs:
                review_raw = []
                review_desc = review_block.descendants
                for d in review_desc:
                    if d.name == 'div' and d.get('class', [''])[0] == 'media-body':
                        for child in d.children:
                            if isinstance(child, NavigableString) and not isinstance(child, Comment):
                                review_raw.append(child.strip())
                reviews_all.append(' '.join(list(filter(lambda x: x != '', review_raw))))

            # Create the dataset
            for review in reviews_all:
                filter = all_reviews.filter(comment = review.contents[0] if not isinstance(review,str) else review).exists()
                if (not filter):
                    self.store_review(college, review, Review.ReviewSources.COLLEGE_SEARCH.value)
        except:
            pass

    # Shiksha Scraper
    def shiksha(self,url: str, college: College):
        # Initialization
        driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        try:
            driver.get(url)
            wait = WebDriverWait(driver, 5)

            # Scraping
            loader_classname = 'inf-pgntn'
            while True:
                try:
                    loadmore = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button.button--secondary")))
                    driver.execute_script("arguments[0].scrollIntoView();", loadmore)
                    driver.execute_script("arguments[0].click();", loadmore)
                    wait.until(EC.staleness_of(loadmore))
                except Exception:
                    break

            reviews_list = []
            reviews_element = driver.find_elements_by_class_name('desc-sp')
            for review in reviews_element:
                reviews_list.append(review.text)
            for review in reviews_list:
                filter = all_reviews.filter(comment = review.contents[0] if not isinstance(review,str) else review).exists()
                if (not filter):
                    self.store_review(college, review, Review.ReviewSources.SHIKSHA.value)
        except:
            pass

# Career360 Scraper
    def career360(self,url: str, college: College):
        url_request = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}).text
        # Get reviews
        soup = bs(url_request, 'html.parser')
        # Get offset
        offset_div = soup.find('div', class_="paginationBlk text-center")
        try:
            offset = offset_div.find_all('li')[-2].text
        except:
            offset = 'NA'
        # Start extracting reviews
        cards = list(soup.find_all('div', class_="cardBlk repeatBlk"))
        reviews_per_user = []
        if offset == 'NA':
            for sub_card in cards:
                child1 = sub_card.find('div', class_='cardBlkInn')
                child2 = child1.find('div', class_='ratingOuter')
                revs = child2.find_all('div')
                regex_pattern = r'<div>(.*?)</div>'
                revs_filtered = " ".join(list(map(lambda text: re.findall(regex_pattern, text)[0], list(
                    filter(re.compile(regex_pattern).search, list(map(lambda y: str(y), revs)))))))
                reviews_per_user.append(revs_filtered)
        else:
            try:
                for offset_no in range(1, int(offset) + 1):
                    for sub_card in cards:
                        child1 = sub_card.find('div', class_='cardBlkInn')
                        child2 = child1.find('div', class_='ratingOuter')
                        revs = child2.find_all('div')
                        regex_pattern = r'<div>(.*?)</div>'
                        revs_filtered = " ".join(list(map(lambda text: re.findall(regex_pattern, text)[0], list(
                            filter(re.compile(regex_pattern).search, list(map(lambda y: str(y), revs)))))))
                        reviews_per_user.append(revs_filtered)
            except:
                pass
        for review in reviews_per_user:
            filter = all_reviews.filter(comment = review.contents[0] if not isinstance(review,str) else review).exists()
            if (not filter):
                self.store_review(college, review, Review.ReviewSources.CAREER360.value)

# Google Reviews Scraper
    def google(self,url: str,college: College):
        pass

# collegedunia Reviews Scraper
    def collegedunia(self,url: str, college: College):
        # Automating the fetching of offset(no. of review pages)
        try:
            offset_request = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}).text
            soup = bs(offset_request, 'html.parser')

            college_name_raw = soup.select('h1', class_="college_name")[0].text
            college_name = college_name_raw.replace(' - Reviews', '')

            reviews = soup.find_all('p', class_='jsx-2209713675 m-0 review-content d-inline')

            for review in reviews:
                filter = all_reviews.filter(comment = (review.contents[0] if not isinstance(review,str) else review)).exists()
                if (not filter):
                    self.store_review(college, review, Review.ReviewSources.COLLEGE_DUNIA.value)
        except:
            pass

    # Identifying the website
    def identify_and_trigger(self,url: str , college: College):

        if url.find("collegesearch") != -1:
            self.collegesearch(url, college)
        elif url.find("getmyuni") != -1:
            self.getmyuni(url, college)
        elif url.find("shiksha") != -1:
            self.shiksha(url, college)
        elif url.find("careers360") != -1:
            self.career360(url, college)
        elif url.find("google") != -1:
            self.google(url, college)
        elif url.find("collegedunia") != -1:
            self.collegedunia(url, college)
        else:
            print(f"{url} : Not a Recognized website")




#x.identify_and_trigger(url = "https://www.careers360.com/university/dit-university-dehradun/reviews", path_to_csv = 'data/_dit_reviews.csv')
#x.identify_and_trigger(url = 'https://www.collegesearch.in/university/delhi-technological-university-dtu-delhi/reviews',path_to_csv='data/_dtu_new.csv')
#x.identify_and_trigger(url = "https://www.shiksha.com/university/iit-delhi-indian-institute-of-technology-53938/reviews-3", path_to_csv="data/_iit_delhi.csv")
#x.identify_and_trigger(url="https://www.getmyuni.com/college/indraprastha-institute-of-information-technology-iiit-new-delhi/reviews", path_to_csv="data/_indraprastha_reviews.csv")
#x.identify_and_trigger(url = "https://collegedunia.com/university/25602-indian-institute-of-management-iimb-bangalore/reviews", path_to_csv= "data/_iim_b.csv")
#x.identify_and_trigger(url="https://collegedunia.com/university/25494-indian-institute-of-management-iima-ahmedabad/reviews", path_to_csv = "data/iim_a.csv")
