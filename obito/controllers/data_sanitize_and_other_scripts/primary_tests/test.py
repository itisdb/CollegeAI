from bs4 import BeautifulSoup as bs
import requests,re

'''url="https://collegedunia.com/review/get-college-reviews"
get_offset_url="https://collegedunia.com/university/56865-vit-university-vit-chennai/reviews"

offset_request = requests.get(get_offset_url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}).text
soup = bs(offset_request, 'html.parser')
offset = soup.select('li a')[-2].text

print(offset)'''

review_url = 'https://www.careers360.com/colleges/arya-college-of-engineering-and-research-centre-jaipur/reviews'
url_request = requests.get(review_url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}).text
# Get reviews
soup = bs(url_request, 'html.parser')
cards = list(soup.find_all('div', class_ = "cardBlk repeatBlk"))
reviews_per_user = []
sub_card = cards[1]
child1 = sub_card.find('div', class_ = 'cardBlkInn')
child2 = child1.find('div', class_ = 'ratingOuter')
revs = child2.find('div')
'''regex_pattern = r"<div.*?>((?:[^\\])*)<ul.*?>"
revs_filtered = str(child2[0])
# reviews_per_user.append(revs_filtered)
reviews_stripped = re.sub('\n+\t+','',re.findall(regex_pattern,revs_filtered)[0])
reviews_stripped_tab = re.sub('\t','',reviews_stripped)
reviews_modified = re.sub('&amp;','&',reviews_stripped_tab)'''
print(revs)

