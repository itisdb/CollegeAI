from data_sanitize import data_sanitize,reviews_myuni
import re

# Try 1 : "https://collegedunia.com/college/13834-institute-of-engineering-and-management-iem-kolkata/reviews"
class UrlJsonResponse:
    def __init__(self,url_input = "https://www.getmyuni.com/college/delhi-technological-university-dtu-new-delhi/reviews"):
        self.url_input = url_input
    
    # Main extractor function
    def extract_json_reviews(self):
        url_scrape = self.url_input
        regex_pattern_www,regex_pattern = 'https?://www.([A-Za-z_0-9.-]+).com','https?://([A-Za-z_0-9.-]+).com'
        try :
            extract_domain = re.search(regex_pattern_www,url_scrape).group(1)
        except:
            extract_domain = re.search(regex_pattern,url_scrape).group(1)
        # Call correct script
        if extract_domain == 'collegedunia':
            extract_college_id = re.search(r'https://collegedunia.com/college/(\d+)',url_scrape).group(1)
            json_response = data_sanitize.create_datasets(get_offset_url = url_scrape,college_id=extract_college_id)
        else:
            json_response = reviews_myuni.get_reviews(url=url_scrape)
        return json_response


# Driver function
if __name__ == '__main__':
    json_response_obj = UrlJsonResponse()
    print(json_response_obj.extract_json_reviews())


