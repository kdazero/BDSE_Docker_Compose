FROM nginx:latest

# 建立 static 目錄
RUN mkdir /usr/share/nginx/html/static

# 將 shared_data 資料夾中的 index.html 複製到 Nginx 的 static 目錄

# 暴露 Nginx 預設埠
EXPOSE 80

CMD ["cp", "/data/index.html", "/usr/share/nginx/html/static/"]
