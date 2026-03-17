from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode

from service.func import create_kb, create_youtube_link 

from service.generate import ai_generate

from texts import *

import keyboards as kb

router = Router()

class Video(StatesGroup):
    enter = State()
    search = State()

class Gen(StatesGroup):
    wait = State()
    quastion = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"{start}")


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(help)
    
    
@router.message(Command('tips'))
async def cmd_start(message: Message):
    await message.answer(f"{TIPS}")


@router.message(Command("math"))
async def cmd_math(message: Message):
    await message.answer(
        f'''Отлично! Ты выбрал(а) профильную математику. Теперь давай определимся, что будем изучать:
        ''', reply_markup=kb.math_first_part
    )
    await message.answer(
        f'''Выбирай и погружайся в подготовку!'''
    )


@router.message(Command("phys"))
async def cmd_math(message: Message):
    await message.answer(
        f'''Отлично! Ты выбрал(а) физику. Теперь давай определимся, что будем изучать:
        ''', reply_markup=kb.phys_first_part_1
    )
    await message.answer(
        f'''Выбирай и погружайся в подготовку!'''
    )
    
@router.callback_query(F.data == 'next_phys')
async def next_phys(callback: CallbackQuery):
    await callback.message.answer(text='Следующий раздел', reply_markup=kb.phys_first_part_2)
    await callback.answer()
    
    
@router.callback_query(F.data == 'back_phys')
async def next_phys(callback: CallbackQuery):
    await callback.message.answer(text='Предыдущий раздел', reply_markup=kb.phys_first_part_1)
    await callback.answer()
    

@router.message(Command("inf"))
async def cmd_math(message: Message):
    await message.answer(
        f'''Отлично! Ты выбрал(а) информатику. Теперь давай определимся, что будем изучать:
        ''', reply_markup=kb.inf_first_part_1
    )
    await message.answer(
        f'''Выбирай и погружайся в подготовку!'''
    )


@router.callback_query(F.data == 'next_inf')
async def next_phys(callback: CallbackQuery):
    await callback.message.answer(text='Следующий раздел', reply_markup=kb.inf_first_part_2)
    await callback.answer()
    
    
@router.callback_query(F.data == 'back_inf')
async def next_phys(callback: CallbackQuery):
    await callback.message.answer(text='Предыдущий раздел', reply_markup=kb.inf_first_part_1)
    await callback.answer()

@router.callback_query(F.data == '1_task')
async def first_task_math(callback: CallbackQuery):
    await callback.message.answer(text='Задание 1', reply_markup=create_kb('1'))
    await callback.answer()  


@router.callback_query(F.data == '2_task')
async def first_task_math(callback: CallbackQuery):
    await callback.message.answer(text='Задание 2', reply_markup=create_kb('2'))
    await callback.answer()  

@router.callback_query(F.data == '3_task')
async def first_task_math(callback: CallbackQuery):
    await callback.message.answer(text='Задание 3', reply_markup=create_kb('3'))
    await callback.answer()  

@router.callback_query(F.data == '4_task')
async def first_task_math(callback: CallbackQuery):
    await callback.message.answer(text='Задание 4', reply_markup=create_kb('4'))
    await callback.answer()  


@router.callback_query(F.data == '5_task')
async def first_task_math(callback: CallbackQuery):
    await callback.message.answer(text='Задание 5', reply_markup=create_kb('5'))
    await callback.answer()  


@router.callback_query(F.data == '6_task')
async def first_task_math(callback: CallbackQuery):
    await callback.message.answer(text='Задание 6', reply_markup=create_kb('6'))
    await callback.answer()  


@router.callback_query(F.data == '7_task')
async def first_task_math(callback: CallbackQuery):
    await callback.message.answer(text='Задание 7', reply_markup=create_kb('7'))
    await callback.answer()  


@router.callback_query(F.data == '8_task')
async def first_task_math(callback: CallbackQuery):
    await callback.message.answer(text='Задание 8', reply_markup=create_kb('8'))
    await callback.answer()  


@router.callback_query(F.data == '9_task')
async def first_task_math(callback: CallbackQuery):
    await callback.message.answer(text='Задание 9', reply_markup=create_kb('9'))
    await callback.answer()  


@router.callback_query(F.data == '10_task')
async def first_task_math(callback: CallbackQuery):
    await callback.message.answer(text='Задание 10', reply_markup=create_kb('10'))
    await callback.answer()  


@router.callback_query(F.data == '11_task')
async def first_task_math(callback: CallbackQuery):
    await callback.message.answer(text='Задание 11', reply_markup=create_kb('11'))
    await callback.answer()  


@router.callback_query(F.data == '12_task')
async def first_task_math(callback: CallbackQuery):
    await callback.message.answer(text='Задание 12', reply_markup=create_kb('12'))
    await callback.answer()  
    

@router.callback_query(F.data == '13_task')
async def first_task_math(callback: CallbackQuery):
    await callback.message.answer(text='Задание 13', reply_markup=create_kb('13'))
    await callback.answer() 
    
    
@router.callback_query(F.data == '14_task')
async def first_task_math(callback: CallbackQuery):
    await callback.message.answer(text='Задание 14', reply_markup=create_kb('14'))
    await callback.answer() 
    
@router.callback_query(F.data == '15_task')
async def first_task_math(callback: CallbackQuery):
    await callback.message.answer(text='Задание 15', reply_markup=create_kb('15'))
    await callback.answer() 
    
@router.callback_query(F.data == '16_task')
async def first_task_math(callback: CallbackQuery):
    await callback.message.answer(text='Задание 16', reply_markup=create_kb('16'))
    await callback.answer() 
    
@router.callback_query(F.data == '17_task')
async def first_task_math(callback: CallbackQuery):
    await callback.message.answer(text='Задание 17', reply_markup=create_kb('17'))
    await callback.answer() 
    
@router.callback_query(F.data == '18_task')
async def first_task_math(callback: CallbackQuery):
    await callback.message.answer(text='Задание 18', reply_markup=create_kb('18'))
    await callback.answer() 
    
@router.callback_query(F.data == '19_task')
async def first_task_math(callback: CallbackQuery):
    await callback.message.answer(text='Задание 19', reply_markup=create_kb('19'))
    await callback.answer() 
    
@router.callback_query(F.data == '20_task')
async def first_task_math(callback: CallbackQuery):
    await callback.message.answer(text='Задание 20', reply_markup=create_kb('20'))
    await callback.answer() 
    
@router.callback_query(F.data == '21_task')
async def first_task_math(callback: CallbackQuery):
    await callback.message.answer(text='Задание 21', reply_markup=create_kb('21'))
    await callback.answer() 
    
    
@router.callback_query(F.data == '22_task')
async def first_task_math(callback: CallbackQuery):
    await callback.message.answer(text='Задание 22', reply_markup=create_kb('22'))
    await callback.answer() 
    
@router.callback_query(F.data == '23_task')
async def first_task_math(callback: CallbackQuery):
    await callback.message.answer(text='Задание 23', reply_markup=create_kb('23'))
    await callback.answer() 
    
@router.callback_query(F.data == '24_task')
async def first_task_math(callback: CallbackQuery):
    await callback.message.answer(text='Задание 24', reply_markup=create_kb('24'))
    await callback.answer() 
    
    








@router.message(Gen.wait)
async def stop_flood(message: Message):
    await message.answer("Подождите, ваш запрос генерируется.")


@router.message(Gen.quastion)
async def generating(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Gen.wait)
    response = await ai_generate(message.text)
    await message.answer(response, ParseMode.HTML)
    await state.clear()


@router.callback_query(F.data == 'ai_answer')
async def data_generate(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.quastion)
    await callback.answer('Введите ваш запрос по теории:')
    
# @router.callback_query(F.data == 'data_base')
# async def data_generate(callback: CallbackQuery, state: FSMContext):
#     await state.set_state(Gen.quastion)
#     await callback.answer('Введите ваш запрос по теории: ')

# @router.message(Gen.wait)
# async def stop_flood(message: Message):
#     await message.answer("Подождите, ваш запрос генерируется.")

# @router.message()
# async def generating(message: Message, state: FSMContext):
#     await state.clear()
#     await state.set_state(Gen.wait)
#     response = await ai_generate(message.text)
#     await message.answer(response, ParseMode.HTML)
#     await state.clear()

@router.callback_query(F.data == 'get_video')
async def video_search(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Video.enter)
    await callback.message.answer(text='Введите ваш запрос для поиска видеороликов:')
    await callback.answer()  
    

@router.message(Video.enter)
async def search_video(message: Message, state: FSMContext):
    await message.answer(text='Вот результаты поиска по вашему запросу: ')
    await message.answer(create_youtube_link(message.text))
