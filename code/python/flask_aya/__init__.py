# __init__.pyは親ディレクトリ名のモジュール作成

# flask初期設定
from flask import Flask

# flaskアプリオブジェクト。flaskを実行するスクリプトでappをimportする
# static_folderに指定したパスはそのままブラウザなどから表示できる＝画像などを置く場所
app = Flask(__name__, static_folder='public')

# main.pyをimport
import flask_aya.main

# flask runで実行すると自動で__init__.pyが実行 → main.pyが実行
# dc logs コンテナ名でログ確認するとURLが表示されるが、
# dockerのコンテナ内のPORTになっているので外（ホスト）のPORTに変更したURLにアクセス

from logging import getLogger, handlers, Formatter, DEBUG
# 全体のログ設定
# ファイルに書き出す。ログが100KB溜まったらバックアップにして新しいファイルを作る。
root_logger = getLogger()
root_logger.setLevel(DEBUG)
rotating_handler = handlers.RotatingFileHandler(
    r'./flask_aya/log/app.log',
    mode="a",
    maxBytes=100 * 1024,
    backupCount=3,
    encoding="utf-8"
)
format = Formatter('%(asctime)s : %(levelname)s : %(filename)s - %(message)s')
rotating_handler.setFormatter(format)
root_logger.addHandler(rotating_handler)
