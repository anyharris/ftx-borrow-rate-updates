from tg_api import Telegram
from ftx_api import Ftx
from dotenv import load_dotenv
import os

load_dotenv()
ftx_api_key = os.getenv('FTXAPIKEY')
ftx_api_secret = os.getenv('FTXAPISECRET')
tg_eth_bot_token = os.getenv('ETHBOTTOKEN')
tg_eth_channel_id = os.getenv('ETHCHANNEL')
tg_usd_bot_token = os.getenv('USDBOTTOKEN')
tg_usd_channel_id = os.getenv('USDCHANNEL')
tg_bnb_bot_token = os.getenv('BNBBOTTOKEN')
tg_bnb_channel_id = os.getenv('BNBCHANNEL')

tg_eth = Telegram(tg_eth_bot_token, tg_eth_channel_id)
tg_usd = Telegram(tg_usd_bot_token, tg_usd_channel_id)
ftx = Ftx(ftx_api_key, ftx_api_secret)

response = ftx.get_spot_margin_rates().json()
rates = response['result']
for ticker in rates:
    if ticker['coin'] == 'ETH':
        apy = "{:.1%}".format(ticker['previous']*24*365)
        message = f'ETH borrowing: {apy}'
        tg_eth.broadcast(message)
    elif ticker['coin'] == 'USD':
        apy = "{:.1%}".format(ticker['previous']*24*365)
        message = f'USD borrowing: {apy}'
        tg_usd.broadcast(message)
    elif ticker['coin'] == 'BNB':
        apy = "{:.1%}".format(ticker['previous']*24*365)
        message = f'BNB borrowing: {apy}'
        tg_usd.broadcast(message)