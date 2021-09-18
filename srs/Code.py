from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
import pprint

print("Please, enter a positive integer number: ")
x = int(input())

pprint.pprint(cg.get_coins_markets(vs_currency='usd', per_page=x))
