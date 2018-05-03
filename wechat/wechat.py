#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wechat_sender import *
from wxpy import *

name = '新boss问题反馈交流群'

name_test = '比利外卖'
bot = Bot(console_qr=True, cache_path=True)
bot.enable_puid()
my_friend = bot.groups().search(name_test)[0]
my_friend.send('Wechat Test')


def send_message(name, message):
    friend = bot.groups().search(name)[0]
    friend.send(message)


send_message(name_test, "test")
