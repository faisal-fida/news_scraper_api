import json
import httpx
import asyncio
from bs4 import BeautifulSoup as bs

async def get(url):
    async with httpx.AsyncClient() as client:
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


async def get_news_data(url: str) -> dict:
    html = await get(url)
    soup = bs(html, "html.parser")
    title = soup.select_one("div.story-box-section h1")
    title = title.text if title else None
    author = soup.select_one("div.left-authorbox span a")
    author = author.text if author else None
    date = soup.select_one("div.left-authorbox span:nth-child(2)")
    date = date.text if date else None
    article_text = soup.select_one("span.story-text")
    article_text = article_text.text if article_text else None
    print(f"Scraping {url}")
    return {"title": title, "url": url, "date": date, "article_text": article_text}


async def main():
    news_urls = await asyncio.gather(*[get_news_urls(page_no) for page_no in range(1, 10)])
    news_urls = [url for page_urls in news_urls for url in page_urls]
    news_data = await asyncio.gather(*[get_news_data(url) for url in news_urls])
    with open("news_data.json", "w") as f:
        json.dump(news_data, f)
    return news_data

asyncio.run(main())