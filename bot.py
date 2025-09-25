import telebot
import random
from telebot import types

TOKEN = "7827604200:AAHkU80SAMXkBoKMj2sZJ0YPuA8T9uJmVZs"
bot = telebot.TeleBot(TOKEN)


# ===== Данные об участниках (MineShield IV) =====
def _norm(s: str) -> str:
    return "".join(s.lower().split()) if isinstance(s, str) else ""

INFO = {
    # Источник: https://mineshield.fandom.com/ru/wiki/MineShield_IV (упоминания в хронологии)
    "Alcest M": [
        "Находил загадочные записки",
        "Вёл наблюдения на радиотелескопе",
        "Замечал метеорные потоки и их влияние на радио",
        "Его радиотелескоп фиксировал сообщения о кометах",
        "Получал ‘записку’ среди первых",
    ],
    "Alfedov": [
        "Участвовал в исследовании войда",
        "Замечал пролёт белых комет",
        "Участвовал в экспедиции по карте порталов",
    ],
    "Arlabus": [
        "Инициировал ЧСВЖД — Железнодорожников",
        "Занимался инфраструктурой острова",
    ],
    "BarsiGold": [
        "Обнаружил перенос портала в Незере в войд",
        "Нашёл карту, благодаря которой попали в Энд",
        "Участвовал в исследовании ‘войд’ измерения",
    ],
    "Bez LS": [
        "Получил одну из загадочных записок (вместе с Пугодом)",
        "Находил записки с бинарным кодом",
    ],
    "CapXenomorph": [
        "Нашёл карту с новыми порталами второго круга",
        "Участвовал в картографировании порталов",
    ],
    "DEB": [
        "Участвовал в озеленении грибного острова",
        "Помогал с экологическими проектами ГНДР",
    ],
    "Diamkey": [
        "Первым заметил смертельную зону вокруг острова",
        "Нашёл несколько записок",
        "Запускал спутник ‘Вояджер’",
        "Фиксировал появление комет и предупреждения со спутника",
    ],
    "Dushenka": [
        "Создал киоск СОДА — оценка действий и адекватности",
        "Запускал авторские инициативы на спавне",
    ],
    "Faradey": [
        "Участник IV сезона и событий вокруг зоны",
        "Участвовал в общих вылазках и наблюдениях",
    ],
    "Gel mo": [
        "Объявил себя императором Верстании",
        "Принимал участие в политике Верстании",
    ],
    "Hayd1": [
        "Входил в СЭКС — контроль и развитие спавна",
        "Помогал с улучшениями спавна",
    ],
    "HeO": [
        "Участник ГНДР; замечал феномен ‘красных глаз’ у других",
        "Входил в проекты ГНДР на острове",
    ],
    "Jay Pokerman": [
        "Участник IV сезона; фигурирует в хронике событий",
        "Участвовал в совместных поисках порталов",
    ],
    "Just S": [
        "Нашёл порталы в Энд с недостающими рамками",
        "Экспериментировал с армор-стендами",
        "Фиксировал странности порталов Энда",
    ],
    "KetrinCyst": [
        "Объявила образование Верстании",
        "Занималась дипломатией и управлением",
    ],
    "KlashRaick": [
        "Участвовал в вылазках в войд и за границу зоны",
        "Попал под эффект ‘смерти по неизвестной причине’ на границе",
    ],
    "KrolikMun": [
        "Ломал рамки порталов Энда, проверяя теорию Неркина",
        "Экспериментировал с механикой открытых порталов",
    ],
    "LordSantos": [
        "Был в составе Дровосеков, активный участник экспедиций",
        "Исследовал войд вместе с группой",
    ],
    "Mo1vine": [
        "Вступал в ГНДР как тайный агент Верстании",
        "Участвовал в дипломатических операциях",
    ],
    "MoDDyChat": [
        "Подобрал координаты из записки и нашёл очередную",
        "Построил пушку для телепорта через зону в Энд",
        "Помогал расшифровывать шифры на записках",
    ],
    "Nerkin": [
        "Продвигал теорию о ‘доброте’ острова и порталов",
        "Его теория повлияла на поведение с порталами",
    ],
    "NikiWright": [
        "Замечала феномен множества ‘красных глаз’",
        "Работала со штабом СЭКС на спавне",
    ],
    "ObsidianTime69": [
        "Его база оказалась рядом с местом падения метеорита",
        "Вступал в Верстанию в ходе сезона",
    ],
    "PWGood": [
        "Объявил грибной остров суверенной территорией (ГНДР)",
        "Назначал и принимал дипломатов Верстании",
        "Организовывал установку мицелия на выжженной территории",
    ],
    "Sanhez": [
        "Находил способ обходить эффекты зоны короткими заходами в Незер",
        "Был исключён из Верстании",
        "Совместно с Пугодом — дипломатическое взаимодействие ГНДР/Верстании",
    ],
    "SecB": [
        "Создал сеть спутников; запускал и обновлял их прошивки",
        "Строил и запускал магниты на острове",
        "Спутники получали функционал радара и сообщения о метеорите",
    ],
    "SirPiligrim": [
        "Нашёл лаборатории и справочники; видел ‘красные глаза’",
        "Исследовал найденные справочники ‘Заметки’ и ‘Справочники’",
    ],
    "SnrGiraffe": [
        "Получал одну из нумерованных записок",
        "Участвовал в озеленении грибного острова",
    ],
    "TheKlyde": [
        "Замечал феномен ‘красных глаз’",
        "Сообщал о странном поведении питомцев",
    ],
    "Venazar": [
        "Вступал в Верстанию; эльфийскому королевству дали автономию",
        "Связан с автономным статусом Эльфийского королевства",
    ],
    "Zakviel": [
        "Наблюдал пролёт белых комет и другие явления",
        "Фиксировал небесные объекты в хронике",
    ],
}

# Строковые краткие описания участников (IV сезон)
DESCR = {
    "Alcest M": "бывший Дровосек; исследователь. Находил записки, ведёт радиотелескоп, замечал метеорные события",
    "Alfedov": "бывший Дровосек; исследователь, участвовал в вылазках в войд и наблюдениях",
    "Arlabus": "Организатор ЧСВЖД (Железнодорожники); инфраструктура сервера",
    "BarsiGold": "Исследователь войда и порталов; помог попасть в Энд",
    "Bez LS": "Игрок ГНДР; участвовал в событиях с записками и миграции",
    "CapXenomorph": "Исследователь; находил карты порталов второго круга",
    "DEB": "Участник Верстании/союзник; участвовал в озеленении грибного острова",
    "Diamkey": "Исследователь тайн; находил записки, владелец спутника ‘Вояджер’",
    "Dushenka": "Создатель киоска СОДА — служба оценки действий и адекватности",
    "Faradey": "участник Верстании; нету четкого канона",
    "Gel mo": "Верстания; позднее объявил себя императором Верстании",
    "Hayd1": "Участник СЭКС — Самостоятельные Эксперты Контроля Спавна",
    "HeO": "архангел; участник ГНДР и СОВТ",
    "Jay Pokerman": "учасник Нью-Джесико; разрушитель порталов в энд",
    "Just S": "бывший Дровосек; Исследователь порталов Энда; эксперименты с армор-стендами",
    "KetrinCyst": "Лидер и идеолог Верстании; ключевая фигура политических событий",
    "KlashRaick": "Исследователь; участвовал в вылазках за зону и в войде",
    "KrolikMun": "Ломал рамки порталов Энда, следуя теории Неркина о «доброте» острова",
    "LordSantos": "бывший Дровосек; активный участник экспедиций",
    "Mo1vine": "Вступал в ГНДР как тайный агент Верстании",
    "MoDDyChat": "Решал шифры записок; построил пушку в Энд; участник громких событий",
    "Nerkin": "Автор теории о добром острове и порталах; медиа-участник",
    "NikiWright": "Участница СЭКС; замечала феномен ‘красных глаз’",
    "ObsidianTime69": "База близ места падения метеорита; вступал в Верстанию; база живая!!",
    "PWGood": "Лидер ГНДР; дипломат и инициатор проектов на грибном острове",
    "Sanhez": "Исследователь зоны; дипломат ГНДР/Верстании; исключён из Верстании",
    "SecB": "бывший Дровосек; Создатель сети спутников; аппаратура, магниты и обновления прошивки",
    "SirPiligrim": "Исследователь и путешественник; лаборатории, загадочные находки",
    "SnrGiraffe": "Жираф; получал записки; участвовал в озеленении грибного острова",
    "TheKlyde": "Наблюдал феномен ‘красных глаз’; заметки о питомцах и базе",
    "Venazar": "Вступал в Верстанию; Эльфийское королевство получило автономию",
    "Zakviel": "Наблюдал астрономические явления (кометы)",
}

# Выбор случайного факта по нику (фолбэк — краткое описание)
def pick_fact(nick: str) -> str:
    lst = INFO.get(nick)
    if isinstance(lst, list) and lst:
        return random.choice(lst)
    return DESCR.get(nick, "Участник MineShield IV")

# Альтернативные написания (синонимы/русские варианты/краткие формы)
ALIASES = {
    # Русские варианты и сокращения
    "Альцест": "Alcest M",
    "Алцест": "Alcest M",
    "Алфёдов": "Alfedov",
    "Алфедов": "Alfedov",
    "Арлабус": "Arlabus",
    "Барси": "BarsiGold",
    "БЛС": "Bez LS",
    "Без ЛС": "Bez LS",
    "Балбес": "Bez LS",
    "Кэп Ксеноморф": "CapXenomorph",
    "Кэп": "CapXenomorph",
    "Ксеноморф": "CapXenomorph",
    "Деб": "DEB",
    "Диамкей": "Diamkey",
    "Душенька": "Dushenka",
    "Фарадей": "Faradey",
    "Гельмо": "Gel mo",
    "Хайди": "Hayd1",
    "Нео": "HeO",
    "Джей Покерман": "Jay Pokerman",
    "Джей": "Jay Pokerman",
    "Покерман": "Jay Pokerman",
    "Джаст": "Just S",
    "Кэтрин": "KetrinCyst",
    "Клэш": "KlashRaick",
    "Кролик Мун": "KrolikMun",
    "Сантос": "LordSantos",
    "Молвин": "Mo1vine",
    "МоддиЧат": "MoDDyChat",
    "Модди": "MoDDyChat",
    "Неркин": "Nerkin",
    "Ники": "NikiWright",
    "ОбсидианТайм": "ObsidianTime69",
    "Пугод": "PWGood",
    "Санчез": "Sanhez",
    "Секби": "SecB",
    "Пилигрим": "SirPiligrim",
    "Жираф": "SnrGiraffe",
    "Клайд": "TheKlyde",
    "Веназар": "Venazar",
    "Заквиель": "Zakviel",
}

# Обратный индекс: для каждого канонического ника список его русских вариантов/сокращений
ALIASES_BY_CANON = {}
for _alias, _canon in ALIASES.items():
    ALIASES_BY_CANON.setdefault(_canon, []).append(_alias)

# Упорядочим варианты: сначала покороче, затем по алфавиту (по нормализованной форме)
for _variants in ALIASES_BY_CANON.values():
    _variants.sort(key=lambda s: (len(_norm(s)), _norm(s)))

def _fmt_with_aliases(nick: str) -> str:
    """Вернёт строку вида "Nick (рус, сокращения)" если есть альтернативы."""
    aliases = ALIASES_BY_CANON.get(nick, [])
    return f"{nick} (" + ", ".join(aliases) + ")" if aliases else nick

INFO_NORM = { _norm(k): k for k in DESCR.keys() }
for alias, canonical in ALIASES.items():
    INFO_NORM[_norm(alias)] = canonical

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я твой Telegram бот. Напиши что-нибудь!\nНапиши /help чтобы увидеть доступные команды.")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.send_message(message.chat.id, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.send_message(message.chat.id, "Пока! Удачи!")

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "Доступные команды:\n"
        "/start — приветствие и подсказка\n"
        "/hello — поздороваться\n"
        "/bye — попрощаться\n"
        "/menu — показать удобное меню\n"
        "/dice — бросить кости (d6)\n"
        "/coin — подбросить монетку\n"
        "/mineshield, /ms4, /участники — список ников участников MineShield IV (с русскими вариантами/сокращениями)\n"
        "/msinfo, /ms4info, /описания — краткие подписи о каждом участнике (с вариантами)\n"
        "/who <ник>, /mswho <ник>, /кто <ник> — краткая инфо по конкретному нику\n"
        "/fact [ник], /msfact [ник], /факт [ник] — рандомный факт (по нику или случайный)\n"
        "(Поддерживаются альтернативные написания ников: рус/англ, с пробелами/без)\n"
        "А также можешь просто написать что-нибудь — я повторю твое сообщение."
    )
    bot.send_message(message.chat.id, help_text)

@bot.message_handler(commands=['menu'])
def send_menu(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    kb.add(
        types.KeyboardButton('/help'),
        types.KeyboardButton('/mineshield'),
        types.KeyboardButton('/msinfo'),
        types.KeyboardButton('/who'),
        types.KeyboardButton('/fact'),
        types.KeyboardButton('/dice'),
        types.KeyboardButton('/coin'),
    )
    bot.send_message(message.chat.id, "Меню команд:", reply_markup=kb)

@bot.message_handler(commands=['mineshield', 'ms4', 'участники'])
def send_mineshield_list(message):
    nicks = [
        "Alcest M",
        "Alfedov",
        "Arlabus",
        "BarsiGold",
        "Bez LS",
        "CapXenomorph",
        "DEB",
        "Diamkey",
        "Dushenka",
        "Faradey",
        "Gel mo",
        "Hayd1",
        "HeO",
        "Jay Pokerman",
        "Just S",
        "KetrinCyst",
        "KlashRaick",
        "KrolikMun",
        "LordSantos",
        "Mo1vine",
        "MoDDyChat",
        "Nerkin",
        "NikiWright",
        "ObsidianTime69",
        "PWGood",
        "Sanhez",
        "SecB",
        "SirPiligrim",
        "SnrGiraffe",
        "TheKlyde",
        "Venazar",
        "Zakviel",
    ]
    reply_text = "Участники MineShield IV (ник + русские варианты/сокращения):\n" + "\n".join(
        f"• {_fmt_with_aliases(nick)}" for nick in nicks
    )
    bot.send_message(message.chat.id, reply_text)

@bot.message_handler(commands=['dice'])
def cmd_dice(message):
    roll = random.randint(1, 6)
    bot.send_message(message.chat.id, f"🎲 Выпало: {roll}")

@bot.message_handler(commands=['coin'])
def cmd_coin(message):
    side = random.choice(['Орел', 'Решка'])
    bot.send_message(message.chat.id, f"🪙 Монетка: {side}")

@bot.message_handler(commands=['msinfo', 'ms4info', 'описания'])
def send_mineshield_info(message):
    # Сформируем текст. Для ников без подробностей — стандартная подпись
    lines = []
    for nick in [
        "Alcest M","Alfedov","Arlabus","BarsiGold","Bez LS","CapXenomorph","DEB","Diamkey",
        "Dushenka","Faradey","Gel mo","Hayd1","HeO","Jay Pokerman","Just S","KetrinCyst",
        "KlashRaick","KrolikMun","LordSantos","Mo1vine","MoDDyChat","Nerkin","NikiWright",
        "ObsidianTime69","PWGood","Sanhez","SecB","SirPiligrim","SnrGiraffe","TheKlyde",
        "Venazar","Zakviel",
    ]:
        desc = DESCR.get(nick, "Участник MineShield IV")
        lines.append(f"• {_fmt_with_aliases(nick)} — {desc}")
    header = "Краткие подписи участников MineShield IV (с русскими вариантами/сокращениями):\n(Источник: хронология и упоминания на вики — mineshield.fandom.com)\n"
    text = header + "\n".join(lines)
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['fact', 'msfact', 'факт'])
def send_random_fact(message):
    # /fact <ник> — факт по нику; /fact — факт по случайному участнику
    parts = message.text.split(maxsplit=1)
    if len(parts) > 1 and parts[1].strip():
        query = parts[1].strip()
        key = INFO_NORM.get(_norm(query))
        if not key:
            # Частичное совпадение
            qn = _norm(query)
            candidates = [k for n,k in INFO_NORM.items() if n.startswith(qn) or qn in n]
            key = candidates[0] if candidates else None
        if key:
            bot.send_message(message.chat.id, f"{_fmt_with_aliases(key)} — {pick_fact(key)}")
            return
        bot.send_message(message.chat.id, "Не нашёл такого ника. Использование: /fact [ник]. Пример: /fact KetrinCyst")
        return
    # Случайный участник
    key = random.choice(list(DESCR.keys()))
    bot.send_message(message.chat.id, f"{_fmt_with_aliases(key)} — {pick_fact(key)}")

@bot.message_handler(commands=['who', 'mswho', 'кто'])
def send_who(message):
    # Ожидается: /who <ник>
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        prompt = bot.send_message(
            message.chat.id,
            "Введите ник участника (можно по-русски, работают алиасы):",
            reply_markup=types.ForceReply(selective=False)
        )
        bot.register_next_step_handler(prompt, who_query_step)
        return
    query = parts[1].strip()
    key = INFO_NORM.get(_norm(query))
    if not key:
        # Попробуем частичное совпадение по началу или вхождению
        qn = _norm(query)
        candidates = [k for n,k in INFO_NORM.items() if n.startswith(qn) or qn in n]
        key = candidates[0] if candidates else None
    if key:
        bot.send_message(message.chat.id, f"{_fmt_with_aliases(key)} — {DESCR[key]}")
    else:
        bot.send_message(message.chat.id, "Не нашёл такого ника. Проверь написание или используйте /mineshield для списка.")

def who_query_step(message):
    # Обработчик ответа на ForceReply для /who
    query = (message.text or '').strip()
    if not query:
        bot.send_message(message.chat.id, "Пустой ник. Попробуй снова: /who")
        return
    key = INFO_NORM.get(_norm(query))
    if not key:
        qn = _norm(query)
        candidates = [k for n,k in INFO_NORM.items() if n.startswith(qn) or qn in n]
        key = candidates[0] if candidates else None
    if key:
        bot.send_message(message.chat.id, f"{_fmt_with_aliases(key)} — {DESCR[key]}")
    else:
        bot.send_message(message.chat.id, "Не нашёл такого ника. Проверь написание или воспользуйся /mineshield.")

# Если пользователь присылает только ник — вернём описание
@bot.message_handler(func=lambda m: (
    bool(getattr(m, 'text', None))
    and _norm(m.text) in INFO_NORM
    and not (getattr(m, 'reply_to_message', None) and isinstance(m.reply_to_message, types.Message) and 'Введите ник участника' in (m.reply_to_message.text or ''))
))
def send_info_by_plain_nick(message):
    key = INFO_NORM[_norm(message.text)]
    bot.send_message(message.chat.id, f"{_fmt_with_aliases(key)} — {DESCR[key]}")


# Простая система small-talk (приветствия/прощания/спасибо/как дела)
GREETINGS = {"привет", "здравствуй", "здравствуйте", "hi", "hello", "дарова", "ку", "qq"}
FAREWELLS = {"пока", "до встречи", "увидимся", "бай", "bye"}
THANKS = {"спасибо", "благодарю", "thanks", "thx"}
HOW_ARE_YOU = {"как дела", "как ты", "как поживаешь"}

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = (message.text or "").strip()
    norm = _norm(text)
    # small-talk
    if norm in { _norm(x) for x in GREETINGS }:
        bot.send_message(message.chat.id, "Привет! Чем помочь? Нажми /menu для списка команд.")
        return
    if norm in { _norm(x) for x in FAREWELLS }:
        bot.send_message(message.chat.id, "Пока! Возвращайся 😊")
        return
    if norm in { _norm(x) for x in THANKS }:
        bot.send_message(message.chat.id, "Всегда пожалуйста!")
        return
    if any(phrase in text.lower() for phrase in HOW_ARE_YOU):
        bot.send_message(message.chat.id, "Отлично! Я готов помочь. Попробуй /fact или /who <ник>.")
        return
    # fallback — эхо
    bot.send_message(message.chat.id, text)

bot.polling()
