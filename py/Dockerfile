FROM python3.13
WORKDIR /py_dir
ENV DEBIAN_FRONTEND=noninteractive
RUN pip install --no-cache-dir pymysql flask
COPY . .
CMD ["python","app.py"]
