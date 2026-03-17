from aiogram.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
)


def create_kb(task):
    kb_task = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=f'Получить видео-разборы задания {task}', callback_data=f'get_video'),
        ],
        [
            InlineKeyboardButton(text='Получить ответ по заданию от нейросети', callback_data='ai_answer')
        ],
    ])
    return kb_task


def create_youtube_link(query):
    # Кодируем пробелы и специальные символы
    encoded_query = query.replace(' ', '+')
    # Генерируем ссылку для поиска на YouTube
    link = f"https://www.youtube.com/results?search_query={encoded_query}"
    return link
