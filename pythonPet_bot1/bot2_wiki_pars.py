import os
from aiogram import Bot, types, executor, Dispatcher
from wikipedia import *
from icrawler.builtin import GoogleImageCrawler
from aiogram.dispatcher.filters import Text

bot = Bot('6179435711:AAGWbN7IO-A-cwjbqtL6CYRr_f064B_FvbU')
dp = Dispatcher(bot)
name = None


@dp.message_handler(commands=['start', 'info'])
async def start(message: types.Message):
    if message.text == '/start':
        await message.answer(f"Здравствуйте, {message.from_user.first_name}\n"
                             f"Спасибо, что пользуетесь нашим телеграмм-ботом")
        await message.answer('Введите название или имя объекта')
    elif message.text == '/info':
        await message.answer('Введите название или имя объекта')


@dp.message_handler(content_types=['text'])
async def get_name(message: types.Message):
    """Принимает название и вызывает функции в зависимости от нажатия конпки"""
    global name
    if message.text != 'Только фото' and message.text != 'Информация без фото' and message.text != 'Информация и фото':
        name = message.text.title()
        buttons = ['Только фото', 'Информация без фото', 'Информация и фото']
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*buttons)
        await message.answer('Выберите категорию', reply_markup=markup)
    elif message.text == 'Только фото':
        await send_photo(message)
    elif message.text == 'Информация без фото':
        await send_summary(message)
    elif message.text == 'Информация и фото':
        await send_photo_and_summary(message)


@dp.message_handler(Text(equals='Только фото'))
async def send_photo(message: types.Message):
    global name
    await message.answer('Пожалуйста, подождите...')
    pars_picture(name)
    photo = types.InputFile('picture/000001.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Готово')
    await message.answer(f'Если статья или картинка не соответсвуют правде, то проверьте корректонсть ввода.\n'
                         f'Зачастую дело в этом')
    os.remove(path='picture/000001.jpg')


@dp.message_handler(Text(equals='Информация без фото'))
async def send_summary(message: types.Message):
    global name
    await message.answer('Пожалуйста, подождите...')
    try:
        summary = pars_summary(name)
        await message.answer(summary)
        await message.answer('Готово')
    except:
        await message.answer('Пожалуйста, водите имя корректо')


@dp.message_handler(Text(equals='Информация и фото'))
async def send_photo_and_summary(message: types.Message):
    global name
    await message.answer('Пожалуйста, подождите...')
    try:
        pars_picture(name)
        photo = types.InputFile('picture/000001.jpg')
        summary = pars_summary(name)
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
        await message.answer(summary)
        await message.answer('Готово')
        os.remove(path='picture/000001.jpg')
    except:
        await message.answer('Пожалуйста, водите имя корректо')


def pars_summary(name_something):
    set_lang('ru')
    pag = page(name_something)
    return pag.summary


def pars_picture(name_something, cnt_pictures=1):
    google_craw = GoogleImageCrawler(storage={'root_dir': 'C:/Users/slava/PycharmProjects/pythonPet_bot1/picture'})
    google_craw.crawl(keyword=name_something, max_num=cnt_pictures)


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
