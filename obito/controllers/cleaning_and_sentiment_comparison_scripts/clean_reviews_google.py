import pandas as pd
import numpy as np
import string,re,nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from html.parser import HTMLParser
# from translate import Translator
from googletrans import Translator

# Run this only once, then comment it out
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

##################################################### MAIN FUNCTIONS #######################################################

# Apostrophe lookup
# Apostrophe constraction map
CONTRACTION_MAP = {
"ain't": "is not",
"aren't": "are not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he would",
"he'd've": "he would have",
"he'll": "he will",
"he'll've": "he he will have",
"he's": "he is",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how is",
"I'd": "I would",
"I'd've": "I would have",
"I'll": "I will",
"I'll've": "I will have",
"I'm": "I am",
"I've": "I have",
"i'd": "i would",
"i'd've": "i would have",
"i'll": "i will",
"i'll've": "i will have",
"i'm": "i am",
"i've": "i have",
"isn't": "is not",
"it'd": "it would",
"it'd've": "it would have",
"it'll": "it will",
"it'll've": "it will have",
"it's": "it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"o'clock": "of the clock",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she would",
"she'd've": "she would have",
"she'll": "she will",
"she'll've": "she will have",
"she's": "she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so as",
"that'd": "that would",
"that'd've": "that would have",
"that's": "that is",
"there'd": "there would",
"there'd've": "there would have",
"there's": "there is",
"they'd": "they would",
"they'd've": "they would have",
"they'll": "they will",
"they'll've": "they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
"we'd": "we would",
"we'd've": "we would have",
"we'll": "we will",
"we'll've": "we will have",
"we're": "we are",
"we've": "we have",
"weren't": "were not",
"what'll": "what will",
"what'll've": "what will have",
"what're": "what are",
"what's": "what is",
"what've": "what have",
"when's": "when is",
"when've": "when have",
"where'd": "where did",
"where's": "where is",
"where've": "where have",
"who'll": "who will",
"who'll've": "who will have",
"who's": "who is",
"who've": "who have",
"why's": "why is",
"why've": "why have",
"will've": "will have",
"won't": "will not",
"won't've": "will not have",
"would've": "would have",
"wouldn't": "would not",
"wouldn't've": "would not have",
"y'all": "you all",
"y'all'd": "you all would",
"y'all'd've": "you all would have",
"y'all're": "you all are",
"y'all've": "you all have",
"you'd": "you would",
"you'd've": "you would have",
"you'll": "you will",
"you'll've": "you will have",
"you're": "you are",
"you've": "you have"
}
# Punctuation lookup
PUNCTUATIONS_LOOKUP = '''!()[]{};:'"\,<>./?@#$%^&*_~--'''
# Combine repetitive whitespaces to one single whitespace
COMBINE_WHITESPACE_REGEX = re.compile(r"\s+")
# Strip trailing dots
STRIP_TRAIL = re.compile(r" …")
# Translator using Google API
translator = Translator()

# Function
def clean_reviews(text,lemmatizer = WordNetLemmatizer(), contractions = CONTRACTION_MAP,punctuations = PUNCTUATIONS_LOOKUP,combine_whitespace = COMBINE_WHITESPACE_REGEX,remove_trail = STRIP_TRAIL,translate_object = translator):
    # Translate to English if not in english
    try:
        text_translated = translate_object.translate(text,dest='en')
    except:
        text_translated = text
    # Lowercase
    text_lower = text_translated.lower()
    # Resolve contractions/apostrophe lookup
    cleaned = [contractions[word] if word in contractions else word for word in text_lower.split()]
    clean_apostrophes = " ".join(cleaned)
    # Decode emojis, symbols, signs.
    apostrophe_cleaned = clean_apostrophes.encode('ascii','ignore').decode("utf8")
    # Remove newlines, tabs and extra spaces
    strip_newline_tab = apostrophe_cleaned.translate(str.maketrans('\n\t','  ',punctuations))
    strip_whitespace = combine_whitespace.sub(" ", strip_newline_tab).strip()
    # Some reviews have --> (translated by google), in them, strip it.
    pre_final_cleaned = re.compile(r"translated by google ").sub("", strip_whitespace).strip()
    # Strip trailing dots
    strip_trails = re.compile(r" …").sub("", pre_final_cleaned).strip()
    # Remove any other non-alphanumeric characters that may have been ignored
    final_cleaned = re.sub(r'\W+', ' ', strip_trails).lstrip()
    return final_cleaned

# Clean the dataset
def cleaned_feature(dataset):
    dataset['cleaned_reviews'] = dataset['Unnamed: 0'].apply(clean_reviews)
    return dataset

############################################################################################################################
