FROM mysql:latest

# 設定 root 使用者密碼
ENV MYSQL_ROOT_PASSWORD "dockerHW"

# 複製 CSV 檔案和 SQL 腳本到容器中
COPY Titanic-Dataset.csv /var/lib/mysql-files/data.csv
COPY import.sql /docker-entrypoint-initdb.d/

# 暴露 MySQL 預設埠
EXPOSE 3306
