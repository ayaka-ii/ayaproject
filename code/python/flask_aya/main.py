# __init__.pyで作成したflaskオブジェクトを呼び出す
from flask_aya import app
from flask import render_template

# @オブジェクト名.routeで指定した / はトップページのことになるので
# トップページにアクセスしたときにindex関数が実行されて
# 戻り値のindex.htmlが表示される
@app.route('/')
def index():
    return render_template('index.html')

