from typing import Optional
from fastapi import FastAPI
from textblob import TextBlob
from models import Date_Time, Quote, Sentiment, SentimentPostQuery
import uvicorn
from datetime import datetime
import json
import random

def load_quotes():
    f = open('quotes.json',)
    quotes = json.load(f)
    f.close()
    return quotes

app = FastAPI()
quotes = load_quotes()


@app.get("/")
def root():
    return {"message":"Hello World!"}

@app.get("/hi/{name}")
def hi(name: str):
    return {"message":f"Hello {name}!"}

@app.get("/time", response_model=Date_Time)
def get_time():
    return {"datetime": datetime.now().strftime("%d/%m/%Y %H:%M:%S")}

def calc_sentiment(phrase:str) -> Sentiment:
    token = TextBlob(phrase)
    score = token.sentiment.polarity
    dict = {'sentiment': score, 'phrase': phrase}
    sentiment = Sentiment(**dict)
    return sentiment

@app.get("/sentiment/{phrase}", response_model=Sentiment)
def get_sentiment(phrase: str):
    sentiment = calc_sentiment(phrase)
    return sentiment

@app.post("/sentiment", response_model=Sentiment)
def post_sentiment(query:SentimentPostQuery):
    sentiment = calc_sentiment(query.phrase)
    return sentiment

@app.get("/quote", response_model=Quote)
def get_quote():
    return quotes[random.randint(1,len(quotes)-1)]

@app.get("/quote_sentiment", response_model=Sentiment)
def get_quote_with_sentiment():
    quote = get_quote()
    sentiment = get_sentiment(quote["quoteText"])
    return sentiment

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
    pass