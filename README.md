#### FastAPI Sentiment
This project creates a Docker container that exposes an API to provide sentiment analysis

#### Building the container
docker build -t api-back .

#### Running the container
docker run -p 8000:8000 api-back

### Methods Exposed
- / -- Returns Hello World
- /time -- Returns current time
- [POST] /sentiment -- Returns sentiment analysis of given phrase
- /quote -- Returns random quote
- /quote_sentiment -- Returns random quote with Sentiment