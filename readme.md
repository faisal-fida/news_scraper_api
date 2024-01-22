# Pakistan News API

## A FastApi, httpx and docker-compose powered App.

### How to run

- Clone the repo
- Run `docker-compose up --build`
- Go to `http://localhost:8000/docs` to see the docs

### How to run tests

- Run `docker-compose run --rm app sh -c "python -m pytest"`

### Features

- [x] Get news from Dawn, Express Tribune, The News, Geo News, Samaa News, ARY News
- [x] Used httpx to make async requests
- [x] Used FastApi to create the API
- [x] Used docker-compose to run the app
- [x] Used pytest to write tests
- [x] Scrape news in database and serve from there

### TODO

- [ ] Add more news sources
- [ ] Improve the keyword search
- [ ] Add pagination

### API Endpoints Example

- `/news/dawn` - Get all news from Dawn
- `/news/dawn/imran-khan` - Get all news from Dawn with keyword Imran Khan
- `/news/dawn/imran-khan/2` - Get all news from Dawn with keyword Imran Khan and page 2

### Response Example

```json
{
  "news": [
    {
      "title": "Pakistan, India agree to halt cross-border firing in Kashmir",
      "link": "https://www.example.com/news/1603246/",
      "description": "The militaries of Pakistan and India agreed on Thursday...",
      "image": "https://www.example.com/image.jpg",
      "published": "2021-02-25T15:00:00+05:00"
    },
    {
      "title": "Pakistan, India agree to halt cross-border firing in Kashmir",
      "link": "https://www.example.com/news/1603246/",
      "description": "The militaries of Pakistan and India agreed on Thursday...",
      "image": "https://www.example.com/image.jpg",
      "published": "2021-02-25T15:00:00+05:00"
    }
  ]
}
```

### Final Words

- If you have any questions, feel free to ask. You can reach me at [LinkedIn](https://www.linkedin.com/in/faisal-fida/)
- If you like the project, please give it a star. It will be much appreciated.

### Credits

- [FastApi](https://fastapi.tiangolo.com/)
- [Docker](https://www.docker.com/)

### License

MIT
