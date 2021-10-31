from typing import List, Optional
from pydantic import BaseModel, validator, ValidationError

class Sentiment(BaseModel):
    sentiment: float
    phrase: str

class SentimentPostQuery(BaseModel):
    phrase: str

class Date_Time(BaseModel):
    datetime: str

class Quote(BaseModel):
    quoteText: str
    quoteAuthor: str