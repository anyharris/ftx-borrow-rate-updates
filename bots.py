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
tg_btc_bot_token = os.getenv('BTCBOTTOKEN')
tg_btc_channel_id = os.getenv('BTCCHANNEL')
tg_usdt_bot_token = os.getenv('USDTBOTTOKEN')
tg_usdt_channel_id = os.getenv('USDTCHANNEL')

tg_eth = Telegram(tg_eth_bot_token, tg_eth_channel_id)
tg_usd = Telegram(tg_usd_bot_token, tg_usd_channel_id)
tg_bnb = Telegram(tg_bnb_bot_token, tg_bnb_channel_id)
tg_btc = Telegram(tg_btc_bot_token, tg_btc_channel_id)
tg_usdt = Telegram(tg_usdt_bot_token, tg_usdt_channel_id)

ftx = Ftx(ftx_api_key, ftx_api_secret)

response = ftx.get_spot_margin_borrow().json()
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
        tg_bnb.broadcast(message)

response = ftx.get_spot_margin_lend().json()
rates = response['result']
for ticker in rates:
    if ticker['coin'] == 'BTC':
        apy = "{:.1%}".format(ticker['previous'] * 24 * 365)
        message = f'BTC lending: {apy}'
        tg_btc.broadcast(message)
    if ticker['coin'] == 'USDT':
        apy = "{:.1%}".format(ticker['previous'] * 24 * 365)
        message = f'USDT lending: {apy}'
        tg_usdt.broadcast(message)