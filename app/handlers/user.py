import asyncio
from logging import getLogger
from io import BytesIO

from aiogram import Router, F, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, BufferedInputFile
from aiogram.utils.keyboard import InlineKeyboardMarkup
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.enums import ChatAction

from utils.recognition import recognition_audio
from database.requests import get_recepts, get_recepts_from_db, add_new_user
from keyboards.keyboards import recept_buttons
from utils.create_msg import create_recept_message

user = Router()
log = getLogger(__name__)


@user.message(CommandStart())
async def cmd_start(msg: Message):
    await add_new_user(tg_id=msg.from_user.id,
                            username=msg.from_user.username,
                            firstname=msg.from_user.first_name,
                            lastname=msg.from_user.last_name)
    await msg.answer(
        f'Привет, {msg.from_user.first_name}! Я помогу решить, что приготовить. Запиши мне голосовое с перечислением того, что есть у тебя есть из продуктов и я подберу блюдо.',
    )

@user.message(F.voice)
async def audio(msg: Message, bot:Bot):
    """распознание аудио, запрос"""
    file = await bot.get_file(msg.voice.file_id)
    log.debug(f'Получено голосовое: {file.file_id} от {msg.from_user.id}')
    await msg.bot.send_chat_action(chat_id=msg.from_user.id, action=ChatAction.TYPING)
    with BytesIO() as bytes:
        await bot.download_file(file.file_path, destination=bytes)
        bytes.seek(0)
        text_voice = await recognition_audio(audio_file=bytes)
        log.debug(f'Распознано: {text_voice} от {msg.from_user.id}')
    kb = await get_list_recepts(text_search=text_voice)
    await msg.answer(text='Выбор блюд:', reply_markup=kb)
    # await msg.edit_reply_markup(reply_markup=kb)


async def get_list_recepts(text_search:str) -> InlineKeyboardMarkup:
    """создание списка кнопок из релевантных рецептов"""
    recepts = await get_recepts(words=text_search)
    log.debug(f'релевантные ответы: {recepts} на {text_search}' )
    return await recept_buttons(relevant_recepts=recepts)


@user.callback_query(F.data.startswith('recept_id_'))
async def get_recept(callback:CallbackQuery):
    """получение рецепта"""
    id_recept = callback.data.replace('recept_id_', '')
    recepts = await get_recepts_from_db(ids=[id_recept], select='*')
    txts = create_recept_message(recepts[0])
    await callback.answer('')
    await callback.message.answer(text=txts[0])
    for row in txts[1]:
        await callback.message.answer(text=row)
