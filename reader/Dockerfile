FROM python:2.7

WORKDIR /app

COPY . /app

RUN pip install -r requirements

EXPOSE 8000

ENTRYPOINT ["python"]

CMD ["reader.py"]
