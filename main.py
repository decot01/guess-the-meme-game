from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import random

rofls = ["Когда узнал, сколько ей лет",
        "Когда узнал, что ее батя военком.",
        "Когда матюкнулся при родителях.",
        "Когда мама назвала тебя 'сукин сын'.",
        "Когда не можешь в карманах нащупать ключи.",
        "Когда меняешь статус 'в отношениях' на 'в активном поиске'.",
        "Когда услышал: 'Садись, пять', но вспомнил, что ты в суде.",
        "Когда в 3 часа ночи посмотрел мотивационный ролик на Youtube.",
        "Когда узнал, что вылечить зуб стоит 15 000 рублей, а удалить - 3000.",
        "Когда твой врач говорит: 'Сколько пальцев?', а ты на проверке простаты.",

        "Когда Мурат до богоподобия громко пердит на всю комнату.",
        "С каким лицом Гоша сочинял стэндап.",
        "Наши лица, когда Мурат бежит за нами с обосранным куском наждачки до 6 утра.",
        "Когда все уже договорились и пошли гулять, а один балбес не пришел потому что даже не удосужился открыть группу.",
        "Когда договаривались пойти в кино, а Настя не ела три дня.",
        "Когда ты уже весь синий от того, что тебя душит амбал дзюдоист, зато твой кент все снимает на 4k 60fps.",
        "Когда договаривались гасить Мурата на фиджитале, а в итоге его команда на первом месте.",
        "Когда Настя с Шухратом снова оставляют одну Соню на произвол судьбы с нами.",
        "Когда пошел весь нарядный и яркий на лагерную дискотеку, а в итоге там было 4 человека считая диджея.",
        "Как Гоша ощущает себя осознавая, что он меньше по габаритам и может получить люлей, но все равно высирает какую-то задевающую шутку.",

        "Когда Мурат говорит: «Я бы тебе кое-что сказал, но ты обидишься»",
        "Наши лица, когда Настя избегала всех два дня потому, что ей приснилось как они не поделили воппер с Соней.",
        "Когда хотели устроить мега-пранк с бананом над сожителем в лагере, а он даже не заметил.",
        "Когда Мурат хвастается видосом, где два шкета в падике шалят.",
        "Когда Соня говорит, что приготовит нам покушать.",
        "Когда сказали, что в лагере будет вожатый чеченец.",
        "Последняя нервная клетка Шухрата, когда до него снова докопался Мурат.",
        "Когда учишься в школе, в которой каждую неделю происходит бойцовский клуб.",
        "Когда пересматривешь свои посты 5-летней давности.",
        "Когда представляешь себя в эдите.",]

class MyBot(StatesGroup):
    def __init__(self, token):
        self._TOKEN = token
        self.bot = Bot(token=self._TOKEN)
        self.dp = Dispatcher(bot=self.bot, storage=MemoryStorage())

        @self.dp.message_handler(commands=['start'])
        async def hello(message: types.Message):
            inline_keyboard = self.get_inline_keyboard()
            await message.answer("Привет, я бот 'угодай мем' с моей помощью ты сможешь сыграть в эту игру с друзьями!", reply_markup=inline_keyboard)

        @self.dp.callback_query_handler(lambda query: query.data == 'help')
        async def show_info(callback_query: types.CallbackQuery):
            await callback_query.answer()
            await callback_query.message.answer("Инструкция: Добавь меня в вашу группу, прочтите правила и если хоте сыграть жмите кнопку 'Начать'")

        @self.dp.callback_query_handler(lambda query: query.data == 'rules')
        async def show_info(callback_query: types.CallbackQuery):
            await callback_query.answer()
            await callback_query.message.answer("""Правила игры:
1.Нужно использовать стикеры из тг. 
2.Ведущий из нажимает начать или дальше и показывается тема. 
3.Каждый игрок кидает самый смешной мем под эту ситуацию по его мнению. 
4.Ведущий выбирает самый смешной мем и даёт игроку 1 балл. 
5.Побеждает игрок, первый набравший 5 баллов.""")

        @self.dp.callback_query_handler(lambda query: query.data == 'StartRound')
        async def show_info(callback_query: types.CallbackQuery):
            await callback_query.answer()
            inline_keyboard = self.ingame_keyboard()
            random_phrase = random.choice(rofls)
            print(random_phrase)
            await callback_query.message.answer(random_phrase, reply_markup=inline_keyboard)


    def get_inline_keyboard(self):
        keyboard = InlineKeyboardMarkup()
        keyboard.add(InlineKeyboardButton('help📄', callback_data='help'))
        keyboard.add(InlineKeyboardButton('Правила📕', callback_data='rules'))
        keyboard.add(InlineKeyboardButton('Начать▶️', callback_data='StartRound'))
        return keyboard
    def ingame_keyboard(self):
        keyboard = InlineKeyboardMarkup()
        keyboard.add(InlineKeyboardButton('Дальше➡️', callback_data='StartRound'))
        return keyboard

    

    def start(self):
        executor.start_polling(self.dp, skip_updates=True)

if __name__ == '__main__':
    token = '7537776117:AAFO1g00QvqnvU3eag1kk5mDPGJTBvtvh5o'
    bot = MyBot(token)
    bot.start()
