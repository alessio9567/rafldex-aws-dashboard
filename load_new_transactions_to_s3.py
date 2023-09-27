import utils
import boto3
import os

# Set the AWS profile name to use (replace with your profile name)
os.environ['AWS_PROFILE'] = 'aiannini-minsait'

ETHERSCAN_API_TOKEN = "FXDQ4IE84V61CDDSVYBMMRHQG4YY3EFH6V"

# Initialize S3 client
s3 = boto3.client('s3')

# Specify your S3 bucket name
bucket_name = 'rafldex'

# Ethereum account address creator of RAFLDex smart contracts
account_address = '0x92e825169Ee5D5e7235b548B9fb0709767DF23Db'

# if initial launch , then start_block = 0, else start_block = MAX(block) from transactions
start_block = 0

rafldex_smart_contract_addresses = utils.get_contracts_addresses_created_by_account(account_address, start_block)

# Array of array of json
rafldex_new_transactions = []

for contract in rafldex_smart_contract_addresses:
    # Specify the JSON file name
    json_file_name = f"{contract}_{start_block}"

    # Upload the JSON data as a JSON file to S3
    s3.put_object(
        Bucket=bucket_name,
        Key=json_file_name,
        Body=utils.get_transactions(contract,start_block),  # The JSON data string
        ContentType='application/json'  # Set the content type as JSON
    )

    #rafldex_new_transactions.append(utils.get_transactions(contract,start_block))



# transaction_hashes = ["0xfe48cb57029f5f5c102c5d0b6af6b883e2fcfbbb4971facb69e8c0ad0a532071",
#                      "0xff7e826a25489e0237ecb3393b7e57091ea1652764e67fa4f79c50312c801433"]




# loop cycle over transactions having "value" = 0
#get_all_transactions_receipts_url = "https://api.etherscan.io/api"

#params = {
#    "module": "proxy",
#    "action": "eth_getTransactionReceipt",
#    "txhash": "0xff7e826a25489e0237ecb3393b7e57091ea1652764e67fa4f79c50312c801433",
#    "apikey": ETHERSCAN_API_TOKEN
#}

#response = requests.get(get_all_transactions_receipts_url, params=params)
#json_response = response.json()