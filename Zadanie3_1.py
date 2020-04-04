import requests
import json

def data_bb():
    data = requests.get('https://bitbay.net/API/Public/BTCPLN/all.json')
    return data.json()

data = data_bb()
ask = data['ask']
bid = data['bid']

def data_stamp():
    data= requests.get('https://www.bitstamp.net/api/ticker/')
    return data.json()

data = data_stamp()

asks = float(data['ask'])
bids = float(data['bid'])


print('ask=',ask)
print('bid=',bid)
print('asks=',asks)
print('bids=',bids)

if bid < bids:
    print('Zakup w BitBay')
else:
    print('Zakup w BitStamp')

if ask>asks:
    print('Zakup w BitBay')
else:
    print('Zakup w BitStamp')
