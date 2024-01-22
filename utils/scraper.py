import timeit
import json
import httpx
import asyncio
from datetime import datetime
from bs4 import BeautifulSoup as bs

from db_init import insert_data

news_db_data = []

semaphore = asyncio.Semaphore(100)

async def get(url):
    async with semaphore:
        async with httpx.AsyncClient(timeout=15) as client:
            response = await client.get(url)
            return response.text

async def get_news_urls(page_no: int) -> list:
        url = f"https://tribune.com.pk/latest?page={page_no}"
        html = await get(url)
        soup = bs(html, "html.parser")
        news_urls = soup.select("div.horiz-news3-caption a[href*=story]")
        if news_urls:
            parsed_news_urls = [url["href"] for url in news_urls]
            return parsed_news_urls
        else:
            print("No news found")
            return None


async def get_news_data(url: str):
    html = await get(url)
    soup = bs(html, "html.parser")
    title = soup.select_one("div.story-box-section h1")
    title = title.text if title else None
    author = soup.select_one("div.left-authorbox span a")
    author = author.text if author else None
    date = soup.select_one("div.left-authorbox span:nth-child(2)")
    if date:
        date = date.text
        date = datetime.strptime(date, "%B %d, %Y").strftime("%Y-%m-%d")
    article_text = soup.select_one("span.story-text")
    article_text = article_text.text if article_text else None
    news_data = {"title": title, "author": author, "date": date, "article_text": article_text, "url": url}
    news_db_data.append(news_data)
    if len(news_db_data) % 1000 == 0:
        await insert_data(news_db_data)
        news_db_data.clear()

async def main():
    start = timeit.default_timer()
    print("Fetching news urls...")
    news_urls = await asyncio.gather(*[get_news_urls(page_no) for page_no in range(900, 5000)])
    print("Fetching news data...")  
    news_urls = [url for page_urls in news_urls for url in page_urls]
    await asyncio.gather(*[get_news_data(url) for url in news_urls])
    stop = timeit.default_timer()
    print("Time: ", stop - start)

asyncio.run(main())