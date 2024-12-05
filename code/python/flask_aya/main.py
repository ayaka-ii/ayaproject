# __init__.pyで作成したflaskオブジェクトを呼び出す
from flask_aya import app
from flask import render_template, request, redirect, url_for
import json

from flask_aya.models import select_students, json_students, register_students, regi


import psycopg2
import os # 環境変数を取得するライブラリ

import logging
logger = logging.getLogger(__name__)

# @オブジェクト名.routeでルーティング。指定した / はトップページのことになるので
# トップページにアクセスしたときにindex関数が実行されて戻り値のindex.htmlが表示される
# methodsの指定をしてない場合GETメソッドになる
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students/')
def students():
    students = select_students()
    logger.info(students)
    return render_template('students.html', students = students)

@app.route('/students/registration/')
def registration():
    return render_template('registration.html')

@app.route('/register/', methods=['POST'])
def register():
    regi(request.form)
    return redirect(url_for('index'))


# WEBAPI用のエンドポイント（URL）   
@app.route('/api/students/')
def students_api():
    return json_students()

# requestモジュールによってrequest.jsonでjsonとして取得ができる
@app.route('/api/register/', methods=['POST'])
def register_api():
    # request.jsonはリスト型（登録されたデータの辞書が要素になっている）
    registration_list = request.json    
    register_students(registration_list)
    return "登録完了しました"
