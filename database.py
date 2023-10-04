import sqlite3

connection = sqlite3.connect('data.db')
sql = connection.cursor()

sql.connection('CREATE TABLE IF NOT EXISTS admin_info (upload_time, user_mail, user_name, user_course, lesson_time, info_admin)')