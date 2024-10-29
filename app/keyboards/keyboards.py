from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from utils.create_msg import ICONS_CAT

async def recept_buttons(relevant_recepts:list[dict]) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for recept in relevant_recepts:
        kb.add(
            InlineKeyboardButton(
                text=f"{ICONS_CAT.get(recept.get('category'))} {recept.get('title')}",
                callback_data=f'recept_id_{recept.get('id')}'
                 )
        )
    return kb.adjust(1).as_markup()