import configparser
import os

from pyrogram import Client

config_path = 'config.ini'
if not os.path.isfile(config_path):
    print('Config file not found!')
    exit(1)
config = configparser.ConfigParser()
config.read(config_path)
bot_username = config.get('bot', 'bot_username')
bot_token = config.get('bot', 'bot_token')
admin_id = int(config.get('bot', 'admin_id'))
mongo_url = config.get('bot', 'mongo_url')
api_id = 2040
api_hash = "b18441a1ff607e10a989891a5462e627"
plugins = dict(root="TeamIndia.modules")


def main():
    app = Client(
        session_name=bot_username,
        bot_token=bot_token,
        api_id=api_id,
        api_hash=api_hash,
        plugins=plugins
    )
    app.run()
