from clean_reviews_google import clean_reviews,cleaned_feature
import pandas as pd
import nltk
from nltk.corpus import state_union
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon
nltk.download('state_union')
nltk.download('vader_lexicon')
nltk.download('punkt')

# Select one dataset to work on
data = pd.read_csv("../data_files/new_CSVs/NIT_delhi_reviews.csv")
# Remove NaN values
try:
    data.dropna(inplace=True)
except:
    data = data[data['Unnamed: 0'] != 'NaN']
# Clean the data
cleaned_data = cleaned_feature(dataset = data)
print(cleaned_data.head(10))

# Create sentiment analysis model
def sentiment_analysis(text, model = SentimentIntensityAnalyzer(), tokenizer = PunktSentenceTokenizer(train_text = state_union.raw('2006-GWBush.txt'))):
    review_sentences = tokenizer.tokenize(text)
    for sentence in review_sentences:
        polarity_scores = model.polarity_scores(sentence)
        # 0 = positive, 1 = negative, 2 = neutral
        if polarity_scores['pos'] > polarity_scores['neg']:
            return 0
        elif polarity_scores['pos'] < polarity_scores['neg']:
            return 1
        else:
            return 2

# Transform dataset
cleaned_data['sentiment'] = cleaned_data['cleaned_reviews'].apply(sentiment_analysis)
print(cleaned_data.head(10))
