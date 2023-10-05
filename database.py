import json
import sqlite3
import googlesheets as google

connection = sqlite3.connect('data.db')
sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS admin_info (id INTEGER, save_text TEXT);')


def save_comment():
    connection = sqlite3.connect('data.db')
    sql = connection.cursor()
    data = google.get_comment()[-1]
    data_list = json.dumps(data)
    sql.execute('INSERT INTO admin_info (save_text) VALUES (?);', (data_list,))
    connection.commit()
    connection.close()


def check_comment():
    pass

save_comment()