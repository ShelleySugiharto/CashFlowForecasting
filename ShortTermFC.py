#starting with 1mo period forecasting, assuming the general case (excludes scenario analysis)
#notes: username and pw for plaid is user_good, pass_good.
# if asked for authentication, 1234 is the code

import os
from plaid import ApiClient, Configuration
from plaid.api import plaid_api
from plaid.model import transactions_get_request
from plaid.model import transactions_get_request_options
from plaid.model import transactions_get_response
from plaid.model import country_code
from plaid.model import products
from plaid.model import item_public_token_exchange_request
from plaid.model import accounts_get_request
from plaid.model import accounts_balance_get_request
from datetime import datetime, timedelta

PLAID_CLIENT_ID = os.getenv('PLAID_CLIENT_ID')
PLAID_SECRET = os.getenv('PLAID_SECRET')
PLAID_ENV = 'sandbox'

config = Configuration(
    host="https://sandbox.plaid.com",
    api_key={
        'clientId': PLAID_CLIENT_ID,
        'secret': PLAID_SECRET
    }
)

api_client = ApiClient(config)
client = plaid_api.PlaidApi(api_client)

publicToken = 'access-sandbox-213c665b-4600-42bf-a24a-ec3a483a1dd2'

exchange_request = item_public_token_exchange_request(
    publicToken=publicToken
)
exchange_response = client.item_public_token_exchange(exchange_request)
access_token = exchange_response['access_token']