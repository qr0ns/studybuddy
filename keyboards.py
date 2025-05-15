from aiogram.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
)


math_first_part = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Задание 1", callback_data="1_task"),

            InlineKeyboardButton(text="Задание 2", callback_data="2_task"),

            InlineKeyboardButton(text="Задание 3", callback_data="3_task"),

            InlineKeyboardButton(text="Задание 4", callback_data="4_task"),
        ],
        [
            InlineKeyboardButton(text="Задание 5", callback_data="5_task"),

            InlineKeyboardButton(text="Задание 6", callback_data="6_task"),

            InlineKeyboardButton(text="Задание 7", callback_data="7_task"),

            InlineKeyboardButton(text="Задание 8", callback_data="8_task"),
        ],
        [
            InlineKeyboardButton(text="Задание 9", callback_data="9_task"),

            InlineKeyboardButton(text="Задание 10", callback_data="10_task"),

            InlineKeyboardButton(text="Задание 11", callback_data="11_task"),

            InlineKeyboardButton(text="Задание 12", callback_data="12_task"),
        ],
    ]
)


phys_first_part_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Задание 1", callback_data="1_task"),

            InlineKeyboardButton(text="Задание 2", callback_data="2_task"),

            InlineKeyboardButton(text="Задание 3", callback_data="3_task"),

            InlineKeyboardButton(text="Задание 4", callback_data="4_task"),
            
        ],
        [
            InlineKeyboardButton(text="Задание 5", callback_data="5_task"),
            
            InlineKeyboardButton(text="Задание 6", callback_data="6_task"),

            InlineKeyboardButton(text="Задание 7", callback_data="7_task"),

            InlineKeyboardButton(text="Задание 8", callback_data="8_task"),
        ],
        [
            InlineKeyboardButton(text="Задание 9", callback_data="9_task"),
            
            InlineKeyboardButton(text="Задание 10", callback_data="10_task"),
        ],
        
        [
            InlineKeyboardButton(text="Следующая страница", callback_data="next_phys"),
        ]
    ]
)
phys_first_part_2 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Задание 11", callback_data="11_task"),

            InlineKeyboardButton(text="Задание 12", callback_data="12_task"),

            InlineKeyboardButton(text="Задание 13", callback_data="13_task"),

            InlineKeyboardButton(text="Задание 14", callback_data="14_task"),
            
        ],
        
        [
            InlineKeyboardButton(text="Задание 15", callback_data="15_task"),
            
            InlineKeyboardButton(text="Задание 16", callback_data="16_task"),

            InlineKeyboardButton(text="Задание 17", callback_data="17_task"),

            InlineKeyboardButton(text="Задание 18", callback_data="18_task"),

        ],
        [
            InlineKeyboardButton(text="Задание 19", callback_data="19_task"),
            
            InlineKeyboardButton(text="Задание 20", callback_data="20_task"),
        ],
        
        [
            InlineKeyboardButton(text="Предыдущая страница", callback_data="back_phys"),
        ]
    ]
)


inf_first_part_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Задание 1", callback_data="1_task"),

            InlineKeyboardButton(text="Задание 2", callback_data="2_task"),

            InlineKeyboardButton(text="Задание 3", callback_data="3_task"),

            InlineKeyboardButton(text="Задание 4", callback_data="4_task"),
        ],
        [
            InlineKeyboardButton(text="Задание 5", callback_data="5_task"),

            InlineKeyboardButton(text="Задание 6", callback_data="6_task"),

            InlineKeyboardButton(text="Задание 7", callback_data="7_task"),

            InlineKeyboardButton(text="Задание 8", callback_data="8_task"),
        ],
        [
            InlineKeyboardButton(text="Задание 9", callback_data="9_task"),

            InlineKeyboardButton(text="Задание 10", callback_data="10_task"),

            InlineKeyboardButton(text="Задание 11", callback_data="11_task"),

            InlineKeyboardButton(text="Задание 12", callback_data="12_task"),
        ],
        
        [
            InlineKeyboardButton(text="Следующие задания", callback_data="next_inf"),
        ],
    ]
)

inf_first_part_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Задание 13", callback_data="13_task"),

            InlineKeyboardButton(text="Задание 14", callback_data="14_task"),

            InlineKeyboardButton(text="Задание 15", callback_data="15_task"),

            InlineKeyboardButton(text="Задание 16", callback_data="16_task"),
        ],
        [
            InlineKeyboardButton(text="Задание 17", callback_data="17_task"),

            InlineKeyboardButton(text="Задание 18", callback_data="18_task"),

            InlineKeyboardButton(text="Задание 19", callback_data="19_task"),

            InlineKeyboardButton(text="Задание 20", callback_data="20_task"),
        ],
        [
            InlineKeyboardButton(text="Задание 21", callback_data="21_task"),

            InlineKeyboardButton(text="Задание 22", callback_data="22_task"),

            InlineKeyboardButton(text="Задание 23", callback_data="23_task"),

        ],
        
        [
            InlineKeyboardButton(text="Предыдущие задания", callback_data="back_inf"),
        ],
    ]
)


math_second_part = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Задание 13", callback_data="?"),
        ],
        [
            InlineKeyboardButton(text="Задание 14", callback_data="?"),
        ],
        [
            InlineKeyboardButton(text="Задание 15", callback_data="?"),
        ],
        [
            InlineKeyboardButton(text="Задание 16", callback_data="?"),
        ],
        [
            InlineKeyboardButton(text="Задание 17", callback_data="?"),
        ],
        [
            InlineKeyboardButton(text="Задание 18", callback_data="?"),
        ],
        [
            InlineKeyboardButton(text="Задание 19", callback_data="?"),
        ],
    ]
)

first_task_math = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Теория",
                callback_data="data_base",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Практика", callback_data="first_task_math_practise"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Тест",
                url="https://bank-ege.ru/ege/profilnaya-matematika/tasks/task1/13-ugly-v-treugolnike  ",
                callback_data="?",
            ),
        ],
    ]
)

practise_first_task_math = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Тригонометрия в прямоугольном треугольнике",
                url="https://bank-ege.ru/ege/profilnaya-matematika/tasks/task1/11-trigonometriya-v-pryamougolnom-treugolnike",
                callback_data="triga_90_triangle",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Углы и отрезки в прямоугольном треугольнике",
                url="https://bank-ege.ru/ege/profilnaya-matematika/tasks/task1/12-ugly-i-otrezki-v-pryamougolnom-treugolnike",
                callback_data="?",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Углы в треугольнике",
                url="https://bank-ege.ru/ege/profilnaya-matematika/tasks/task1/13-ugly-v-treugolnike",
                callback_data="?",
            ),
        ],
        [
            InlineKeyboardButton(
                text="<<<  Назад  <<<", callback_data="back_first_part_first_task_math"
            ),
        ],
    ]
)

kb_back_first_part_math = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="<<< Назад <<<", callback_data="back_first_part_math"
            ),
        ],
    ]
)
