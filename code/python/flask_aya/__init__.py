# __init__.pyは親ディレクトリ名のモジュール作成

# flask初期設定
from flask import Flask

#flaskアプリオブジェクト。flaskを実行するスクリプトでappをimportする
app = Flask(__name__)

# main.pyをimport
import flask_aya.main

# flask runで実行すると自動で__init__.pyが実行 → main.pyが実行
# dc logs コンテナ名でログ確認するとURLが表示されるが、
# dockerのコンテナ内のPORTになっているので外（ホスト）のPORTに変更したURLにアクセス
