# inputでレコードを追加する方法

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
    name, address, telephone = input("氏名、住所、電話番号を半角区切りで入力").split()
    sql = f"INSERT INTO Address (name, address, telephone) VALUES ('{name}','{address}','{telephone}');"
    # SQL実行
    cur.execute(sql)

# 変更をcommitしないと反映されない。
# postgreにおいてはDDLはcommit必須、DMLは自動commitされるのでいらない。
connection.commit()

# 接続を閉じる
connection.close()
