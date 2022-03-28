import tweepy, time, json


consumer_key = 'aCYstLGKwlnTNPv4XVSvwSgwK'
consumer_secret = 'BmuVahErvQrvoZJgGKpA7XhJ205Aj6p8t0isV5RroyxqZDYFWJ'
access_token = '1192598952530599938-c15IKBqfCemWCtykbllimbb4e0LSUX'
access_token_secret = 'UxabQmDR9VDUHHfbV9rd4IUmPOmi4FNhcel60X9JPcHwG'

# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Price API
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'id':'1'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'd9689ffe-4506-4b3b-84b8-66722748a2a8',
}

session = Session()
session.headers.update(headers)


def get_data():
    data = None
    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)

    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)

    return data

def main():
    while True:
        # Start with a clean sheet
        data = None

        while not data:
            # trigger a get every 10 min unless we get data
            data = get_data()
            if data:
                print('Raw data: %s' %data)
                break
            else:
                print('Did not find data, waiting 10 min')
                time.sleep(60*10)

        # At this point we know we have data to work with, but just in case
        try:
            bitcoin_price = data['data']['1']['quote']['USD']['price']
            print('bitcoin_price: %s' %bitcoin_price)
        except:
            break

        #define prices
        fraction = round((bitcoin_price * .003), 2)

        # update the status
        status = "7 Billion people. 21 million #btc. " + '\n'  '\n'\
           "300k sats per human." + '\n' '\n'\
           "Today's cost to secure this real estate: $" + str(fraction) + " USD."

        print('About to post the following status: %s' %status)
        api.update_status(status=status)


        time.sleep(60*60*5)

if __name__ == "__main__":
    main()
