import psycopg2
import os # 環境変数を取得するライブラリ
import json

import logging
logger = logging.getLogger(__name__)


connection = psycopg2.connect(
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

def select_students():
    try:
        with connection.cursor() as cur:
            sql = '''
                SELECT *
                FROM Address;
                '''
            cur.execute(sql)
            # 取得したデータをresultsに代入  
            results = cur.fetchall()
        list_result = []
        # データを1行ずつカラムをキーとした辞書にしてリストに追加
        for row in results:
            dict_result = dict()
            dict_result["id"] = row[0]
            dict_result["name"] = row[1]
            dict_result["address"] = row[2]
            dict_result["telephone"] = row[3]
            list_result.append(dict_result)
        # 辞書が要素となったリストを返す
        return list_result
    except Exception as e:
        # データベース接続に関するエラーハンドリング
        logger.exception("Error occured in /api/circles")
        pass

# WEBAPI用の関数
def json_students():
    # 辞書が要素になったリストをstudentsに代入
    students = select_students()
    # jsonに変換
    return json.dumps(students)

# WEBAPIを通して受け取ったデータの登録をする
# psycopg2は自動でトランザクションが張られてrallbackも自動でされるがcommitは記載しないとテーブルに反映されない
def register_students(registration_list):
    try:
        with connection.cursor() as cur:
            for row in registration_list:
                sql = f"INSERT INTO Address (name, address, telephone) VALUES ('{row["name"]}', '{row["address"]}', '{row["telephone"]}');"
                cur.execute(sql)
            connection.commit()
    except Exception as e:
        logger.exception("Error occured in /api/register/")
    pass
