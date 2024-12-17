import os
import pymysql

class SQL_DB:
    
    def __init__(self, default_database=None):
        self.connection = pymysql.connect(
            host=os.getenv('MYSQL_HOST', 'localhost'),  # 默認值為 Docker Compose 中 MySQL 的服務名稱
            user=os.getenv('MYSQL_USER', 'root'),  # 使用環境變量，默認為 'root'
            password=os.getenv('MYSQL_PASSWORD', 'root'),  # 默認密碼
            port=int(os.getenv('MYSQL_PORT', 3306)),  # 默認 MySQL 端口
            database=default_database,  # 如果有指定的數據庫，則連接該數據庫
            cursorclass=pymysql.cursors.DictCursor
        )

    def show_DB(self):
        with self.connection.cursor() as cursor:
            cursor.execute('SHOW DATABASES')
            result = cursor.fetchall()
            return result

if __name__ == "__main__":
    try:
        print("Available Databases:")
        print(SQL_DB().show_DB())
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
