import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Путь к JSON-ключу, который вы скачали
json_keyfile = 'json.json'

# Устанавливаем область видимости и аутентифицируемся
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile, scope)
gc = gspread.authorize(credentials)

def get_comment():
    # Открываем таблицу по её названию
    worksheet = gc.open('ОС Админа').sheet1

    data = worksheet.get_all_values()
    # print(data)
    return data




# headers = data[0]
# record = data[1]

# for header, value in zip(headers[2:-1], record[2:-1]):
#     print(header, value)
# pairs = [(header, value) for header, value in zip(headers[2:-1], record[2:-1])








