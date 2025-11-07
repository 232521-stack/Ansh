#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8376204434:AAH7QrzzEQ6QBsjViynOEP6u2WM72gF2TCk")
    API_ID = int(os.environ.get("API_ID", "20135931"))
    API_HASH = os.environ.get("API_HASH", "60fb3f132eda81a31e0f77177ef95a75")
    AUTH_USERS = "1411895712"


