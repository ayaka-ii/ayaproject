# SQL文をpythonスクリプトに直接書く方法

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
    # Addressテーブル作成。IF NOT EXISTSで同じテーブル名が存在する場合にエラーにせず注意喚起のみする
    sql = '''
        CREATE TABLE IF NOT EXISTS Address (
            id SERIAL PRIMARY KEY,
            name varchar(30) NOT NULL,
            address varchar(100) NOT NULL);
        '''
    # SQL実行
    cur.execute(sql)

# 変更をcommitしないと反映されない。
# postgreにおいてはDDLはcommit必須、DMLは自動commitされるのでいらない。
connection.commit()

# 接続を閉じる
connection.close()
