import json
import time
import requests

def bitstamp_ticker():
    BTC = requests.get("https://www.bitstamp.net/api/v2/ticker/btcusd")
    LTC = requests.get("https://www.bitstamp.net/api/v2/ticker/ltcusd")
    ETH = requests.get("https://www.bitstamp.net/api/v2/ticker/ethusd")
    XRP = requests.get("https://www.bitstamp.net/api/v2/ticker/xrpusd")
    BCH = requests.get("https://www.bitstamp.net/api/v2/ticker/bchusd")
    return BTC.json(), LTC.json(), ETH.json(), XRP.json(), BCH.json()

def funkcja():
    BTC, LTC, ETH, XRP, BCH = bitstamp_ticker()

    btc_max = float(BTC["high"])
    btc_min = float(BTC["low"])

    xrp_max = float(XRP["high"])
    xrp_min = float(XRP["low"])

    ltc_max = float(LTC["high"])
    ltc_min = float(LTC["low"])

    eth_max = float(ETH["high"])
    eth_min = float(ETH["low"])

    bch_max = float(BCH["high"])
    bch_min = float(BCH["low"])

    zysk = [(btc_max / btc_min - 1) * 100, (xrp_max / xrp_min - 1) * 100, (ltc_max / ltc_min - 1) * 100,
             (eth_max / eth_min - 1) * 100, (bch_max / bch_min - 1) * 100]

    calls = ["BTC", "LTC", "ETH", "XRP", "BCH"]

    def sort(a):
     tab_size = len(a)
     tab = a.copy()
     ind = list(range(tab_size))
     w = 1
     while w != (tab_size-1):
         w = tab_size - 1
         for i in range(tab_size-1):
             if tab[i] < tab[i + 1]:
                 w = w - 1
                 b1 = tab[i]
                 b2 = tab[i + 1]
                 tab[i] = b2
                 tab[i + 1] = b1

                 in1 = ind[i]
                 in2 = ind[i + 1]
                 ind[i] = in2
                 ind[i + 1] = in1
     return tab, ind


    for i in range(len(zysk)):
        zysk[i] = round(zysk[i],2)

    zysk_sorted, ind = sort(zysk)
    calls_sorted = []

    for i in range(len(ind)):
        calls_sorted.append(calls[ind[i]])
    for i in range(len(zysk_sorted)):
        if zysk_sorted[i] > 0:
            print(calls_sorted[i], "+", zysk_sorted[i])
        else:
            print(calls_sorted[i], "", zysk_sorted[i])
while 1:
    funkcja()
    time.sleep(100)