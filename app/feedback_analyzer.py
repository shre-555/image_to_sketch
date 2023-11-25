import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

def get_max_sentiment(txt):
    sentiments= sia.polarity_scores(txt)
    del sentiments['compound']
    return max(sentiments, key=lambda x:sentiments[x])

def get_reply(txt):
    sentiment =get_max_sentiment(txt)
    if sentiment == 'pos':
        return "Thank you! We are glad that you liked it."
    elif sentiment == 'neu':
        return "Thank you for your feedback."
    elif sentiment == 'neg':
        return "We are continuously trying to improve. Thank you for your feedback"
