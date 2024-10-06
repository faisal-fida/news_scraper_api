
# News Scraper API

This project is a FastAPI-based web application designed to scrape news data from the web and store it in a Supabase database. It uses asynchronous programming to efficiently fetch and process large amounts of data.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Complexities](#complexities)
- [Solutions](#solutions)
- [Challenges](#challenges)
- [License](#license)

## Installation

1. Clone the repository:

```sh
git clone https://github.com/faisal-fida/news_scraper_api.git
cd news_scraper_api
```

2. Install the dependencies:

```sh
pip install -r requirements.txt
```

3. Create a `.env` file with the following content:

```
SUPABASE_URL=<your_supabase_url>
SUPABASE_KEY=<your_supabase_key>
```

4. Run the application:

```sh
uvicorn app:app --reload
```

## Usage

The application provides two endpoints:

1. `GET /` - Returns the status of the API.
2. `GET /news` - Fetches the latest news data.

## Features

- **Asynchronous Programming**: The project uses Python's `asyncio` and `httpx` libraries to perform asynchronous HTTP requests, significantly improving the efficiency and performance of data scraping.
- **Database Integration**: Utilizes Supabase as a backend database to store and manage the scraped news data.
- **Web Scraping**: Uses BeautifulSoup to parse HTML and extract relevant news information from web pages.
- **Efficient Data Fetching**: By implementing a semaphore and asynchronous requests, the project is capable of handling multiple concurrent connections, thus speeding up the data fetching process.
- **Database Operations**: The project includes functions to insert, retrieve, and update data in Supabase, ensuring that the data is stored and managed effectively.
- **Error Handling**: The project includes basic error handling to manage scenarios where data cannot be fetched or inserted into the database.
- **Rate Limiting**: Managing the rate at which requests are made to avoid being blocked by the target website.
- **Data Consistency**: Ensuring that data is consistently and correctly scraped, parsed, and stored in the database.
- **Scalability**: Making sure the application can handle large volumes of data and scale effectively with increased load.
