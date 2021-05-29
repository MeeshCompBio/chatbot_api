# chatbot_api

Example repo using Chatterbot and FastAPI to make an api chatbot

## getting started

You can run this application in docker using the commands:

```bash
docker build -t meeshcompbio/chatbot_api .
docker run -p 8887:80 meeshcompbio/chatbot_api
```

You can then go to <localhost:8887/docs> to get to the swagger UI for testing
