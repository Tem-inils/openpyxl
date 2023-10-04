import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Путь к JSON-ключу, который вы скачали
json_keyfile = 'json.json'

# Устанавливаем область видимости и аутентифицируемся
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile, scope)
gc = gspread.authorize(credentials)

# Открываем таблицу по её названию
worksheet = gc.open('SheetsTest').sheet1

data = worksheet.get_all_values()
print(data[-1])
