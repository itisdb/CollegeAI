from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests,time

url = "https://www.shiksha.com/university/iit-delhi-indian-institute-of-technology-53938/reviews-3"

# Initialization
'''options = webdriver.ChromeOptions()
options.add_argument("headless")'''
driver = webdriver.Chrome("C:\\chromedriver.exe") #, options = options
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

