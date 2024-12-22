FROM nginx:latest

# 建立 static 目錄
RUN mkdir /usr/share/nginx/html/static
COPY nginx.conf /etc/nginx/nginx.conf
# 將 shared_data 資料夾中的 index.html 複製到 Nginx 的 static 目錄
COPY index.html /usr/share/nginx/html/index.html
# 暴露 Nginx 預設埠
EXPOSE 80
