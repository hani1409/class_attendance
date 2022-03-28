import yfinance, tweepy, time, requests, json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def CoinData():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'id': '1'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'd9689ffe-4506-4b3b-84b8-66722748a2a8',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)


    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    return data

# define prices
def GetPrice(data):
    # bitcoin prices
    coinmarketcap_btc_price = data['data']['1']['quote']['USD']['price']
    bitcoin_price = coinmarketcap_btc_price
    bitcoin_quantity = 0.13900473
    origin_value = (bitcoin_quantity * 7194)
    btc_new_value = round((bitcoin_quantity * bitcoin_price), 2)
    btc_change_pct = round((btc_new_value - origin_value) / (origin_value) * 100)

    # get prices from yfinance
    SPY = yfinance.Ticker("SPY").info['previousClose']
    # SPY Prices
    spy_origin_value = (324.87 * 3.07)
    spy_new_value = round((3.07 * SPY), 2)
    spy_change_pct = round((spy_new_value - spy_origin_value) / (spy_origin_value) * 100)

    BRKA = yfinance.Ticker("BRK-A").info['previousClose']
    # Berkshire Prices
    brka_origin_value = (342261 * .00292175)
    brka_new_value = round((.00292175 * BRKA), 2)
    brka_change_pct = round((brka_new_value - brka_origin_value) / (brka_origin_value) * 100)

    GLD = yfinance.Ticker("GLD").info['previousClose']
    # Gold Prince
    gld_origin_value = (143.95 * 6.94685)
    gld_new_value = round((6.94685 * GLD), 2)
    gld_change_pct = round((gld_new_value - gld_origin_value) / (gld_origin_value) * 100)

    return (btc_new_value, btc_change_pct,
            spy_new_value, spy_change_pct,
            brka_new_value, brka_change_pct,
            gld_new_value, gld_change_pct)

# update the status
while True:

    price = GetPrice(CoinData())

    print('\n'
          "#Bitcoin = $" + str(price[0]) + " (+" + str(price[1]) + "%)" '\n' + '\n'
                                                                                          "S&P Index Fund $SPY = $" + str(
        price[2]) + " (" + str(price[3]) + "%)"  '\n' + '\n'
                                                                   "Berkshire Hathaway $BRK.A @WarrenBuffett = $" + str(
        price[4]) + " (" + str(price[5]) + "%)" '\n' + '\n'
                                                                    "Gold $GLD @PeterSchiff = $" + str(
        price[6]) + " (+" + str(price[7]) + "%)")

    time.sleep(10)