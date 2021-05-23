from data_sanitize_and_other_scripts import data_sanitize,reviews_myuni
# Import constants
from obito import constants
import re

# Try 1 : "https://collegedunia.com/college/13834-institute-of-engineering-and-management-iem-kolkata/reviews"
class UrlJsonResponse:
    def __init__(self,url_input = constants.STATIC_URL_DEFAULT):
        self.url_input = url_input
    
    # Main extractor function
    def extract_json_reviews(self):
        url_scrape = self.url_input
        regex_pattern_www,regex_pattern = constants.REGEX_WITH_WWW,constants.REGEX_WITHOUT_WWW
        try :
            extract_domain = re.search(regex_pattern_www,url_scrape).group(1)
        except:
            extract_domain = re.search(regex_pattern,url_scrape).group(1)
        # Call correct script
        if extract_domain == constants.COLLEGEDUNIA_MATCH:
            extract_college_id = re.search(constants.COLLEGEDUNIA_CONSTANT_DOMAIN_REGEX,url_scrape).group(1)
            json_response = data_sanitize.create_datasets(get_offset_url = url_scrape,college_id=extract_college_id)
        else:
            json_response = reviews_myuni.get_reviews(url=url_scrape)
        return json_response


# Driver function
if __name__ == '__main__':
    json_response_obj = UrlJsonResponse()
    print(json_response_obj.extract_json_reviews())


