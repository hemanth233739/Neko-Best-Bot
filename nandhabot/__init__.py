import os
from pyrogram import Client 

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
SUPPORT = os.environ.get("SUPPORT", None)
UPDATES = os.environ.get("UPDATES", None)

bot = Client("nandhabot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="{}/plugins".format(__name__)))


PM_START_TEXT = "hello! {}\nI'm anime themed nekos bot below click the help button know my commandslist!"
PM_START_IMG = [
 "https://telegra.ph/file/5d0953a536678e88e9e2a.jpg",
"https://telegra.ph/file/ce2fda9ecae0a574f1d42.jpg",
"https://telegra.ph/file/ee4087f9c29b16e6a1b64.jpg",
"https://telegra.ph/file/529c6071dbdd7600990ad.jpg" ]
