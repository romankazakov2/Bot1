from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from config import TELEGRAM_TOKEN

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

# Callback data
game_cb = CallbackData('game', 'category', 'action')

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton('Стратегии')
button2 = KeyboardButton('Приключения')
button3 = KeyboardButton('Шутеры')
button4 = KeyboardButton('Интелектуальные')
button5 = KeyboardButton('Гонки')
button6 = KeyboardButton('Платформеры')
keyboard.add(button1, button2, button3, button4, button5, button6)

inline_buttons = {
    "Civilization VI": InlineKeyboardButton('Civilization VI',url='https://store.steampowered.com/app/1308090/Sid_Meiers_Civilization_VI_New_Frontier_Pass/'),
    "Total War: Warhammer II": InlineKeyboardButton('Total War: Warhammer II',url='https://store.steampowered.com/app/1209121/Total_War_WARHAMMER_II__Imrik/'),
    "XCOM 2": InlineKeyboardButton('XCOM 2', url='https://store.steampowered.com/app/268500/XCOM_2/'),
    "Stellaris": InlineKeyboardButton('Stellaris', url='https://store.steampowered.com/app/281990/Stellaris/'),
    "The Witcher 3: Wild Hunt": InlineKeyboardButton('The Witcher 3: Wild Hunt', url='https://thebyrut.org/4483-vedmak-3-dikaja-ohota.html'),
    "Tomb Raider (2013)": InlineKeyboardButton('Tomb Raider (2013)', url='https://store.steampowered.com/app/203160/Tomb_Raider/'),
    "Subnautica": InlineKeyboardButton('Subnautica', url='https://store.steampowered.com/app/264710/Subnautica/'),
    "Ori and the Blind Forest": InlineKeyboardButton('Ori and the Blind Forest', url='https://store.steampowered.com/app/466390/Ori_and_the_Blind_Forest_Additional_Soundtrack/'),
    "PlayerUnknown's Battlegrounds (PUBG)": InlineKeyboardButton("PlayerUnknown's Battlegrounds (PUBG)", url='https://store.steampowered.com/app/578080/PUBG_BATTLEGROUNDS/'),
    "DOOM (2016)": InlineKeyboardButton('DOOM (2016)', url='https://moreigr.org/load/ehkshn/2003-doom-2016.html'),
    "Rainbow Six Siege": InlineKeyboardButton("Tom Clancy's Rainbow Six® Siege - Ultra HD Texture Pack", url='https://store.steampowered.com/app/377560/Tom_Clancys_Rainbow_Six_Siege__Ultra_HD_Texture_Pack/'),
    "Borderlands 2": InlineKeyboardButton('Borderlands 2 Season Pass', url='https://store.steampowered.com/app/218560/Borderlands_2_Season_Pass/'),
    "Portal 2": InlineKeyboardButton('Portal 2', url='https://store.steampowered.com/app/620/Portal_2/'),
    "The Witness": InlineKeyboardButton('The Witness', url='https://store.steampowered.com/app/210970/The_Witness/'),
    "Human: Fall Flat": InlineKeyboardButton('Human: Fall Flat', url='https://store.steampowered.com/app/477160/Human_Fall_Flat/'),
    "The Talos Principle": InlineKeyboardButton('The Talos Principle', url='https://store.steampowered.com/app/257510/The_Talos_Principle/'),
    "Dirt Rally 2.0": InlineKeyboardButton('Dirt Rally 2.0', url='https://thelastgame.ru/dirt-rally-2-0/'),
    "Forza Horizon 4": InlineKeyboardButton('Forza Horizon 4', url='https://thelastgame.ru/forza-horizon-4/?ysclid=lwukt0te6227199009'),
    "Gran Turismo Sport": InlineKeyboardButton('Gran Turismo Sport', url='https://steamcommunity.com/sharedfiles/filedetails/?id=2934249693'),
    "Need for Speed: Heat": InlineKeyboardButton('Need for Speed: Heat', url='https://thelastgame.ru/need-for-speed-heat/?ysclid=lwukv3gwqt54553655'),
    "Hollow Knight": InlineKeyboardButton('Hollow Knight', url='https://thelastgame.ru/hollow-knight/?ysclid=lwumduspqj884101525'),
    "Celeste": InlineKeyboardButton('Celeste', url='https://thelastgame.ru/celeste/?ysclid=lwumfpq9bg968370085'),
    "Super Meat Boy": InlineKeyboardButton('Super Meat Boy', url='https://thelastgame.ru/super-meat-boy/?ysclid=lwumhpzjex609151855'),
    "Rayman Legends": InlineKeyboardButton('Rayman Legends', url='https://thelastgame.ru/rayman-legends/?ysclid=lwumim3ubd444462047')
}

# Игры по категориям
categories = {
    'Стратегии': ["Civilization VI", "Total War: Warhammer II", "XCOM 2", "Stellaris"],
    'Приключения': ["The Witcher 3: Wild Hunt", "Tomb Raider (2013)", "Subnautica", "Ori and the Blind Forest"],
    'Шутеры': ["PlayerUnknown's Battlegrounds (PUBG)", "DOOM (2016)", "Rainbow Six Siege", "Borderlands 2"],
    'Интелектуальные': ["Portal 2", "The Witness", "Human: Fall Flat", "The Talos Principle"],
    'Гонки': ["Dirt Rally 2.0", "Forza Horizon 4", "Gran Turismo Sport", "Need for Speed: Heat"],
    'Платформеры':["Hollow Knight", "Celeste", "Super Meat Boy", "Rayman Legends"]
}

# Текущие индексы для каждой категории
current_index = {
    'Стратегии': 0,
    'Приключения': 0,
    'Шутеры': 0,
    'Интелектуальные': 0,
    'Гонки': 0,
    'Платформеры': 0
}

inline_keyboards = {}

for category, games in categories.items():
    for game in games:
        inline_keyboards[game] = InlineKeyboardMarkup().add(inline_buttons[game]).add(
            InlineKeyboardButton('Назад', callback_data=game_cb.new(category=category, action='prev')),
            InlineKeyboardButton('Следующая', callback_data=game_cb.new(category=category, action='next'))
        )

game_photos = {
    "Civilization VI": "https://avatars.mds.yandex.net/i?id=be959062da5d643727984ddd9e77e4ed5f5b3e50-8376360-images-thumbs&n=13",
    "Total War: Warhammer II": "https://avatars.mds.yandex.net/i?id=45090b1db642e41f9dc1aafb2484b053529f74e4-10868764-images-thumbs&n=13",
    "XCOM 2": "https://avatars.mds.yandex.net/i?id=a6acae9386cfe6b7b14846287d378e49e23c3a99-10590187-images-thumbs&n=13",
    "Stellaris": "https://avatars.mds.yandex.net/i?id=429b0244f715f6d407d3e022544569c0f5304a03-10026303-images-thumbs&n=13",
    "The Witcher 3: Wild Hunt": "https://avatars.mds.yandex.net/i?id=baaa9688bd54b5deca1952e784a77b0e8c05af16-9860796-images-thumbs&n=13",
    "Tomb Raider (2013)": "https://avatars.mds.yandex.net/i?id=1fcc5bcf3d3ca239268e5e48762e41be-5210381-images-thumbs&n=13",
    "Subnautica": "https://avatars.mds.yandex.net/i?id=65d46f6497ce170b8a5c5cf33b2c1cf4a1b6abf0-10414552-images-thumbs&n=13",
    "Ori and the Blind Forest": "https://avatars.mds.yandex.net/i?id=967888b889405db8a9e493324428943a7f86e1c0-9098231-images-thumbs&n=13",
    "PlayerUnknown's Battlegrounds (PUBG)": "https://avatars.mds.yandex.net/i?id=925a5a22b73b3549bb24141bbb9ab63136e9fb40-10767243-images-thumbs&n=13",
    "DOOM (2016)": "https://avatars.mds.yandex.net/i?id=388a1453c3b135801b13482d4ffea875d9ab4e8f-9040073-images-thumbs&n=13",
    "Rainbow Six Siege": "https://avatars.mds.yandex.net/i?id=5b38a5132c5be6e37ccde9e555959b59fab0fff5-9271342-images-thumbs&n=13",
    "Borderlands 2": "https://avatars.mds.yandex.net/i?id=3ccc3926ca8de60dea55aa3344518e11c201c6c2-8313048-images-thumbs&n=13",
    "Portal 2": "https://avatars.mds.yandex.net/i?id=50b46485f3c6d4895ea5ad6b276e7bc0-4365757-images-thumbs&n=13",
    "The Witness": "https://avatars.mds.yandex.net/i?id=1abd44d2c1920ee5be99f26639dac562b9d4d7a7-8474952-images-thumbs&n=13",
    "Human: Fall Flat": "https://avatars.mds.yandex.net/i?id=f2649f773cd2aa23e29cdd5534cae056133d447b-7758750-images-thumbs&n=13",
    "The Talos Principle": "https://avatars.mds.yandex.net/i?id=35e169a2b28a21c28010305d7dc898d48fe0d8e1-5231631-images-thumbs&n=13",
    "Dirt Rally 2.0": "https://avatars.mds.yandex.net/i?id=07b7733b95624dd2f333ede8e98bcf981c2066ef-8977890-images-thumbs&n=13",
    "Forza Horizon 4": "https://avatars.mds.yandex.net/i?id=e52859b96c0e640aba023a2bff3e83ef7e9bdeee-12523590-images-thumbs&n=13",
    "Gran Turismo Sport": "https://avatars.mds.yandex.net/i?id=7ff216c3963e92a0cf195b0096535458759f68a9-10640295-images-thumbs&n=13",
    "Need for Speed: Heat": "https://avatars.mds.yandex.net/i?id=665ae92c98943297ef5122e290d198e66aa3d1de-8199312-images-thumbs&n=13",
    "Hollow Knight": "https://avatars.mds.yandex.net/i?id=631a1500b7441e6bc14007343dbdeccedd33ef24-9212030-images-thumbs&n=13",
    "Celeste": "https://avatars.mds.yandex.net/i?id=b6ee4ca12d1dd86d8002cc9e60eed5a1ef2f7cf5-11379499-images-thumbs&n=13",
    "Super Meat Boy": "https://avatars.mds.yandex.net/i?id=4ee68998ccaa1fb5183636c2cda80fca9e74e879-11531625-images-thumbs&n=13",
    "Rayman Legends": "https://avatars.mds.yandex.net/i?id=5627a8b7ca9ba005bcd9f267fe082b2713f1d627-10577947-images-thumbs&n=13"
}

game_descriptions = {
    "Civilization VI": "Эта игра предлагает непревзойденный геймплей, в котором вам нужно умело управлять своей цивилизацией, развивать ее и вести ее к победе в основных аспектах человеческого развития, таких как наука, культура, армия и дипломатия.",
    "Total War: Warhammer II": "Рассчитывайте свои ходы, раскрывайте карту и покоряйте фантастический мир Warhammer, предлагая разнообразные стратегические возможности и классическую пошаговую боевую систему.",
    "XCOM 2": "Альтернативное будущее, в котором вам предстоит возглавить команду солдат, которая сражается против вторжения инопланетной расы. Вам придется принимать сложные стратегические решения, управлять базой и вооружением, а также разрабатывать тактику для выживания.",
    "Stellaris": "В этой космической стратегии вы будете управлять целыми галактиками, исследовать новые планеты, строить колонии, сражаться с другими расами и создавать союзы или войны в вашу пользу.",
    "The Witcher 3: Wild Hunt": "Эпическая фэнтезийная игра, в которой вы играете в роль Геральта из Ривии, охотника на монстров. Исследуйте огромный открытый мир, выполняйте задания и принимайте решения, которые повлияют на ход сюжета.",
    "Tomb Raider (2013)": "Приключенческая игра, где вы воплощаете легендарную Лару Крофт. Решайте головоломки, сражайтесь с врагами и исследуйте опасные локации в поисках тайн и сокровищ.",
    "Subnautica": "Поднимитесь на поверхность экзотической планеты, полностью покрытой водой, и исследуйте ее океанические просторы. Выживайте, стройте базу, исследуйте и создавайте снаряжение в этой захватывающей игре-приключении.",
    "Ori and the Blind Forest": "В этой визуально прекрасной игре вы играете в роли маленького лесного существа Ори, которому предстоит спасти свой лес от разрушения. Погружайтесь в удивительный мир, разгадывайте головоломки и сражайтесь с врагами.",
    "PlayerUnknown's Battlegrounds (PUBG)": "Игра в жанре 'Battle Royale', где вам нужно бороться за выживание на огромной карте, сражаясь с другими игроками. PUBG предлагает интенсивные бои, реалистичную графику и широкий выбор оружия и тактик.",
    "DOOM (2016)": "Ремейк классической игры, DOOM предлагает быстрый и кровавый шутер от первого лица с прекрасной графикой и адреналиновым геймплеем. Вам предстоит сражаться с ордами демонов, используя разнообразное оружие и свою хитрость.",
    "Rainbow Six Siege": "Соревнуйтесь в командных тактических боях, управляя одним из различных оперативников, каждый из которых имеет свои уникальные навыки и специальное снаряжение. Rainbow Six Siege предлагает эффектные сражения и стратегическое мышление.",
    "Borderlands 2": "Смесь шутера от первого лица и RPG, Borderlands 2 предлагает вам увлекательные приключения в ярком постапокалиптическом мире. Сражайтесь с врагами, выполняйте задания, находите лут и играйте в кооперативном режиме с друзьями.",
    "Portal 2": "Головоломки в этой игре, сочетающие в себе физику и логику, представляют собой настоящее испытание для вашего интеллекта. Разгадывайте загадки и сражайтесь с врагами с помощью портальной пушки.",
    "The Witness": "Это мистическая головоломка, которая развертывается на острове, полном интерактивных головоломок. Разгадывайте загадки, исследуйте окружающую среду и раскройте секреты этого загадочного места.",
    "Human: Fall Flat": "Оригинальная головоломка, где вы играете за мягкого и неуклюжего персонажа. Решайте физические загадки, используя уникальную механику игры, чтобы достичь цели.",
    "The Talos Principle": "Это философская головоломка, которая подводит вас к размышлениям о смысле жизни, сознании и технологии. Раскрыйте мир, решая сложные головоломки и исследуя древний храм.",
    "Dirt Rally 2.0": "Пыльные трассы и сложные условия погоды делают эту игру одной из лучших для любителей раллийных гонок.",
    "Forza Horizon 4": "Самая реалистичная гоночная игра, которая позволяет игрокам насладиться красивым открытым миром и разнообразными автомобилями.",
    "Gran Turismo Sport": "Легендарная серия игр Gran Turismo, предлагающая реалистичные авто и трассы для гонок.",
    "Need for Speed: Heat": "Адреналиновая гоночная игра с захватывающими погонями и уличными гонками.",
    "Hollow Knight": "Это метроидвания-платформер, где игрок управляет персонажем на пути через огромный мир подземелий, полный опасностей, загадок и боссов. Отличается прекрасным дизайном уровней, увлекательным геймплеем и мрачной атмосферой.",
    "Celeste": "В этой игре игрок управляет героиней по имени Мадлен, которая отправляется на гору Целест с намерением покорить ее вершину. Геймплей ориентирован на исследование и преодоление сложных платформенных уровней, а также на решение головоломок.",
    "Super Meat Boy": "Это экстремальный платформер, в котором игрок управляет куском мяса по опасным уровням, полным ловушек и препятствий. Игра известна своим высоким уровнем сложности, быстрым геймплеем и чувством юмора.",
    "Rayman Legends": "В этой игре игроку предстоит пройти через разнообразные уровни, бросая вызов различным препятствиям и врагам. Rayman Legends отличается ярким и красочным стилем визуального исполнения, отличным саундтреком и захватывающим игровым процессом."
}

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    your_id = message.from_user.id
    your_name = message.from_user.first_name
    await message.answer(
        f'[{your_name}](tg://user?id={str(your_id)}), Привет, я бот, который будет подсказывать актуальные игры по выбранной категории',
        parse_mode="Markdown", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text in categories.keys())
async def handle_category(message: types.Message):
    category = message.text
    game = categories[category][current_index[category]]
    photo_url = game_photos[game]
    caption = game_descriptions[game]
    keyboard = inline_keyboards[game]
    await message.answer_photo(photo=photo_url, caption=caption, reply_markup=keyboard)

@dp.callback_query_handler(game_cb.filter(action=["next", "prev"]))
async def handle_callback(call: types.CallbackQuery, callback_data: dict):
    category = callback_data['category']
    action = callback_data['action']

    if action == 'next':
        current_index[category] = (current_index[category] + 1) % len(categories[category])
    elif action == 'prev':
        current_index[category] = (current_index[category] - 1) % len(categories[category])

    game = categories[category][current_index[category]]
    photo_url = game_photos[game]
    caption = game_descriptions[game]
    keyboard = inline_keyboards[game]
    await call.message.edit_media(types.InputMediaPhoto(photo_url, caption=caption), reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
