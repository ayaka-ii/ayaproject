# __init__.pyで作成したflaskオブジェクトを呼び出す
from flask_aya import app
from flask import render_template
import json

import psycopg2
import os # 環境変数を取得するライブラリ

import logging
logger = logging.getLogger(__name__)

# @オブジェクト名.routeで指定した / はトップページのことになるので
# トップページにアクセスしたときにindex関数が実行されて
# 戻り値のindex.htmlが表示される
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

# WEBAPI用のエンドポイント（URL）
@app.route('/api/circles')
def circles():
    try:
        connection = psycopg2.connect(
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        with connection.cursor() as cur:
            sql = '''
                SELECT *
                FROM Address;
                '''
            cur.execute(sql)  
            results = cur.fetchall()
            logger.info("dddddddddddddddddddddddddddd")
        dict_result = []
        for row in results:
            dict_result.append(list(row))
        
        # ensure_ascii=Falseを引数に設定すると日本語をただしく表示できる        
        circle_data_json = json.dumps(dict_result, ensure_ascii=False)
        return circle_data_json
    except Exception as e:
        # データベース接続に関するエラーハンドリング
        logger.exception("Error occured in /api/circles")
        pass
    # finallyで正常に処理されてreturnした場合でもデータベースを閉じてくれる
    finally:
        if connection in locals():
            connection.close()
        
