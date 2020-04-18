import requests
import json
import threading

def ticker_blockchain():
    response = requests.get('https://blockchain.info/ticker')
    return response.json()
def ticker_cex():
    response = requests.get('https://cex.io/api/ticker/BTC/USD')
    return response.json()
def ticker_bitstamp():
    response = requests.get('https://www.bitstamp.net/api/ticker/')
    return response.json()
def ticker_bitbay():
    response = requests.get('https://bitbay.net/API/Public/BTC/ticker.json')
    return response.json()

wallet = [0, 5]

def Arbitrage(wallet):
    blockchain = ticker_blockchain()
    blockchain_buy = float(blockchain['USD']['buy'])
    blockchain_sell = float(blockchain['USD']['sell'])

    cex = ticker_cex()
    cex_bid = float(cex['bid'])
    cex_ask = float(cex['ask'])

    bitstamp = ticker_bitstamp()
    bitstamp_bit = float(bitstamp['bid'])
    bitstamp_ask = float(bitstamp['ask'])

    bitbay = ticker_bitbay()
    bitbay_bid = float(bitbay['bid'])
    bitbay_ask = float(bitbay['ask'])

    b_index = {'bitbay':bitbay_ask, 'bitstamp':bitstamp_ask, 'cex':cex_ask, 'blockchain':blockchain_buy}
    s_index = {'bitbay':bitbay_bid, 'bitstamp':bitstamp_bit, 'cex':cex_bid, 'blockchain':blockchain_sell}
    t_index = {'bitbay':0.043, 'bitstamp':0.05, 'cex':0.05, 'blockchain':0.24}

    buy_price = min(b_index.values())
    buy = min(b_index, key=b_index.get)

    sell_price = max(s_index.values())
    sell = min(s_index, key=s_index.get)

    taker_indexb = t_index[buy]
    takerb = 1+taker_indexb

    taker_indexs = t_index[sell]
    takers = 1-taker_indexs

    USD = wallet[0]
    BTC = wallet[1]

    buing = BTC*buy_price*takerb
    selling = BTC*sell_price*takers

    if buing < selling:
        print('Kup',BTC,'bitcoiny na: ',buy,'za',buy_price,'\n i sprzedać na: ',sell,'za',sell_price,'\n z zyskiem: ',round((selling-buing),3),'$')
    else: print('Nic nie kupuj, arbitraz niemozliwy')

    threading.Timer(3, Arbitrage(wallet)).start()
    
Arbitrage(wallet)

    