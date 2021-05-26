from bs4 import BeautifulSoup as bs
from bs4 import NavigableString,Comment
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
DTU
IIT Madras
IIT Kanpur
IIT Roorkie
IIT Guwahati
'''

def get_reviews(url=None,path_to_csv= None):
    url_request = requests.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}).text
    soup = bs(url_request,'html.parser')
    review_divs = soup.find_all('div', class_='row indi-review')
    reviews_all = []
    for review_block in review_divs:
        review_raw = []
        review_desc = review_block.descendants
        for d in review_desc:
            if d.name == 'div' and d.get('class',[''])[0] == 'media-body':
                for child in d.children:
                    if isinstance(child,NavigableString) and not isinstance(child,Comment):
                        review_raw.append(child.strip())
        reviews_all.append(' '.join(list(filter(lambda x: x != '', review_raw))))

    # Create the dataset
    review_df = pd.DataFrame({'reviews':reviews_all})
    review_df.to_csv(path_to_csv,index=False)

# Scraping Reviews
get_reviews(url = 'https://www.collegesearch.in/university/delhi-technological-university-dtu-delhi/reviews',path_to_csv='data/collegesearch1.csv')
get_reviews(url='https://www.collegesearch.in/colleges/indian-institute-of-technology-iit-madras-chennai/reviews', path_to_csv='data/collegesearch2.csv')
#get_reviews(url='https://www.collegesearch.in/colleges/indian-institute-of-technology-iit-kanpur/reviews', path_to_csv='data/_iit_kanpur.csv')
#get_reviews(url='https://www.collegesearch.in/colleges/indian-institute-of-technology-iit-roorkee/reviews', path_to_csv='data/_iit_roorkie.csv')
#get_reviews(url='https://www.collegesearch.in/colleges/indian-institute-of-technology-iit-guwahati/reviews',path_to_csv='data/_iit_guwahati.csv')
