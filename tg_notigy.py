import requests

bot_token = ''
chat_id = ''


def send_tg_found(name: str):
    send_tg_notification(f"Code is found in {name}!")


def send_tg_start(name: str):
    send_tg_notification(f"Brute for {name} is started!")


def send_tg_notification(message: str):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + message

    response = requests.get(send_text)

    return response.json()
