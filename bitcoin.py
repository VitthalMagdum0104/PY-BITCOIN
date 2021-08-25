import requests
from whatsapp import client, send_whatsapp


def get_rate_of_bitcoin(to_currency="INR"):
    """
    Gets Bitcoin value in particular using Rest Api by to_currency parameter.
    takes to_currency as parameter and returns value in that Currency using alpha-vantage api.

    """
    url = "https://alpha-vantage.p.rapidapi.com/query"

    querystring = {
        "from_currency": "BTC",
        "function": "CURRENCY_EXCHANGE_RATE",
        "to_currency": to_currency
    }

    headers = {
        'x-rapidapi-key': ,
        'x-rapidapi-host': "alpha-vantage.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    status = response.status_code
    match status:
        case 200:
            bitcoin_exchange_rate = response.json(
            )["Realtime Currency Exchange Rate"]
        case 400:
            bitcoin_exchange_rate = data["error"]["message"]
        case _:
            bitcoin_exchange_rate = "Sorry. Could not retrieved code."

    bitcoin_rate = "From Currency : {}\nTo Currency : {}\nTo Currency Name : {}\nExchange Rate : {}".format(
        bitcoin_exchange_rate['2. From_Currency Name'],
        bitcoin_exchange_rate['3. To_Currency Code'],
        bitcoin_exchange_rate['4. To_Currency Name'],
        bitcoin_exchange_rate['5. Exchange Rate']
    )

    return bitcoin_rate


message = get_rate_of_bitcoin()
