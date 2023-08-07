import telebot
from telebot import types
import requests
import json
from translate import Translator
bot = telebot.TeleBot("5375421876:AAGWFbrUgBHoopNrOlkKhuUgKn7pRW4v3yE", parse_mode=None)
weather_API = 'ff2761a5d2230bdc851102a7a6af1cbf'


@bot.message_handler(commands=['start'])
def start_bot(message):
    markup = types.ReplyKeyboardMarkup()
    buttom1 = types.KeyboardButton('Погода')
    markup.row(buttom1)
    bot.send_message(message.chat.id, f"Здравствуйте, {message.from_user.first_name}"
                                      f" Спасибо, что пользуетесь нашим телеграмм-ботом", reply_markup=markup)
    bot.register_next_step_handler(message, click_weater)


@bot.message_handler()
def click_weater(message):
    if message.text.lower() != 'погода':
        get_weather(message)
    else:
        bot.reply_to(message, 'Введите город, чтобы узнать погоду в нем:')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    """Получает данный о погоде на данный момент по названию города,обрабатывает их и отправляет пользователю. Если же город введен
    некорректно, сообщает об этом пользователю и просит вести корректно"""
    name_city = message.text.lower().capitalize()
    translator = Translator(to_lang="Russian")
    res = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={name_city}&appid={weather_API}&units=metric')
    if res.status_code == 200:
        weather_dct = json.loads(res.text)
        status_dct = {'Clouds': 'Облачно', 'Clear': 'Ясно', 'Haze': 'Легкий туман', 'Smoke': 'Туман'}
        if weather_dct['weather'][0]['main'] in status_dct.keys():
            bot.reply_to(message,
                         f"Погода в городе {translator.translate(weather_dct['name']).capitalize()} на данный момент:\n"
                         f"{weather_dct['weather'][0]['main'].capitalize()} - {status_dct[weather_dct['weather'][0]['main']]}\n"
                         f"Температура: {round(weather_dct['main']['temp'], 1)}С°\n"
                         f"Ощущается на: {round(weather_dct['main']['feels_like'], 1)}С°\n"
                         f"Влажность: {weather_dct['main']['humidity']}\n"
                         f"Скорость ветра: {round(weather_dct['wind']['speed'], 1)}"
                         f" - {wind_power(round(weather_dct['wind']['speed'], 1))}\n")
        else:
            bot.reply_to(message,
                         f"Погода в городе {translator.translate(weather_dct['name']).capitalize()} на данный момент:\n"
                         f"{weather_dct['weather'][0]['main'].capitalize()}"
                         f" - {translator.translate(weather_dct['weather'][0]['main'].lower()).capitalize()}\n"
                         f"Температура: {round(weather_dct['main']['temp'], 1)}С°\n"
                         f"Ощущается на: {round(weather_dct['main']['feels_like'], 1)}С°\n"
                         f"Влажность: {weather_dct['main']['humidity']}\n"
                         f"Скорость ветра: {round(weather_dct['wind']['speed'], 1)}"
                         f" - {wind_power(round(weather_dct['wind']['speed'], 1))}\n")
    elif message.text.lower() == 'start' or message.text.lower() == '/start':
        start_bot(message)

    else:
        bot.reply_to(message, f'{message.from_user.first_name}, введите город корректно)')
        bot.send_message(message.chat.id, 'Попробуйте еще раз')

def wind_power(x):
    if x < 6:
        return 'Слабый'
    elif x < 11:
        return 'Умеренный'
    elif x < 17:
        return 'Сильный'
    elif x < 22:
        return 'Очень сильный'
    elif x > 22:
        return 'Шторм/Ураган(Оставайтесь дома)'


def main():
    bot.infinity_polling()
if __name__ == '__main__':
    main()