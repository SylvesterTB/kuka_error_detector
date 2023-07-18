import requests

TOKEN = "6394746388:AAH9cXDsJb3caDc6_3wzuFLFMgnu7t46aH0"
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
print(requests.get(url).json())
error_message = 'something'
import requests
TOKEN = "6394746388:AAH9cXDsJb3caDc6_3wzuFLFMgnu7t46aH0"
chat_id = "5946134823"
message = "error detected"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
# print(requests.get(url).json()) # this sends the message

def telebot(err_msg, out_msg):
    url2 = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={err_msg, out_msg}"
    print(requests.get(url2).json()) 




# chat ID: 5946134823 
# bot ID: 6394746388:AAH9cXDsJb3caDc6_3wzuFLFMgnu7t46aH0