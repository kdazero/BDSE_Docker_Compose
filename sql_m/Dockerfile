FROM mysql:latest

# 設定 root 使用者密碼
ENV MYSQL_ROOT_PASSWORD "dockerHW"

# 複製 CSV 檔案和 到 container 中
# 此處必須要使用 /var/lib/mysql-files/ 此資料夾，container 才讀的到，我也不知道為啥，去問 MYSQL
COPY Titanic-Dataset.csv /var/lib/mysql-files/data.csv
# 在 container 啟動時 自動執行此 SQL 腳本
COPY import.sql /docker-entrypoint-initdb.d/

# MySQL 連接埠
EXPOSE 3306
