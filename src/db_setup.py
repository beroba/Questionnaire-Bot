# DBセットアップ用

import sqlite3
import settings

DB_NAME = settings.DB_NAME

# DBが存在していなければ作成
conn = sqlite3.connect(DB_NAME)

#カーソルオブジェクト生成
cur = conn.cursor()

# DBの中にscheduleテーブルが存在していない場合作成
cur.execute("SELECT * FROM sqlite_master WHERE type='table' and name='task_schedule'")
if not cur.fetchone():
    cur.execute('CREATE TABLE task_schedule  (id INTEGER PRIMARY KEY AUTOINCREMENT, time STRING, message_id STRING, channel_id STRING)')
else:
    while True:
        choice = input("テーブルが存在しています。再作成しますか？ [Y/N]: ").lower()
        if choice in ['y', 'ye', 'yes']:
            cur.execute("DROP TABLE task_schedule")
            cur.execute('CREATE TABLE task_schedule  (id INTEGER PRIMARY KEY AUTOINCREMENT, time STRING, message_id STRING, channel_id STRING)')
            print("再作成しました。")
            conn.close()
            exit()
        elif choice in ['n', 'no']:
            print("終了します。")
            conn.close()
            exit()

