from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re


def clean_text(text):
    # remove any URLs
    text = re.sub(r"http\S+", "", text)
    # remove any special characters
    text = re.sub(r"[^A-Za-z0-9.!?]+", " ", text)
    return text


def analyze_sentiment(text, analyzer=None):
    # clean the text
    text = clean_text(text)
    # initialize the sentiment analyzer
    analyzer =  SentimentIntensityAnalyzer() if analyzer is None else analyzer
    # get the sentiment score
    sentiment_score = analyzer.polarity_scores(text)
    return sentiment_score


def main():
    # example text to analyze
    text = "I love this product! It's the best thing I've ever bought."
    # initialize the sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()
    # analyze the sentiment of the text
    sentiment_score = analyze_sentiment(text, analyzer)
    print(sentiment_score)


if __name__ == "__main__":
    main()