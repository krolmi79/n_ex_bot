#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import telebot
import subprocess
from background import keep_alive
import eng_to_ipa as ipa

token = os.environ['TOKEN']
bot = telebot.TeleBot(token)
def text_to_convert(text):
    converted_text = (ipa.convert(text))
    return converted_text
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Произнесите или напечатайте фразу на английском языке; откройте текстовый или аудио файл: ')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    result_convert = text_to_convert(message.text)
    bot.send_message(message.chat.id, 'Транскрипция: ' + result_convert)

keep_alive()
bot.polling(none_stop=True, interval=0)# Очень не культурно стучимся телеге и проверяем наличие сообщений