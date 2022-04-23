import requests
import telebot
import time




bot = telebot.TeleBot('YOUR TOKEN')

@bot.message_handler()
def get_by_IP(message):
    bot.send_message(message.chat.id, f'Привет,<b>{message.from_user.first_name}</b>', parse_mode='html')
    bot.send_message(message.chat.id, 'Уже ищю информацию...', parse_mode='html')
    time.sleep(1.5)
    if message.text.count('.') == 3:
        response = requests.get(url=f'http://ip-api.com/json/{message.text}').json()
        names_data = {
            'IP': response.get('query'),
            'Org': response.get('org'),
            'Int prov': response.get('isp'),
            'Region Name': response.get('regionName'),
            'Country': response.get('country'),
            'City': response.get('city'),
            'ZIP': response.get('zip'),
            'latitude': response.get('lat'),
            'longitude': response.get('lon'),
        }
        info = ''
        for k, v in names_data.items():
            info += '\n' + (f'{k} : {v}')

        bot.send_message(message.chat.id,  info, parse_mode='html')
        bot.send_location(message.chat.id, response.get('lat'),response.get('lon'))

    else:
        bot.send_message(message.chat.id, "Информация не найдена,пожалуйста проверьте IP адрес.")



if __name__ == '__main__':
    bot.polling(none_stop=True)

