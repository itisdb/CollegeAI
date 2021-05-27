from bs4 import BeautifulSoup as bs
import requests,csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome("/usr/local/bin/chromedriver")
test_url = "https://www.google.com/maps/place/Indian+Institute+of+Technology+Delhi/@28.54523,77.1903753,17z/data=!4m7!3m6!1s0x0:0x81c10b266b1ea3c0!8m2!3d28.5449756!4d77.1926284!9m1!1b1"
driver.get(test_url)

scroll_pause_time = 10
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1

while True:
    # scroll one screen height each time
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break

review_text = driver.find_elements_by_class_name("section-review-review-content")
print([a.text for a in review_text])

'''
with open(r'data/google.csv', 'a', newline='\n', encoding='utf-8') as f:
    writer = csv.writer(f)
    for a in review_text:
        writer.writerow([a.text])

# Initializing empty CSV
df = pd.DataFrame()
df.to_csv("iit_delhi_reviews.csv")

# Initialization
#options = webdriver.ChromeOptions()
#options.add_argument("headless")
driver = webdriver.Chrome("C:\\chromedriver.exe")
# The URL
test_url = "https://www.google.com/maps/place/Indian+Institute+of+Technology+Delhi/@28.54523,77.1903753,17z/data=!4m7!3m6!1s0x0:0x81c10b266b1ea3c0!8m2!3d28.5449756!4d77.1926284!9m1!1b1"
# test_request = requests.get(test_url).text
driver.get(test_url)

i,MAX_LENGTH = 0,20000

# Scraping
while i < MAX_LENGTH:
    try:
        scrollable_div = driver.find_elements_by_class_name('scrollable-show')
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div[0])
        i += 1
    except:
        scrollable_div = driver.find_elements_by_css_selector('div.scrollable-show')
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div[0])
        i += 1

review_text = driver.find_elements_by_class_name("section-review-review-content")
print([a.text for a in review_text])
with open(r'iit_delhi_reviews.csv', 'a', newline='\n', encoding='utf-8') as f:
    writer = csv.writer(f)
    for a in review_text:
        writer.writerow([a.text])
'''
