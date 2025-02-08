import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification
from transformers import pipeline


class StockSentiment:
    def __init__(self):
        model = BertForSequenceClassification.from_pretrained('yiyanghkust/finbert-tone', num_labels=3)
        tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')
        self.nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

    
    def get_sentiment(self, headline: str) -> str:
        result = self.nlp(headline)
        return result[0]['label'], result[0]['score']
    
    def get_sentiment_df(self, df: pd.DataFrame, column_name: str) -> pd.DataFrame:
        sentiments = df[column_name].apply(lambda x: self.get_sentiment(x))
        df['sentiment'] = sentiments.apply(lambda x: x[0])
        df['score'] = sentiments.apply(lambda x: x[1])
        return df