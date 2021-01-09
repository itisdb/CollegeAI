import requests
import re
import pandas as pd
from bs4 import BeautifulSoup as bs

# final_ratings_stream = pd.DataFrame()

def create_datasets(url="https://collegedunia.com/review/get-college-reviews",get_offset_url="https://collegedunia.com/university/25948-indian-institute-of-technology-iit-kanpur/reviews",college_id="25948", path_to_reviews_csv = 'data_files\iitk_reviews.csv',path_to_other_csv = 'data_files\iitk_others.csv'):
    # Automating the fetching of offset(no. of review pages)
    offset_request = requests.get(get_offset_url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}).text
    soup = bs(offset_request, 'html.parser')
    offset = soup.select('li a')[-2].text
    college_name_raw = soup.select('h1', class_="college_name")[0].text
    college_name = college_name_raw.replace(' - Reviews','')
    '''
    Extracting data for various colleges
    25948 : IIT Kanpur
    25992 : IIT Roorkee
    26007 : IIT Kharagpur
    25396 : IIT Guwahati
    25703 : IIT Mumbai
    25455 : IIT Delhi
    25947 : IIT BHU, Varanasi
    25449 : DTU
    13834 : IEM
    13708 : Heritage Institute of Technology
    15439 : Techno India University
    13695 : Haldia Institute of Technology
    45696 : JIS College of Engineering
    28330 : IIEST Shibpur
    25851 : UEM Jaipur
    57446 : UEM Kolkata
    25800 : BITS Pilani
    13088 : BIT Mesra
    26008 : Jadavpur University
    25760 : KIIT
    26009 : NIT Durgapur
    24260 : NIT Rourkela
    25584 : NIT Jamshedpur
    25442 : NIT Raipur
    25916 : NIT Agartala
    25399 : NIT Silchar
    25464 : NIT Delhi
    56865 : VIT
    56189 : SRM
    13966 : KGEC Nadia
    54797 : Amity Noida
    25837 : Poornima University
    14719 : RIET
    25871 : BIHER
    25863 : Anna University
    25777 : Chandigarh University
    25819 : Jaipur National University
    25972 : Sharda University
    25787 : LPU
    25598 : Christ University
    25828 : MNIT
    13917 : KJ Somaiya KJSIEIT
    15452 : Thadomal TSEC
    54796 : Thakur college
    '''
    reviews, ratings, stream = [], [], []
    # Main loop
    for offset_val in range(1,int(offset)-1):
        for sort_val in range(1,5):
            querystring = {"college_id":college_id,"sort":str(sort_val),"offset":str(offset_val),"tab":"home"}
            payload = ""
            response = requests.request("GET", url, data=payload, params=querystring)
            # Extracting the string to search from
            revs_raw = response.json()['snippet']
            revs_raw.replace('','Grabage value')
            # REGEX for extracting reviews
            regex_pattern_rev = r'<p.*?>(.*?)<\/p>'
            # REGEX for extracting student ratings and their stream of study
            regex_pattern_rating = r'<span class="rating " id="review_rating">(.*?)<\/span>'
            regex_pattern_course = r'<span class="author_stream">(.*?)<\/span>'
            # Segregating out the reviews, ratings and the stream of study.
            reviews_all = re.findall(regex_pattern_rev, revs_raw)
            ratings_all = re.findall(regex_pattern_rating, revs_raw)
            stream_variety = re.findall(regex_pattern_course, revs_raw)
            # Append them to separate lists
            reviews.extend(reviews_all)
            ratings.extend(ratings_all)
            stream.extend(stream_variety)
    # Creating dataframe for reviews
    review_df = pd.DataFrame({'review':reviews})
    review_df.to_csv(path_to_reviews_csv,index=False)
    # Creating dataframe for other information
    other_data_df = pd.DataFrame({'college_name':college_name,'rating':ratings,'stream':stream})
    other_data_df.to_csv(path_to_other_csv,index=False)

    return other_data_df

# Test run for IIT-Kanpur
# print("REVIEWS :\n",reviews,"\nRATINGS :\n",ratings,"\nSTREAM OF STUDY :\n",stream)
# OPTIONAL : print("REVIEWS SHAPE :\n",len(reviews),"\nRATINGS SHAPE :\n",len(ratings),"\nSTREAM OF STUDY SHAPE :\n",len(stream))'''


# Create CSV files for different colleges.
'''
# 1. IIT Kanpur
others_iitk = create_datasets(get_offset_url="https://collegedunia.com/university/25948-indian-institute-of-technology-iit-kanpur/reviews",college_id="25948")

# 2. IIT Roorkee
others_iitr = create_datasets(get_offset_url="https://collegedunia.com/university/25992-indian-institute-of-technology-iit-roorkee/reviews",college_id="25992", path_to_reviews_csv = 'data_files\iitr_reviews.csv',path_to_other_csv = 'data_files\iitr_others.csv')

# 3. IIT KGP
others_iit_kgp = create_datasets(get_offset_url="https://collegedunia.com/university/26007-indian-institute-of-technology-iit-kharagpur/reviews",college_id="26007", path_to_reviews_csv = 'data_files\iit_kgp_reviews.csv',path_to_other_csv = 'data_files\iit_kgp_others.csv')

# 4. IEM
others_iem = create_datasets(get_offset_url="https://collegedunia.com/college/13834-institute-of-engineering-and-management-iem-kolkata/reviews",college_id="13834", path_to_reviews_csv = 'data_files\iem_reviews.csv',path_to_other_csv = 'data_files\iem_others.csv')

# 5. BITS Pilani
others_bitsp = create_datasets(get_offset_url="https://collegedunia.com/university/25800-birla-institute-of-technology-and-science-bits-pilani/reviews",college_id="25800", path_to_reviews_csv = 'data_files\pilani_bits_reviews.csv',path_to_other_csv = 'data_files\pilani_bits_others.csv')

# 6. BIT Mesra
others_bitm = create_datasets(get_offset_url="https://collegedunia.com/university/13088-birla-institute-of-technology-bit-mesra-ranchi/reviews",college_id="13088", path_to_reviews_csv = 'data_files\mesra_bit_reviews.csv',path_to_other_csv = 'data_files\mesra_bit_others.csv')

# 7. Jadavpur University
others_ju = create_datasets(get_offset_url="https://collegedunia.com/university/26008-jadavpur-university-ju-kolkata/reviews",college_id="26008", path_to_reviews_csv = 'data_files\ju_reviews.csv',path_to_other_csv = 'data_files\ju_others.csv')

# 8. KIIT
others_kiit = create_datasets(get_offset_url="https://collegedunia.com/university/25760-kalinga-institute-of-industrial-technology-kiit-bhubaneswar/reviews",college_id="25760", path_to_reviews_csv = 'data_files\kiit_reviews.csv',path_to_other_csv = 'data_files\kiit_others.csv')

# 9. IIT Guwahati
others_iitg = create_datasets(get_offset_url="https://collegedunia.com/university/25396-indian-institute-of-technology-iit-guwahati/reviews",college_id="25396", path_to_reviews_csv = 'data_files\iit_guwahati_reviews.csv',path_to_other_csv = 'data_files\iit_guwahati_others.csv')

# 10. IIT Mumbai
others_iit_mumbai = create_datasets(get_offset_url="https://collegedunia.com/university/25703-iit-bombay-indian-institute-of-technology-mumbai/reviews",college_id="25703", path_to_reviews_csv = 'data_files\iit_mumbai_reviews.csv',path_to_other_csv = 'data_files\iit_mumbai_others.csv')

# 11. IIT BHU Varanasi
others_iit_bhu = create_datasets(get_offset_url="https://collegedunia.com/university/25947-indian-institute-of-technology-iit-bhu-varanasi/reviews",college_id="25947", path_to_reviews_csv = 'data_files\iit_bhu_reviews.csv',path_to_other_csv = 'data_files\iit_bhu_others.csv')

# 12. NIT Durgapur
others_nit_dgp = create_datasets(get_offset_url="https://collegedunia.com/university/26009-national-institute-of-technology-nit-durgapur/reviews",college_id="26009", path_to_reviews_csv = 'data_files\dgp_nit_reviews.csv',path_to_other_csv = 'data_files\dgp_nit_others.csv')

# 13. NIT Rourkela
others_nit_rourkela = create_datasets(get_offset_url="https://collegedunia.com/university/24260-national-institute-of-technology-nit-rourkela/reviews",college_id="24260", path_to_reviews_csv = 'data_files\_rourkela_nit_reviews.csv',path_to_other_csv = 'data_files\_rourkela_nit_others.csv')

# 14. NIT Jamshedpur
others_nit_jmd = create_datasets(get_offset_url="https://collegedunia.com/university/25584-national-institute-of-technology-nit-jamshedpur/reviews",college_id="25584", path_to_reviews_csv = 'data_files\jmd_nit_reviews.csv',path_to_other_csv = 'data_files\jmd_nit_others.csv')

# 15. NIT Raipur
others_nit_raipur = create_datasets(get_offset_url="https://collegedunia.com/university/25442-national-institute-of-technology-nit-raipur/reviews",college_id="25442", path_to_reviews_csv = 'data_files\_raipur_nit_reviews.csv',path_to_other_csv = 'data_files\_raipur_nit_others.csv')

# 16. NIT Agartala
others_nit_agartala = create_datasets(get_offset_url="https://collegedunia.com/university/25916-national-institute-of-technology-nit-agartala/reviews",college_id="25916", path_to_reviews_csv = 'data_files\_agartala_nit_reviews.csv',path_to_other_csv = 'data_files\_agartala_nit_others.csv')

# 17. NIT Silchar
others_nit_silchar = create_datasets(get_offset_url="https://collegedunia.com/university/25399-national-institute-of-technology-nit-silchar/reviews",college_id="25399", path_to_reviews_csv = 'data_files\_silchar_nit_reviews.csv',path_to_other_csv = 'data_files\_silchar_nit_others.csv')

# 18. VIT
others_vit = create_datasets(get_offset_url="https://collegedunia.com/university/56865-vit-university-vit-chennai/reviews",college_id="56865", path_to_reviews_csv = 'data_files\_vit_reviews.csv',path_to_other_csv = 'data_files\_vit_others.csv')

# 19. SRM
others_srm = create_datasets(get_offset_url="https://collegedunia.com/university/56189-srm-institute-of-science-and-technology-ramapuram-campus-chennai/reviews",college_id="56189", path_to_reviews_csv = 'data_files\_srm_reviews.csv',path_to_other_csv = 'data_files\_srm_others.csv')

# 20. KGEC
others_kgec = create_datasets(get_offset_url="https://collegedunia.com/college/13966-kalyani-government-engineering-college-kgec-nadia/reviews",college_id="13966", path_to_reviews_csv = 'data_files\_kgec_reviews.csv',path_to_other_csv = 'data_files\_kgec_others.csv')

# 21. Amity Noida
others_amity_noida = create_datasets(get_offset_url="https://collegedunia.com/university/54797-amity-university-noida/reviews",college_id="54797", path_to_reviews_csv = 'data_files\_amity_reviews.csv',path_to_other_csv = 'data_files\_amity_others.csv')

# 22. Poornima University
others_poornima = create_datasets(get_offset_url="https://collegedunia.com/university/25837-poornima-university-pu-jaipur/reviews",college_id="25837", path_to_reviews_csv = 'data_files\_poornima_reviews.csv',path_to_other_csv = 'data_files\_poornima_others.csv')

# 23. Rajasthan Institute of Engineering and Technology
others_riet = create_datasets(get_offset_url="https://collegedunia.com/college/14719-rajasthan-institute-of-engineering-and-technology-riet-jaipur/reviews",college_id="14719", path_to_reviews_csv = 'data_files\_riet_reviews.csv',path_to_other_csv = 'data_files\_riet_others.csv')

# 24. IIT Delhi
others_iit_delhi = create_datasets(get_offset_url="https://collegedunia.com/university/25455-indian-institute-of-technology-iit-new-delhi/reviews",college_id="25455", path_to_reviews_csv = 'data_files\iit_delhi_reviews.csv',path_to_other_csv = 'data_files\iit_delhi_others.csv')

# 25. Bharath University
others_biher = create_datasets(get_offset_url="https://collegedunia.com/university/25871-bharath-university-bharath-institute-of-higher-education-and-research-biher-chennai/reviews",college_id="25871", path_to_reviews_csv = 'data_files\_biher_reviews.csv',path_to_other_csv = 'data_files\_biher_others.csv')

# 26. Anna University
others_anna = create_datasets(get_offset_url="https://collegedunia.com/university/25863-anna-university-au-chennai/reviews",college_id="25863", path_to_reviews_csv = 'data_files/review_CSVs/_anna_reviews.csv',path_to_other_csv = 'data_files\_anna_others.csv')

# 27. UEM Jaipur
others_uem_jaipur = create_datasets(get_offset_url="https://collegedunia.com/university/25851-university-of-engineering-and-management-uem-jaipur/reviews",college_id="25851", path_to_reviews_csv = 'data_files/review_CSVs/_uem_jaipur_reviews.csv',path_to_other_csv = 'data_files\_uem_jaipur_others.csv')

# 28. UEM Kolkata
others_uem_kol = create_datasets(get_offset_url="https://collegedunia.com/university/57446-university-of-engineering-and-management-uem-kolkata/reviews",college_id="57446", path_to_reviews_csv = 'data_files/review_CSVs/_uem_kolkata_reviews.csv',path_to_other_csv = 'data_files\_uem_kolkata_others.csv')

# 29. Chandigarh University
others_chandigarh = create_datasets(get_offset_url="https://collegedunia.com/university/25777-chandigarh-university-cu-chandigarh/reviews",college_id="25777", path_to_reviews_csv = 'data_files/review_CSVs/_chandigarh_univ_reviews.csv',path_to_other_csv = 'data_files\_chandigarh_univ_others.csv')

# 30. Jaipur National University
others_jnu = create_datasets(get_offset_url="https://collegedunia.com/university/25819-jaipur-national-university-jnu-jaipur/reviews",college_id="25819", path_to_reviews_csv = 'data_files/review_CSVs/_jnu_reviews.csv',path_to_other_csv = 'data_files\_jnu_others.csv')

# 31. Sharda University
others_sharda = create_datasets(get_offset_url="https://collegedunia.com/university/25972-sharda-university-su-greater-noida/reviews",college_id="25972", path_to_reviews_csv = 'data_files/review_CSVs/_sharda_reviews.csv',path_to_other_csv = 'data_files\_sharda_others.csv')

# 32. LPU
others_lpu = create_datasets(get_offset_url="https://collegedunia.com/university/25787-lovely-professional-university-lpu-jalandhar/reviews",college_id="25787", path_to_reviews_csv = 'data_files/review_CSVs/_lpu_reviews.csv',path_to_other_csv = 'data_files\_lpu_others.csv')

# 33. Christ University
others_christ_univ = create_datasets(get_offset_url="https://collegedunia.com/university/25598-christ-university-bangalore/reviews",college_id="25598", path_to_reviews_csv = 'data_files/review_CSVs/_christ_univ_reviews.csv',path_to_other_csv = 'data_files\_christ_univ_others.csv')

# 34. MNIT
others_mnit = create_datasets(get_offset_url="https://collegedunia.com/university/25828-malaviya-national-institute-of-technology-mnit-jaipur/reviews",college_id="25828", path_to_reviews_csv = 'data_files/review_CSVs/_mnit_reviews.csv',path_to_other_csv = 'data_files\_mnit_others.csv')

# 35. Heritage Institute of Technology
others_hit = create_datasets(get_offset_url="https://collegedunia.com/college/13708-heritage-institute-of-technology-hit-kolkata/reviews",college_id="13708", path_to_reviews_csv = 'data_files/review_CSVs/_hit_reviews.csv',path_to_other_csv = 'data_files\_hit_others.csv')

# 36. Techno India
others_techno = create_datasets(get_offset_url="https://collegedunia.com/university/15439-techno-india-university-kolkata/reviews",college_id="15439", path_to_reviews_csv = 'data_files/review_CSVs/_techno_reviews.csv',path_to_other_csv = 'data_files\_techno_others.csv')

# 37. Haldia Institute of Technology
others_haldia = create_datasets(get_offset_url="https://collegedunia.com/college/13695-haldia-institute-of-technology-hit-haldia/reviews",college_id="13695", path_to_reviews_csv = 'data_files/review_CSVs/_haldia_reviews.csv',path_to_other_csv = 'data_files\_haldia_others.csv')

# 38. JIS College of Engineering
others_JIS = create_datasets(get_offset_url="https://collegedunia.com/college/45696-jis-college-of-engineering-jisce-kolkata/reviews",college_id="45696", path_to_reviews_csv = 'data_files/review_CSVs/_JIS_reviews.csv',path_to_other_csv = 'data_files\_JIS_others.csv')

# 39. IIEST Shibpur
others_iiest_shibpur = create_datasets(get_offset_url="https://collegedunia.com/university/28330-indian-institute-of-engineering-science-and-technology-iiest-shibpur-howrah/reviews",college_id="28330", path_to_reviews_csv = 'data_files/review_CSVs/_iiest_shibpur_reviews.csv',path_to_other_csv = 'data_files\_iiest_shibpur_others.csv')

# 40. DTU
others_dtu = create_datasets(get_offset_url="https://collegedunia.com/university/25449-delhi-technological-university-dtu-new-delhi/reviews",college_id="25449", path_to_reviews_csv = 'data_files/review_CSVs/_dtu_reviews.csv',path_to_other_csv = 'data_files\_dtu_others.csv')

# 41. NIT Delhi
others_nit_delhi = create_datasets(get_offset_url="https://collegedunia.com/university/25464-national-institute-of-technology-nit-new-delhi/reviews",college_id="25464", path_to_reviews_csv = 'data_files/review_CSVs/_nit_delhi_reviews.csv',path_to_other_csv = 'data_files\_nit_delhi_others.csv')

# 42. KJ Somaiya KJSIEIT
others_kjsieit = create_datasets(get_offset_url="https://collegedunia.com/college/13917-kj-somaiya-institute-of-engineering-and-information-technology-kjsieit-mumbai/reviews",college_id="13917", path_to_reviews_csv = 'data_files/review_CSVs/_kjsieit_reviews.csv',path_to_other_csv = 'data_files\_kjsieit_others.csv')

# 443. Thadomal TSEC
others_tsec = create_datasets(get_offset_url="https://collegedunia.com/college/15452-thadomal-shahani-engineering-college-tsec-mumbai/reviews",college_id="15452", path_to_reviews_csv = 'data_files/review_CSVs/_tsec_reviews.csv',path_to_other_csv = 'data_files\_tsec_others.csv')
'''
# 443. Thakur college
others_thakur = create_datasets(get_offset_url="https://collegedunia.com/college/54796-thakur-college-of-engineering-and-technology-tcet-mumbai/reviews",college_id="54796", path_to_reviews_csv = 'data_files/review_CSVs/_thakur_reviews.csv',path_to_other_csv = 'data_files\_thakur_others.csv')