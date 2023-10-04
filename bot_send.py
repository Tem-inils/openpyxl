import telebot
import time
import googlesheets

bot = telebot.TeleBot('6567697373:AAFYnPXktIQRVOWppXOzGfGbMY_65TI57FM')

chat_id = '302137006'
response = googlesheets.get_comment()
headers = response[0]
record = response[1]

previous_message = None

def send_data_to_telegram():
    global previous_message

    message = ""
    for header, value in zip(headers[2:-1], record[2:-1]):
        message += f"{header} {value}\n"
    message = message.replace("::", ":").replace(": :", ":").strip()

    if message != previous_message:
        bot.send_message(chat_id, message)
        previous_message = message

while True:
    send_data_to_telegram()
    time.sleep(5)








