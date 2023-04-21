FROM python:alpine

RUN pip install postgres

RUN pip install python-dotenv

WORKDIR /app

COPY . /app

CMD ["python", "save_queries.py"]