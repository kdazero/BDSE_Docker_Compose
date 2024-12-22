from flask import Flask, render_template
import pymysql
import cryptography

app = Flask(__name__, template_folder='templates')

# MySQL 連線資訊
conn_str = {
    'host': 'sql_server',  # 使用 docker-compose 服務名稱作為主機名稱
    'user': 'root',  # 使用 root 使用者
    'password': 'dockerHW',  # 使用 root 使用者的密碼
    'database': 'mydatabase', 
    'port': 3306,  # MySQL 預設埠
}

@app.route('/')
def index():
    try:
        # 連接到 MySQL
        conn = pymysql.connect(**conn_str)
        cursor = conn.cursor()

        # 執行 SQL 查詢
        cursor.execute("SELECT * FROM TitanicCSV")
        data = cursor.fetchall()

        # 關閉連線
        cursor.close()
        conn.close()

        return render_template('index.html', data=data)

        # 渲染 HTML 模板並傳遞資料
        #rendered_html = render_template('index.html', data=data)

        # 將渲染好的 HTML 儲存到 shared_data 資料夾
        #with open('/data/index.html', 'w') as f:
        #    f.write(rendered_html)

        #return redirect(url_for('static', filename='index.html'))  # 重新導向到 Nginx 提供的靜態檔案
        #return rendered_html
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
