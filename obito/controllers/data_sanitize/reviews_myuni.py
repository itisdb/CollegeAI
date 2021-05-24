from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
DTU
Indraprastha University
NIT Delhi
KJ Somaiya college of engineering
Thadomal Sahani Engineering college
Jaipur National University
Thakur college of Engg & Technology
Veermata Jijabhai Technological Institute
Institute of Chemical Technology
NIT Patna
NIT Allahabad
IIIT Hyderabad
IIIT Allahabad
Swami Keshavnand
UPES Dehradun
ITER Bhubaneswar
Dwarkadas Jivanlal Sanghvi college of Engg
'''

def get_reviews(url=None,existing=True,path_to_existing_df=None,path_to_new_df=None,path_for_csv=None):
    # Get offset
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    driver.get(url)
    try:
        wait = WebDriverWait(driver,10)
        last = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.pagination_btn_other.pagination_btn_last > a.btn.pagination_btn_all")))
        driver.execute_script("arguments[0].scrollIntoView();", last)
        driver.execute_script("arguments[0].click();", last)
        offset = int(driver.current_url[-1])
    except:
        buttons = driver.find_elements_by_class_name("pagination_btn_all")
        offset = int(buttons[-2].text)
    # print(offset)

    # Scrape all reviews
    reviews_complete = []
    for page_no in range(1,offset+1):
        url_per_page = f'{url}?page={page_no}'
        url_content = requests.get(url, headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}).text
        soup = bs(url_content,'html.parser')
        main_divs = soup.find_all('div',class_ = 'review-card')
        all_reviews = []
        for div in main_divs:
            div_child = div.find_all('div',class_ = 'category-wrapper')
            full_review = []
            for review_div in div_child:
                review_text_div = review_div.find('div',class_ = 'review-text-wrapper')
                full_review.append(review_text_div.text)
            all_reviews.append("".join(full_review))
        reviews_complete.extend(all_reviews)

    if existing:
        existing_reviews = pd.read_csv(path_to_existing_df)
        new_df = pd.DataFrame({'review':reviews_complete})
        reviews_concat = pd.concat([existing_reviews, new_df],axis=0,ignore_index=True)
        reviews_concat.to_csv(path_to_new_df,index=False)
    else:
        reviews_df = pd.DataFrame({'review':reviews_complete})
        reviews_df.to_csv(path_for_csv)

# Scraping script
get_reviews(url="https://www.getmyuni.com/college/indraprastha-institute-of-information-technology-iiit-new-delhi/reviews",existing=False,path_for_csv="data/_indraprastha_reviews.csv")
get_reviews(url="https://www.getmyuni.com/college/national-institute-of-technology-nit-new-delhi/reviews",existing=False,path_for_csv="data/_nit_delhi_reviews_new.csv")
get_reviews(url="https://www.getmyuni.com/college/kj-somaiya-institute-of-engineering-and-information-technology-kjsieit-mumbai/reviews",existing=False,path_for_csv="data/_kjsieit_reviews_new.csv")
get_reviews(url="https://www.getmyuni.com/college/thadomal-shahani-engineering-college-tsec-mumbai/reviews",existing=False,path_for_csv="data/_tsec_reviews_new.csv")
get_reviews(url="https://www.getmyuni.com/college/jaipur-national-university-jnu-jaipur/reviews",existing=False,path_for_csv="data/_jnu_reviews_new.csv")
get_reviews(url="https://www.getmyuni.com/college/thakur-college-of-engineering-and-technology-tcet-mumbai/reviews",existing=False,path_for_csv="data/_thakur_reviews_new.csv")
