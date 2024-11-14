# https://qiita.com/devactken/items/a7deb653023b4974f499
# Dockerhubのイメージのページに書き方の参考例がある
# ここのカスタム内容でイメージを作成する

FROM python:3.12.7-bookworm

RUN mkdir -p /code/python
# -pは第２階層以上のディレクトリ作成オプション。
# RUNはコマンド実行＝イメージの中に/code/pythonを作成
COPY requirements.txt /code
# 外 中（外はCONTEXTから見た相対パスを書く）
# 外の世界を知らないイメージちゃんのために外の世界のrequirements.txtをコピーしてあげる
RUN pip install --no-cache-dir -r /code/requirements.txt
# COPYによってコピーされたrequirements.txtを参照して中のライブラリをインストールする
# COPYがこの下の行に書いてあったら実行できない

ENTRYPOINT [ "python" ]
# コンテナ起動時に実行されるコマンドをここで登録
CMD [ "/code/python/hello.py" ]
# コンテナ起動時に実行されるコマンドをここで登録
# CMDはENTRYPOINTの引数になる（ターミナルでpython /code/python/hello.pyと指定するのと同じ）