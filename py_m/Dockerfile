FROM python:latest

WORKDIR /app
RUN mkdir templates

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install cryptography

COPY . .

RUN mv index.html templates/
RUN mv app.py templates/

CMD ["python", "/app/templates/app.py"]
