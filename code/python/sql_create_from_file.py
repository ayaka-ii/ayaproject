# 別に存在するSQLスクリプトを読み込んで実行する方法

import psycopg2
import os # 環境変数を取得するライブラリ

# 接続情報を記載
connection = psycopg2.connect(
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)
# カーソルオブジェクト作成（カーソル＝DB操作するためのオブジェクト）
# withで開いて閉じる。withによりエラーが起きても必ず閉じられる。
with connection.cursor() as cur:
    with open("sql_create.sql","r") as file: # SQLスクリプトを参照
        sql = file.read()
    cur.execute(sql) # 読み込んだSQL文を実行
        
# 変更をcommitしないと反映されない。
# postgreにおいてはDDLはcommit必須、DMLは自動commitされるのでいらない。
connection.commit()

# 接続を閉じる
connection.close()