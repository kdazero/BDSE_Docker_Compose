FROM python:latest

# 設定工作路徑 避免檔案混亂
WORKDIR /app
# Flask 渲染網頁必備資料夾
RUN mkdir templates

# 安裝套件
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 將 index.html / app.py 等導入
COPY . .

# 將要渲染的 html 放入 templates
RUN mv index.html templates/

# container 啟動時自動執行此程式
CMD ["python", "/app/app.py"]
