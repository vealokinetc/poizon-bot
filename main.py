import telebot
from telebot import types
# from currency_converter import CurrencyConverter
# import yahoo_fin.stock_info as si
# from datetime import datetime, timedelta
cny_course = 13.9
amount = 0
bot = telebot.TeleBot('5846688097:AAF5LWQLocyMJvuOszqFLiNn5gSAP8ISVzY')
markup = types.ReplyKeyboardMarkup()
markup1 = types.ReplyKeyboardMarkup()
markup2 = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('Обувь/Верхняя одежда')
button2 = types.KeyboardButton('Толстовки/Штаны')
markup1.row(button1, button2)
button3 = types.KeyboardButton('Футболки/Шорты')
button4 = types.KeyboardButton('Носки/Нижнее бельё')
markup1.row(button3, button4)
button5 = types.KeyboardButton('Очки/Аксессуары')
button6 = types.KeyboardButton('Сумки/Рюкзаки')
markup1.row(button5, button6)
button7 = types.KeyboardButton('Назад')
markup1.row(button7)
# source_currency = 'CNY'
# destination_currency = 'RUB'

btn1 = types.KeyboardButton('Расчёт стоимости')
btn2 = types.KeyboardButton('Ответы на все вопросы')
markup.row(btn1, btn2)
btn3 = types.KeyboardButton('Отзывы')
btn4 = types.KeyboardButton('Связаться с оператором')
markup.row(btn3, btn4)
btn5 = types.KeyboardButton('Срок доставки')
btn6 = types.KeyboardButton('Товары в наличии')
markup.row(btn5, btn6)
btn7 = types.KeyboardButton('Акции')
markup.row(btn7)

buttons1 = types.KeyboardButton('Перейти к боту')
markup2.row(buttons1)

def start_markup():
    markup = types.InlineKeyboardMarkup(row_width=True)
    link_keyboard_1 = types.InlineKeyboardButton(text="POIZON | KZN", url="https://t.me/poizon_shop_kzn")
    check_keyboard = types.InlineKeyboardButton(text="Проверить ",callback_data="check")
    markup.add(link_keyboard_1,check_keyboard)
    return markup

@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    first_name = message.chat.first_name
    bot.send_message(chat_id, f"<b>Приветствуем Вас</b>,  {first_name}!🙂\n\nЧтобы пользоваться ботом подпишитесь на каналы !",parse_mode='html', reply_markup=start_markup())
def check(call):
    status = ['creator', 'administrator', 'member']
    for i in status:
        if i == bot.get_chat_member(chat_id="-1001510731325", user_id=call.message.chat.id).status:
            bot.send_message(call.message.chat.id, "Спасибо что подписались на каналы !",parse_mode='html',reply_markup=markup2)
            break
    else:
        bot.send_message(call.message.chat.id,"Подпишитесь на каналы!",reply_markup=start_markup())

@bot.callback_query_handler(func= lambda call: True)
def callback(call):
    if call.data == 'check':
        check(call)

@bot.message_handler(func=lambda message: True)
def start(message):
    bot.send_message(message.chat.id,f'Чтобы начать и получить более подробную информацию, просто выберите одну из кнопок ниже ⬇️',parse_mode = 'html',reply_markup=markup)
    bot.register_next_step_handler(message,on_click)

def on_click(message):
    if message.text == 'Расчёт стоимости':
        bot.send_message(message.chat.id,f'Расчёт стоимости 🧮\n\nВыберите интересующую Вас категорию товара.',parse_mode='html',reply_markup=markup1)
        bot.register_next_step_handler(message, on_click1)
    elif message.text == 'Ответы на все вопросы':
        bot.send_message(message.chat.id, '<b>ОТВЕТЫ НА ВСЕ ВОПРОСЫ</b>\n\n🤔 Все ответы в одном месте!\n\nПриветствую вас в разделе "Ответы на все вопросы" 🙂\n\nЗдесь вы найдете самую полезную и актуальную информацию о покупках с маркетплейса <b>POIZON</b>.\n\nМы собрали наиболее часто задаваемые вопросы наших клиентов и предоставили исчерпывающие ответы на каждый из них. Теперь вы можете легко и быстро получить всю необходимую информацию 🙋🏼‍♂️\n\n✅ Как оформить заказ?\n✅ Как происходит доставка?\n✅ Как оплатить покупки?\n✅ Как вернуть товар?\n✅ Есть ли гарантия на товары?\n\n...и многие другие вопросы, которые могут возникнуть у вас перед покупкой. Вы можете сэкономить время и получить все ответы прямо здесь!\n\nЕсли у вас возникнут еще какие-либо вопросы, не стесняйтесь обращаться к @zakaz_poizon_kzn, выбрав соответствующую кнопку ниже.', parse_mode='html',reply_markup=markup)
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Отзывы':
        bot.send_message(message.chat.id,'📝 Отзывы – ваш голос важен! 🗣\n\nДобро пожаловать в раздел "Отзывы"! Здесь вы найдете отзывы и мнения наших довольных клиентов о покупках на маркетплейсе POIZON.\n\nНаши покупатели делятся своими впечатлениями, и мы гордимся, что среди них есть много положительных отзывов. Ведь ваше мнение имеет огромное значение для нас!\n\n🌟 Радостные отзывы о качестве товаров\n🌟 Впечатления о быстрой и надежной доставке\n🌟 Восторженные комментарии об акциях и скидках\n\nМы всегда стремимся сделать ваш опыт покупок максимально приятным и удобным, и ваш отзыв поможет нам улучшить наш сервис еще больше.\n\nЕсли у вас есть что сказать о наших товарах или обслуживании, не стесняйтесь делиться своими мыслями! Ваш отзыв поможет другим покупателям сделать правильный выбор.\n\nЧтобы связаться с нашим оператором или узнать дополнительную информацию, выберите соответствующую кнопку ниже.\n\nБольшое спасибо за вашу поддержку и доверие к нам! 🛍🤩', parse_mode='html')
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Связаться с оператором':
        bot.send_message(message.chat.id,'СВЯЗАТЬСЯ С ОПЕРАТОРОМ📱\n\nПриветствую Вас в разделе "Связаться с оператором" 🙂\n\n👩🏼‍💻 Наши операторы — профессионалы, готовые ответить на все ваши вопросы:\n\n📢 Узнать подробности о товарах и их характеристиках\n✈️ Уточнить информацию о доставке и сроках\n💳 Получить сведения о способах оплаты\n🛍️ Помочь с выбором подходящего товара\n\nЧтобы связаться с оператором, просто напишите сообщение нашему менеджеру @zakaz_poizon_kzn, и он сразу откликнется на Ваш запрос.', parse_mode='html')
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Срок доставки':
        bot.send_message(message.chat.id,'✈️ Узнайте о сроках доставки! ⏳\n\nДобро пожаловать в раздел "Срок доставки"!\n\n Мы понимаем, что важно знать, когда вы получите свои желанные покупки.\n\n📦 Мы гарантируем оперативную доставку и стремимся сделать процесс максимально удобным для вас. Время доставки зависит от вашего местоположения и выбранного товара,<b> но в среднем 20-30 дней </b>.\n\nПожалуйста, учтите, что сроки могут варьироваться в зависимости от пункта назначения и наличия товара на складе. Мы стараемся держать вас в курсе каждого этапа доставки.\n\n📢 Для получения более точной информации о сроках доставки для вашего конкретного заказа, свяжитесь с нашим оператором, нажав соответствующую кнопку ниже.\n\nМы ценим ваше терпение и доверие к маркетплейсу <b>POIZON</b>. Оставайтесь с нами, и скоро ваши покупки будут у вас! 🛍', parse_mode='html')
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Товары в наличии':
        bot.send_message(message.chat.id,'🛍 Всегда в наличии – ваш выбор готов к покупке!\n\nДобро пожаловать в раздел "Товары в наличии"!\n\n Здесь вы найдете самые популярные и стильные товары, которые уже доступны без доставки.\n\n👗 Широкий выбор одежды и обуви\n👜 Самые модные аксессуары\n🕶 Стильные очки и многое другое\n\nПока товаров в наличии нет.', parse_mode='html')
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Акции':
        bot.send_message(message.chat.id,'<b>АКЦИИ</b>\n\n🎉 Акции — лучшие предложения для вас!\n\n Добро пожаловать в раздел "Акции" 🙂\n\nЗдесь вы найдете самые выгодные предложения по покупкам с маркетплейса <b>POIZON</b>.\n\n🎁 Мы заботимся о наших клиентах и рады предоставить вам уникальные скидки и специальные акции на различные товары.\n\nВас ждут следующие предложения👇🏻\n\n🔥 ДАРЮ ВСЕМ 1000Р\n\nВсе просто - расскажи о моем аккаунте в своей insta-story и получи сертификат на 1000P🛍\n\n Автору самой креативной отметки удвою сумму сертификата ✅\n\n🔥 [Название акции 2]: [Описание акции и условия]\n\n🔥 [Название акции 3]: [Описание акции и условия]\n\n📢 Если у вас возникли вопросы о наших акциях или вы хотите узнать о дополнительных предложениях, наш оператор всегда готов помочь. Просто выберите соответствующую кнопку ниже.', parse_mode='html')
        bot.register_next_step_handler(message, on_click)


def summa_for_shoes_and_clothes(message):
    global amount
    try:
        amount = int(message.text.strip())
    except:
        on_click1(message)
        # bot.register_next_step_handler(message, on_click1)
        return
    if amount > 0:
        exchange_rate = cny_course * amount * 1.15 + 1000
        bot.send_message(message.chat.id,f'Отлично!🙂\n\n Мы посчитали общую стоимость вашего заказа, включая доставку. 🧾📦\n\n💳 Итоговая сумма заказа: {round(exchange_rate)}\n\n📲Для оформления заказа напишите нашему менеджеру @zakaz_poizon_kzn\n\nОн поможет вам с оформлением заказа, ответит на все вопросы и даст дополнительную информацию о продукции. Мы с нетерпением ждем вашего заказа! 🎉')
        bot.register_next_step_handler(message, summa_for_shoes_and_clothes)
    else:
        bot.send_message(message.chat.id, 'Сумма должна быть больше нуля. Введите стоимость заказа:')
        bot.register_next_step_handler(message, summa_for_shoes_and_clothes)

def summa_for_hoodile_and_pants(message):
    global amount
    try:
        amount = int(message.text.strip())
    except:
        on_click1(message)
        # bot.register_next_step_handler(message, on_click1)
        return
    if amount > 0:
        exchange_rate = cny_course * amount * 1.15 + 600
        bot.send_message(message.chat.id,f'Отлично!🙂\n\n Мы посчитали общую стоимость вашего заказа, включая доставку. 🧾📦\n\n💳 Итоговая сумма заказа: {round(exchange_rate)}\n\n📲Для оформления заказа напишите нашему менеджеру @zakaz_poizon_kzn\n\nОн поможет вам с оформлением заказа, ответит на все вопросы и даст дополнительную информацию о продукции. Мы с нетерпением ждем вашего заказа! 🎉')
        bot.register_next_step_handler(message, summa_for_hoodile_and_pants)
    else:
        bot.send_message(message.chat.id, 'Сумма должна быть больше нуля. Введите стоимость заказа:')
        bot.register_next_step_handler(message, summa_for_hoodile_and_pants)

def summa_for_shirts_and_shorts(message):
    global amount
    try:
        amount = int(message.text.strip())
    except:
        on_click1(message)
        # bot.register_next_step_handler(message, on_click1)
        return
    if amount > 0:
        exchange_rate = cny_course * amount * 1.15 + 500
        bot.send_message(message.chat.id,f'Отлично!🙂\n\n Мы посчитали общую стоимость вашего заказа, включая доставку. 🧾📦\n\n💳 Итоговая сумма заказа: {round(exchange_rate)}\n\n📲Для оформления заказа напишите нашему менеджеру @zakaz_poizon_kzn\n\nОн поможет вам с оформлением заказа, ответит на все вопросы и даст дополнительную информацию о продукции. Мы с нетерпением ждем вашего заказа! 🎉')
        bot.register_next_step_handler(message, summa_for_shirts_and_shorts)
    else:
        bot.send_message(message.chat.id, 'Сумма должна быть больше нуля. Введите стоимость заказа:')
        bot.register_next_step_handler(message, summa_for_shirts_and_shorts)

def summa_for_socks_and_underwear(message):
    global amount
    try:
        amount = int(message.text.strip())
    except:
        on_click1(message)
        # bot.register_next_step_handler(message, on_click1)
        return
    if amount > 0:
        exchange_rate = cny_course * amount * 1.15 + 400
        bot.send_message(message.chat.id,f'Отлично!🙂\n\n Мы посчитали общую стоимость вашего заказа, включая доставку. 🧾📦\n\n💳 Итоговая сумма заказа: {round(exchange_rate)}\n\n📲Для оформления заказа напишите нашему менеджеру @zakaz_poizon_kzn\n\nОн поможет вам с оформлением заказа, ответит на все вопросы и даст дополнительную информацию о продукции. Мы с нетерпением ждем вашего заказа! 🎉')
        bot.register_next_step_handler(message, summa_for_socks_and_underwear)
    else:
        bot.send_message(message.chat.id, 'Сумма должна быть больше нуля. Введите стоимость заказа:')
        bot.register_next_step_handler(message, summa_for_socks_and_underwear)

def summa_for_glasses_and_accessories(message):
    global amount
    try:
        amount = int(message.text.strip())
    except:
        on_click1(message)
        # bot.register_next_step_handler(message, on_click1)
        return
    if amount > 0:
        exchange_rate = cny_course * amount * 1.15 + 500
        bot.send_message(message.chat.id,f'Отлично!🙂\n\n Мы посчитали общую стоимость вашего заказа, включая доставку. 🧾📦\n\n💳 Итоговая сумма заказа: {round(exchange_rate)}\n\n📲Для оформления заказа напишите нашему менеджеру @zakaz_poizon_kzn\n\nОн поможет вам с оформлением заказа, ответит на все вопросы и даст дополнительную информацию о продукции. Мы с нетерпением ждем вашего заказа! 🎉')
        bot.register_next_step_handler(message, summa_for_glasses_and_accessories)
    else:
        bot.send_message(message.chat.id, 'Сумма должна быть больше нуля. Введите стоимость заказа:')
        bot.register_next_step_handler(message, summa_for_glasses_and_accessories)

def summa_for_bags(message):
    global amount
    try:
        amount = int(message.text.strip())
    except:
        on_click1(message)
        # bot.register_next_step_handler(message,on_click1)
        return
    if amount > 0:
        exchange_rate = cny_course * amount * 1.15 + 700
        bot.send_message(message.chat.id,f'Отлично!🙂\n\n Мы посчитали общую стоимость вашего заказа, включая доставку. 🧾📦\n\n💳 Итоговая сумма заказа: {round(exchange_rate)}\n\n📲Для оформления заказа напишите нашему менеджеру @zakaz_poizon_kzn\n\nОн поможет вам с оформлением заказа, ответит на все вопросы и даст дополнительную информацию о продукции. Мы с нетерпением ждем вашего заказа! 🎉')
        bot.register_next_step_handler(message, summa_for_bags)
    else:
        bot.send_message(message.chat.id, 'Сумма должна быть больше нуля. Введите стоимость заказа:')
        bot.register_next_step_handler(message, on_click1)

def on_click1(message):
    file = open('./photo_6.jpg', 'rb')
    if message.text == 'Обувь/Верхняя одежда':
        bot.send_photo(message.chat.id,file,'Супер 🙂\n\nТеперь давайте узнаем стоимость выбранного Вами товара 👉🏻\n\nПросто <b>введите его стоимость в юанях</b> с POIZON, и я помогу рассчитать окончательную цену с учётом всех акций и скидок 💴',parse_mode='html',reply_markup=markup1)
        bot.register_next_step_handler(message,summa_for_shoes_and_clothes)
        # bot.register_next_step_handler(message, on_click1)
    elif message.text == 'Толстовки/Штаны':
        bot.send_photo(message.chat.id,file,'Супер 🙂\n\nТеперь давайте узнаем стоимость выбранного Вами товара 👉🏻\n\nПросто <b>введите его стоимость в юанях</b> с POIZON, и я помогу рассчитать окончательную цену с учётом всех акций и скидок 💴',parse_mode='html',reply_markup=markup1)
        bot.register_next_step_handler(message, summa_for_hoodile_and_pants)
        # bot.register_next_step_handler(message, on_click1)
    elif message.text == 'Футболки/Шорты':
        bot.send_photo(message.chat.id,file,'Супер 🙂\n\nТеперь давайте узнаем стоимость выбранного Вами товара 👉🏻\n\nПросто <b>введите его стоимость в юанях</b> с POIZON, и я помогу рассчитать окончательную цену с учётом всех акций и скидок 💴',parse_mode='html',reply_markup=markup1)
        bot.register_next_step_handler(message, summa_for_shirts_and_shorts)
        # bot.register_next_step_handler(message, on_click1)
    elif message.text == 'Носки/Нижнее бельё':
        bot.send_photo(message.chat.id,file,'Супер 🙂\n\nТеперь давайте узнаем стоимость выбранного Вами товара 👉🏻\n\nПросто <b>введите его стоимость в юанях</b> с POIZON, и я помогу рассчитать окончательную цену с учётом всех акций и скидок 💴',parse_mode='html',reply_markup=markup1)
        bot.register_next_step_handler(message, summa_for_socks_and_underwear)
        # bot.register_next_step_handler(message, on_click1)
    elif message.text == 'Очки/Аксессуары':
        bot.send_photo(message.chat.id,file,'Супер 🙂\n\nТеперь давайте узнаем стоимость выбранного Вами товара 👉🏻\n\nПросто <b>введите его стоимость в юанях</b> с POIZON, и я помогу рассчитать окончательную цену с учётом всех акций и скидок 💴',parse_mode='html',reply_markup=markup1)
        bot.register_next_step_handler(message, summa_for_glasses_and_accessories)
        # bot.register_next_step_handler(message, on_click1)
    elif message.text == 'Сумки/Рюкзаки':
        bot.send_photo(message.chat.id,file,'Супер 🙂\n\nТеперь давайте узнаем стоимость выбранного Вами товара 👉🏻\n\nПросто <b>введите его стоимость в юанях</b> с POIZON, и я помогу рассчитать окончательную цену с учётом всех акций и скидок 💴',parse_mode='html',reply_markup=markup1)
        bot.register_next_step_handler(message, summa_for_bags)
        # bot.register_next_step_handler(message, on_click1)
    elif message.text == 'Назад':
        bot.send_message(message.chat.id,'Выбери информацию, которую хочешь узнать.',reply_markup=markup)
        bot.register_next_step_handler(message, on_click)


bot.polling(none_stop=True)
