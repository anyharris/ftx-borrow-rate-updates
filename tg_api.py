# tg_requests.py
import requests


class Telegram:
    API_HOST = 'https://api.telegram.org'

    def __init__(self, bot_token, channel_id):
        self.TG_BOT_TOKEN = bot_token
        self.TG_CHANNEL_ID = channel_id

    def _get(self, path, params):
        uri = self.API_HOST + path
        response = requests.get(uri, params=params)
        return response

    def broadcast(self, msg):
        path = f'/bot{self.TG_BOT_TOKEN}/sendMessage'
        params = {
            'chat_id': self.TG_CHANNEL_ID,
            'text': msg
        }
        response = self._get(path, params)
        return response
