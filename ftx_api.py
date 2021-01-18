# ftx_api.py
import time
import hmac
from requests import Request, Session


def _ts():
    return int(time.time() * 1000)


class Ftx:
    API_HOST = 'https://ftx.com/api'

    def __init__(self, apikey, apisecret):
        self.API_KEY = str(apikey)
        self.API_SECRET = str(apisecret)

    def _sign(self, prepared, ts, path):
        signature_payload = f'{ts}{prepared.method}{prepared.path_url}'.encode()
        signature = hmac.new(self.API_SECRET.encode(), signature_payload, 'sha256').hexdigest()
        return signature

    def _headers(self, signature, ts):
        headers = {
            'FTX-KEY': self.API_KEY,
            'FTX-SIGN': signature,
            'FTX-TS': str(ts),
        }
        return headers

    def get_spot_margin_rates(self):
        path = '/spot_margin/borrow_rates'
        endpoint = self.API_HOST + path
        request = Request('GET', endpoint)
        prepared = request.prepare()
        ts = _ts()
        signature = self._sign(prepared, ts, path)
        headers = self._headers(signature, ts)
        prepared.headers = headers
        response = s.send(prepared)
        return response


s = Session()
