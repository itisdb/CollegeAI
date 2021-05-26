from bs4 import BeautifulSoup as bs
import requests,re
import pandas as pd

'''
DIT University
Parul University
Sharda University
Arya College of Engineering
'''

def get_reviews(url = None , path_to_csv = None):
    url_request = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}).text
    # Get reviews
    soup = bs(url_request, 'html.parser')
    # Get offset
    offset_div = soup.find('div', class_ = "paginationBlk text-center")
    try:
        offset = offset_div.find_all('li')[-2].text
    except:
        offset = 'NA'
    # Start extracting reviews
    cards = list(soup.find_all('div', class_ = "cardBlk repeatBlk"))
    reviews_per_user = []
    if offset == 'NA':
        for sub_card in cards:
            child1 = sub_card.find('div', class_ = 'cardBlkInn')
            child2 = child1.find('div', class_ = 'ratingOuter')
            revs = child2.find_all('div')
            regex_pattern = r'<div>(.*?)</div>'
            revs_filtered = " ".join(list(map(lambda text : re.findall(regex_pattern,text)[0], list(filter(re.compile(regex_pattern).search, list(map(lambda y : str(y), revs)))))))
            reviews_per_user.append(revs_filtered)
    else:
        for offset_no in range(1,int(offset)+1):
            for sub_card in cards:
                child1 = sub_card.find('div', class_ = 'cardBlkInn')
                child2 = child1.find('div', class_ = 'ratingOuter')
                revs = child2.find_all('div')
                regex_pattern = r'<div>(.*?)</div>'
                revs_filtered = " ".join(list(map(lambda text : re.findall(regex_pattern,text)[0], list(filter(re.compile(regex_pattern).search, list(map(lambda y : str(y), revs)))))))
                reviews_per_user.append(revs_filtered)
    review_df = pd.DataFrame({'review' : reviews_per_user})
    review_df.to_csv(path_to_csv,index=False)

get_reviews(url = "https://www.careers360.com/university/dit-university-dehradun/reviews", path_to_csv = 'data/career360_1.csv')
get_reviews(url = 'https://www.careers360.com/university/parul-university-vadodara/reviews', path_to_csv = 'data/career360_2.csv')
#get_reviews(url = 'https://www.careers360.com/university/sharda-university-greater-noida/reviews', path_to_csv = 'data/_sharda.csv')
#get_reviews(url = 'https://www.careers360.com/colleges/arya-college-of-engineering-and-research-centre-jaipur/reviews', path_to_csv = 'data/_arya_college.csv')








