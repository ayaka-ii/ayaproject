-- IF NOT EXISTSで同じテーブル名が存在する場合にエラーにせず注意のみする（注意はDBサーバーに入らないと表示されない？）
-- IF NOT EXISTSしない場合はtryでエラー発生時の処理を記載しないとエラーで処理が中断される

-- 氏名、住所
CREATE TABLE IF NOT EXISTS Address (
    id SERIAL PRIMARY KEY, -- SERIALは値を指定しなくてもINSERTしたときに自動で番号が振られる、自動増分整数
    name VARCHAR(30) NOT NULL, -- VARCHARで文字列指定、30文字まで
    address VARCHAR(100) NOT NULL
);
-- Addressテーブルへtelephoneカラム追加
ALTER TABLE Address ADD COLUMN IF NOT EXISTS telephone VARCHAR(13);

-- サークル一覧
CREATE TABLE IF NOT EXISTS Circle(
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL
);