import logging
import requests
import time
from aiogram import Bot, Dispatcher, executor, types


'''The bot shows data by ip address,
 executes a request for your location and shows longitude and latitude'''


API_TOKEN = '5353951371:AAHUAYz4NdUQv-8tHGLRHrZRKgeD_N6TXGs'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def get_button():    # create of button
    keyboard = types.ReplyKeyboardMarkup()
    button = types.KeyboardButton("My Location", request_location=True)
    keyboard.add(button)
    return keyboard


@dp.message_handler(content_types=['location'])
async def send_lat_lon(message: types.Message):   # message about latitude and longitude
    lat = message.location.latitude
    lon = message.location.longitude
    reply = "latitude:  {}\nlongitude: {}".format(lat, lon)
    await message.answer(reply, reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands=['find_me'])
async def find_me(message: types.Message):  # message for click button
    reply = "click on the button to find out your location"
    await message.answer(reply, reply_markup=get_button())


@dp.message_handler()
async def info_by_ip(message: types.Message):   # outputs information by ip
    await message.answer(f'Привет,<b>{message.from_user.first_name}</b>', parse_mode='html')
    await message.answer('Уже ищю информацию...', parse_mode='html')
    time.sleep(1.5)
    if len(message.text) <= 15 and message.text.count('.') == 3:   # standart number of symbols IP <= 15
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
            info += '\n' + f'{k} : {v}'

        await message.answer(info, parse_mode='html')

    else:
        await message.answer("Информация не найдена,пожалуйста проверьте IP адрес.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
