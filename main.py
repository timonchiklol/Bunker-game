import random
import telebot
from dotenv import load_dotenv
import os

# Загружаем переменные окружения из .env файла
load_dotenv()

# Получаем токен из переменных окружения
token = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(token)

def profession_generator():
    professions = [
        "Инженер",
        "Врач",
        "Солдат",
        "Психолог", 
        "Программист",
        "Астроном",
        "Повар",
        "Археолог",
        "Биолог",
        "Строитель",
        "Электрик",
        "Взломщик",
        "Писатель",
        "Гидролог",
        "Лётчик",
        "Охранник",
        "Художник",
        "Детектив",
        "Спасатель",
        "Ведущий ТВ",
        "Дизайнер игр",
        "Оружейник",
        "Фермер",
        "Криминалист",
        "Радиотехник",
        "Бармен",
        "Клоун"
    ]
    return random.choice(professions)

def age_generator():
    return random.randint(9, 70)

def gender_generator():
    return random.choice(["Мужчина", "Женщина"])

def apple():
    return random.choice(["Плодн(ая/ый)", "Бесплодн(ая/ый)"])

def sickness_generator():
    return random.choice([
    "Грипп",
    "ОРВИ",
    "Ангина",
    "Бронхит",
    "Пневмония",
    "Тонзиллит",
    "Отит",
    "Гастрит",
    "Язва желудка",
    "Колит",
    "Геморрой",
    "Аппендицит",
    "Гипертония",
    "Ишемическая болезнь сердца",
    "Аритмия",
    "Инсульт",
    "Инфаркт миокарда",
    "Остеохондроз",
    "Артрит",
    "Остеопороз",
    "Подагра",
    "Сахарный диабет 1 типа",
    "РАК",
    "Аутизм",
    "Гепатит C",
    "Цирроз печени",
    "Почечная недостаточность",
    "Мигрень",
    "Анемия",
    "Псориаз",
    "Идеально здоров", 
    "Идеально здоров", 
    "Идеально здоров", 
    "Идеально здоров", 
    "Идеально здоров"
])
def sickness_generator_procent():
    return random.randint(0, 100)

def phobia_generator():
    return random.choice([
    "Боязнь замкнутых пространств",
    "Боязнь темноты",
    "Боязнь воды",
    "Боязнь высоты",
    "Боязнь громких звуков",
    "Боязнь толпы",
    "Боязнь женщин",
    "Боязнь мужчин", 
    "Боязнь собак",
    "Боязнь кошек",
    "Нет фобий",
    "Нет фобий",
    "Нет фобий",
    "Нет фобий"
    ])

def hobby_generator():
    return random.choice([
    # Полезные хобби
    "Рыбалка",
    "Охота",
    "Выращивание растений (садоводство, гидропоника)",
    "Кулинария и приготовление еды на костре",
    "Фермерство и разведение животных",
    "Оказание первой медицинской помощи",
    "Травничество (знание лечебных растений)",
    "Ремонт и починка техники",
    "Столярное дело",
    "Кузнечное дело",
    "Рукоделие и шитьё",
    "Изготовление оружия и ловушек",
    "Стрельба (лук, арбалет, огнестрельное оружие)",
    "Боевые искусства и самооборона",
    "Химия (изготовление полезных веществ, фильтрация воды)",
    "Физическая подготовка (бег, кроссфит, турники)",
    "Электроника и пайка",
    "Сбор и очистка воды",
    "Ориентирование на местности (чтение карт, компас)",
    "Строительство и ремонт зданий",
    "Психология (управление стрессом, работа в коллективе)",
    "Шахтёрское дело и добыча ресурсов",
    "Программирование и работа с автоматизированными системами",
    "Живопись и рисование (для морального духа)",
    "Игры и карточные фокусы (развлечение для группы)",

    # Бесполезные хобби
    "Коллекционирование марок",
    "Составление гороскопов",
    "Скоростной сбор кубика Рубика",
    "Просмотр сериалов",
    "Разгадывание кроссвордов",
    "Стендап-комедия",
    "Косплей",
    "Скоростной поедатель еды",
    "Ведение блога о моде",
    "Игры на телефон",
    "Плетение браслетов из бисера",
    "Танцы K-Pop",
    "Сочинение стихов о любви",
    "Разведение редких пород кошек",
    "Выставочные соревнования по собакам"
])

def item_generator():
    return random.choice([
    # Полезный багаж
    "Аптечка первой помощи",
    "Набор инструментов (молоток, отвертки, плоскогубцы)",
    "Многофункциональный нож",
    "Спальный мешок и одеяло",
    "Запас консервированной еды",
    "Фильтр для воды или таблетки для очистки",
    "Фонарь и запас батареек",
    "Зажигалки и огниво",
    "Рация или спутниковый телефон",
    "Верёвка (паракорд)",
    "Тёплая одежда и обувь",
    "Канистра с чистой водой",
    "Геологический компас и карта местности",
    "Учебник по медицине и выживанию",
    "Энергетические батончики и сухпайки",
    "Защитные очки и перчатки",
    "Генератор или солнечная батарея",
    "Противогаз или респиратор",
    "Радио с ручным динамо-зарядом",
    "Гигиенические средства (мыло, зубная паста, туалетная бумага)",
    "Набор для шитья и ремонта одежды",
    "Запасной комплект аккумуляторов",
    "Оружие для самообороны (если разрешено)",
    "Запас соли, сахара и специй",
    "Небольшая печка или примус",

    # Бесполезный багаж
    "Коллекция виниловых пластинок",
    "Глянцевые журналы",
    "Фигурки из комиксов",
    "Свадебное платье",
    "Селфи-палка",
    "Диск с установкой Windows XP",
    "Настольная лампа без электричества",
    "Плюшевые игрушки",
    "Книга о моде 2010 года",
    "Топовый геймерский ПК без источника питания",
    "Старая кассета с музыкой 90-х",
    "Настольная игра без фишек и кубиков",
    "Диплом о высшем образовании",
    "Плакат любимой музыкальной группы",
    "Шампунь для окрашенных волос",
    "Флакон дорогих духов",
    "Годовой запас косметики",
    "Альбом с фотографиями из отпуска",
    "Набор кисточек для макияжа",
    "Чековая книжка и кредитная карта"

    ])

def card_generator():
    return random.choice([
    "Отменить последнее действие",
    "2 голоса в этом раунде",
    "Взлом информации – Посмотрите любую характеристику другого игрока",
    "Обмен ролями – Поменяйтесь с любым игроком характеристиками",
    "Дуэль – Аргументативный поединок с игроком, победителя выбирают другие",
    "Второе дыхание – Вернуть выбывшего игрока на 1 раунд",
    "Запрет на голосование – Лишить игрока права голосовать в этом раунде",
    "Запрет на разговор – Лишить игрока права говорить в этом раунде",
    "Хаос – Все игроки получают новые профессии",
    "Анархия – Голосуют только номинированные на вылет",
    "Запасной выход – Пропустить одно голосование",
    "Абсурд – Если вылетит игрок справа от вас, в следующем раунде можно говорить только слова на букву 'П'"
    ])

@bot.message_handler(commands=['start'])
def start_message(message):
    # Формируем сообщение со всеми характеристиками
    profession = f"Профессия: {profession_generator()}"
    age = f"Возраст: {age_generator()}"
    gender = f"Пол: {gender_generator()}, {apple()}"
    sickness = f"Болезнь: {sickness_generator()}, {sickness_generator_procent()}%"
    phobia = f"Фобия: {phobia_generator()}"
    hobby = f"Хобби: {hobby_generator()}"
    item = f"Багаж: {item_generator()}"
    card = f"Карта: {card_generator()}"
    

    # Отправляем каждую характеристику с новой строки
    bot.send_message(message.chat.id, f"{profession}\n{age}\n{gender}\n{sickness}\n{phobia}\n{hobby}\n{item}\n{card}")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text != '/start':
        try:
            with open('leo.jpg', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Изображение не найдено")

# Запускаем цикл опроса сообщений
bot.polling()
