from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import requests,time

'''
IIT Delhi
IIT Kharagpur
NIT Trichy
VIT Vellore
BITS Pilani
'''

# Creating the function to scrap reviews
def get_reviews(url=None, path_to_csv=None):
    # Initialization
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    driver.get(url)
    wait = WebDriverWait(driver,5)

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
    print(len(reviews_list))
    review = pd.DataFrame(reviews_list)
    review.to_csv(path_to_csv)

get_reviews(url = "https://www.shiksha.com/university/iit-delhi-indian-institute-of-technology-53938/reviews-3", path_to_csv="data/shiksha1.csv")
get_reviews(url='https://www.shiksha.com/college/iit-kharagpur-indian-institute-of-technology-2999/reviews',path_to_csv='data/shiksha2.csv')
#get_reviews(url='https://www.shiksha.com/university/nit-trichy-national-institute-of-technology-tiruchirappalli-2996/reviews', path_to_csv='data/_nit_trichy.csv')
#get_reviews(url='https://www.shiksha.com/university/vellore-institute-of-technology-vellore-29714/reviews', path_to_csv='data/_vit_reviews.csv')
#get_reviews(url='https://www.shiksha.com/university/bits-pilani-birla-institute-of-technology-and-science-467/reviews', path_to_csv='data/_bits_reviews.csv')


# Debugging
'''loadmore = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button.button--secondary")))
driver.execute_script("arguments[0].scrollIntoView();", loadmore)
driver.execute_script("arguments[0].click();", loadmore)
login_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.switchOptions > a.link")))
driver.execute_script("arguments[0].click();", login_link)
# google_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "fY3Crt_globalRegistrationWrapper > div > div > div.reg-form-box > div.socialLoginBox > div.socialBtns > div:nth-child(1) > div > button")))
# driver.execute_script("arguments[0].click();", google_login)
login_option = driver.find_elements_by_class_name('loginButton')
print(login_option)'''

