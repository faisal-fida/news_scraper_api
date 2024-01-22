from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from scraper import get_news_data

app = FastAPI()

class NewsData(BaseModel):
    title: str
    url: str
    date: str
    article_text: str

@app.get("/")
def read_root():
    return {"Api Status": "200 OK"}  

@app.get("/news")
def get_news():
    newsdata = get_news_data()
    if newsdata:
        return newsdata
    else:
        return {"Api Status": "500 Internal Server Error while fetching news data"}