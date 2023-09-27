import requests
#import json
import pandas as pd

ETHERSCAN_API_TOKEN = "FXDQ4IE84V61CDDSVYBMMRHQG4YY3EFH6V"
CONTRACT_ADDRESS_1 = "0x08e1bc602c44ecb7932387b6792c3cb0a5c64a92"
CONTRACT_ADDRESS_2 ="0xB09B88ac29Dd39B4a719650C44aC787Fa2D2D7a3"

get_all_transactions_url = f'https://api.etherscan.io/api?module=account&action=txlist&address={CONTRACT_ADDRESS_2}&startblock=0&endblock=99999999&sort=asc&apikey={ETHERSCAN_API_TOKEN}'

data = pd.DataFrame(requests.get(get_all_transactions_url))

# if response.status_code == 200:
#  data = pd.DataFrame(data['result'])
#  data.tail().T
# else:
#  print(f"Error: {response.status_code}")

transaction_hashes = ["0xfe48cb57029f5f5c102c5d0b6af6b883e2fcfbbb4971facb69e8c0ad0a532071",
                      "0xff7e826a25489e0237ecb3393b7e57091ea1652764e67fa4f79c50312c801433"]

# fare un ciclo for per ciclare sugli hash delle txs che hanno value = 0
get_all_transactions_receipts_url = "https://api.etherscan.io/api"

params = {
    "module": "proxy",
    "action": "eth_getTransactionReceipt",
    "txhash": "0xfe48cb57029f5f5c102c5d0b6af6b883e2fcfbbb4971facb69e8c0ad0a532071",
    "apikey": ETHERSCAN_API_TOKEN
}

response = requests.get(get_all_transactions_receipts_url, params=params)
json_response = response.json()