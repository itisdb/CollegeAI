import pandas as pd
import re
import os, sys
PWD = os.getenv('PWD')

os.chdir(PWD)
sys.path.insert(0, os.getenv('PWD'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.local")

import django
django.setup()

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()


from reviews.models import Review
from obito.constants import academics, placements, infrastructure


# Making the class for review sentiment analysis

class Analysis:

    def __init__(self):
        self.reviews = Review.objects.all()

    def invoke(self):
        df = pd.DataFrame()
        review = []
        a_positive, a_negative,a_neutral,a_score = [],[],[],[]
        p_positive, p_negative,p_neutral,p_score = [],[],[],[]
        i_positive, i_negative,i_neutral,i_score = [],[],[],[]

        for s in self.reviews:
#            self.lowercase(s)
#            self.sanitization(s)
            reviews = self.splitting(s)

            a_list = self.academic(reviews)
            p_list = self.placement(reviews)
            i_list = self.infrastructure(reviews)

            if(len(reviews)>0):
                review.append(s.comment)

                if (len(a_list)>0):
                    pos,neg,neu,compound = self.a_analysis(a_list)
                else:
                    pos, neg, neu, compound = 0,0,0,0

                a_positive.append(pos)
                a_negative.append(neg)
                a_neutral.append(neu)
                a_score.append(compound)

                if (len(p_list) > 0):
                    pos, neg, neu, compound = self.p_analysis(p_list)
                else:
                    pos, neg, neu, compound = 0, 0, 0, 0

                p_positive.append(pos)
                p_negative.append(neg)
                p_neutral.append(neu)
                p_score.append(compound)

                if (len(i_list) > 0):
                    pos, neg, neu, compound = self.i_analysis(i_list)
                else:
                    pos, neg, neu, compound = 0, 0, 0, 0

                i_positive.append(pos)
                i_negative.append(neg)
                i_neutral.append(neu)
                i_score.append(compound)

        dict = {"Review":review, " Academic Positive": a_positive, " Academic Negative":a_negative,
                "Academic Neutral":a_neutral, "Academic Score":a_score , " Placements Positive": p_positive,
                " Placements Negative":p_negative,"Placements Neutral":p_neutral, "Placements Score":p_score,
                " Infrastructure Positive": i_positive, " Infrastructure Negative":i_negative,
                "Infrastructure Neutral":i_neutral, "Infrastructure Score":i_score}

        df = pd.DataFrame(dict)
        df.to_csv("scores.csv")


    def lowercase(self,s):
        s.comment = s.comment.lower()
        s.save()

    def sanitization(self,s):
        try:
            s.comment = s.comment.replace("\n", " ")
            s.comment = s.comment.replace("\r", " ")
            s.comment = s.comment.replace("\t", " ")
            s.save()
        except:
            pass

    def splitting(self,s):
        lst = []
        regex = re.compile(r' [\w.()]{1,2}\.')
        rep = regex.sub(" ", s.comment)
        lst.extend(rep.split("."))
        reviews = [i for i in lst if i != '']
        return reviews

    def a_analysis(self,reviews):
        
        lst = [sid.polarity_scores(review) for review in reviews]
        pos_list = [score['pos'] for score in lst]
        neg_list = [score['neg'] for score in lst]
        neu_list = [score['neu'] for score in lst]
        compound_list = [score['compound'] for score in lst]

        pos = sum(pos_list)/len(pos_list)
        neg = sum(neg_list)/len(neg_list)
        neu = sum(neu_list)/len(neu_list)
        compound = sum(compound_list)/len(compound_list)

        return pos,neg,neu,compound

    def p_analysis(self, reviews):

        lst = [sid.polarity_scores(review) for review in reviews]
        pos_list = [score['pos'] for score in lst]
        neg_list = [score['neg'] for score in lst]
        neu_list = [score['neu'] for score in lst]
        compound_list = [score['compound'] for score in lst]

        pos = sum(pos_list) / len(pos_list)
        neg = sum(neg_list) / len(neg_list)
        neu = sum(neu_list) / len(neu_list)
        compound = sum(compound_list) / len(compound_list)

        return pos, neg, neu, compound

    def i_analysis(self, reviews):

        lst = [sid.polarity_scores(review) for review in reviews]
        pos_list = [score['pos'] for score in lst]
        neg_list = [score['neg'] for score in lst]
        neu_list = [score['neu'] for score in lst]
        compound_list = [score['compound'] for score in lst]

        pos = sum(pos_list) / len(pos_list)
        neg = sum(neg_list) / len(neg_list)
        neu = sum(neu_list) / len(neu_list)
        compound = sum(compound_list) / len(compound_list)

        return pos, neg, neu, compound

    def academic(self,reviews):
        a_list= []
        for l in reviews:
            for word in academics:
                if (l.find(word) != -1):
                    a_list.append(l)
                    break
        return a_list

    def placement(self,reviews):
        p_list= []
        for l in reviews:
            for word in placements:
                if (l.find(word) != -1):
                    p_list.append(l)
                    break
        return p_list

    def infrastructure(self,reviews):
        i_list= []
        for l in reviews:
            for word in infrastructure:
                if (l.find(word) != -1):
                    i_list.append(l)
                    break
        return i_list

x = Analysis()
x.invoke()

'''  
x = Analysis()
x.invoke()

'''