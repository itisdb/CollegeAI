import pandas as pd
import numpy as np
import string,re,nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Run only once, then comment it out
from obito.controllers.cleaning_and_sentiment_comparison_scripts.clean_reviews_google import clean_reviews

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

##################################################### MAIN FUNCTIONS #######################################################

# define punctuation
punctuations = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
'''
Ususally, during sentiment analysis, we use stemming, coz grammatically correct words don't matter
here because our algorithm is not going to interact with a user or output text (as in chatbots).
But since here we're working with
'''
def basic_nltk_cleaning(text,stopwords_set = set(stopwords.words('english')),lemmatizer = WordNetLemmatizer(),punctuations=punctuations):
    sentences = nltk.sent_tokenize(text)
    tokenized,cleaned_list = [],[]
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        tokenized.append(words)
    for token in tokenized:
        # Lower case
        tokenized_lower = [word.lower() for word in token]
        # Remove stopwords, punctuations and lemmatize
        tokenized_lemma = [lemmatizer.lemmatize(word) for word in tokenized_lower if word not in stopwords_set]
        cleaned_list.append(" ".join(tokenized_lemma))
        print(cleaned_list)
    final_punctuated = " ".join(cleaned_list)
    _RE_COMBINE_WHITESPACE = re.compile(r"\s+")
    final_cleaned = final_punctuated.translate(str.maketrans('\n\t','  ',punctuations))
    final_cleaned = _RE_COMBINE_WHITESPACE.sub(" ", final_cleaned).strip()
    return final_cleaned

# Clean the dataset
def cleaned_feature(dataset = data):
    dataset['cleaned_reviews'] = dataset['Unnamed: 0'].apply(clean_reviews)
    return dataset

############################################################################################################################
