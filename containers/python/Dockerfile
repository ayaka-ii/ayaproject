# https://qiita.com/devactken/items/a7deb653023b4974f499
# Dockerhubのイメージのページに書き方の参考例がある
# ここのカスタム内容でイメージを作成する

FROM python:3.12.7-bookworm

# -pは第２階層以上のディレクトリ作成オプション。
# RUNはコマンド実行＝イメージの中に/code/pythonを作成
RUN mkdir -p /code/python

# 外 中（外はCONTEXTから見た相対パスを書く）
# 外の世界を知らないイメージちゃんのために外の世界のrequirements.txtをコピーしてあげる
COPY requirements.txt /code

# COPYによってコピーされたrequirements.txtを参照して中のライブラリをインストールする
# COPYがこの下の行に書いてあったら実行できない
RUN pip install --no-cache-dir -r /code/requirements.txt

# コンテナ起動時に実行されるコマンド（起動するアプリ）をここで登録
ENTRYPOINT [ "flask", "run" ]
# # Pythonの場合
# ENTRYPOINT [ "Python" ]

# # コンテナ起動時に実行されるコマンドをここで登録
# # CMDはENTRYPOINTの引数になる（ターミナルでpython /code/python/hello.pyと指定するのと同じ）
# CMD [ "/code/python/hello.py" ]

