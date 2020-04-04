import requests
import json

def data_bb():
    data = requests.get('https://bitbay.net/API/Public/BTCPLN/all.json')
    return data.json()

data = data_bb()

Asks = data['asks']

Ask = data['ask']

Bids  = data['bids']

Bid = data['bid']

Max = data['max']

Min = data['min']

Vwap = data['vwap']

Average = data['average']


print('Asks=',Asks)
print('Ask=',Ask)
print('Bids=',Bids)
print('Bid=',Bid)
print('Max=',Max)
print('Min=',Min)
print('Vwap=',Vwap)
print('Average=',Average)





