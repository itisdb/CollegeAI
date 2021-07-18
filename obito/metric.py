import os, sys
PWD = os.getenv('PWD')

os.chdir(PWD)
sys.path.insert(0, os.getenv('PWD'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.local")

import django
django.setup()

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
from college.models import College
from reviews.models import Review

from review_analysis import Analysis
from obito.controllers.data_sanitize.generic_scraper import Scraper


class Metric:
    def __init__(self, college: College):
        self.college = college

    def invoke(self):
        self.scraping()
        score = self.reviews()
        metric = self.final_metric(score)
        if metric:
            p_points, a_points, i_points = self.points(metric)
            self.store_metrics(metric, p_points, a_points, i_points)
            print("Score: \n Placements: ",p_points,'/5 \n Academics: ',a_points,'/5 \n Infrastructure:',i_points,'/5')

    def store_metrics(self, metrics, p_points, a_points, i_points):
        self.college.detailed_metrics = metrics
        self.college.metrics = {
            'PLACEMENT': p_points * 2,
            'ACADEMICS': a_points * 2,
            'INFRASTRUCTURE': i_points * 2
        }
        self.college.save()

    def scraping(self):
        x = Scraper()
        x.invoke(self.college)

    def reviews(self):
        y = Analysis(self.college)
        score = y.invoke()
        return score

    def final_metric(self, score):
        a_pos, a_neg, a_neu, a_com = 0, 0, 0, 0
        p_pos, p_neg, p_neu, p_com = 0, 0, 0, 0
        i_pos, i_neg, i_neu, i_com = 0, 0, 0, 0
        length = len(score)
        if length > 0:
            for element in score:
                p_neg += element[0]['negative']
                p_pos += element[0]['positive']
                p_neu += element[0]['neutral']
                p_com += element[0]['compound']
                a_neg += element[1]['negative']
                a_pos += element[1]['positive']
                a_neu += element[1]['neutral']
                a_com += element[1]['compound']
                i_neg += element[2]['negative']
                i_pos += element[2]['positive']
                i_neu += element[2]['neutral']
                i_com += element[2]['compound']
            metric = [{'metric': 'PLACEMENTS', 'negative': p_neg / length, 'positive': p_pos / length,
                       'neutral': p_neu / length, 'compound': p_com / length},
                      {'metric': 'ACADEMICS', 'negative': a_neg / length, 'positive': a_pos / length,
                       'neutral': a_neu / length, 'compound': a_com / length},
                      {'metric': 'INFRASTRUCTURE', 'negative': i_neg / length, 'positive': i_pos / length,
                       'neutral': i_neu / length, 'compound': i_com / length}]
            return metric

    def points(self,metric):
        p_points = round((metric[0]['compound'])*5, 1)
        a_points = round((metric[1]['compound']) * 5, 1)
        i_points = round((metric[2]['compound']) * 5, 1)

        return p_points, a_points, i_points


'''
college = College.objects.all().first()
z = Metric(college)
z.invoke()

r = Review.objects.all()
s = r.filter(comment = "everything is good at this college. wi-fi facility is available at normal speed. classrooms are average, and the library is well spaced. there is a 24 hours open medical facility. labs are placed accordingly. sports and game...")
print(len(s))
'''

