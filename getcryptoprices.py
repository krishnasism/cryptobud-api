import json
import requests
from decimal import Decimal
from creds import apikey

class Crypto:
	def getCryptoPrice(self, cryptoSym):
		try:
			url = f"https://api.lunarcrush.com/v2?data=assets&key={apikey}&symbol={cryptoSym}"
			data = json.loads(requests.get(url).content, parse_float=Decimal)["data"][0]
			return data["price"]
		except Exception:
			return 0