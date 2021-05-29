FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY requirements/* .

RUN pip install -r prod.txt

COPY ./ /chatbot_api
WORKDIR /chatbot_api/app

ENV PYTHONPATH=/chatbot_api

RUN python main.py
EXPOSE 8888