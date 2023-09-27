import requests

# Replace with your own Etherscan API key
api_key = 'FXDQ4IE84V61CDDSVYBMMRHQG4YY3EFH6V'

# Etherscan API base URL
base_url = 'https://api.etherscan.io/api'

def is_valid_contract_address(address):
    if len(address) == 42:
        return True
    else:
        return False


# Function to get the list of transactions for the account
def get_transactions(address, start_block):
    url = f"{base_url}?module=account&action=txlist&address={address}&startblock={start_block}&endblock=99999999&page=1&sort=asc&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data['result']


# Function to check if a transaction is a contract creation
def is_contract_creation(transaction):
    input_data = transaction['input']
    return input_data != '0x'  # If input data is not empty, it's likely a contract creation


# Function to extract contract addresses from transactions
def get_contract_addresses(transactions):
    contract_addresses = set()
    for tx in transactions:
        if is_contract_creation(tx):
            contract_addresses.add(tx['to'])
    return list(contract_addresses)


def get_contracts_addresses_created_by_account(account_address, start_block):
    transactions = get_transactions(account_address, start_block)
    contract_addresses = get_contract_addresses(transactions)

    if not contract_addresses:
        print(f"No contracts found for address {account_address}")
    else:
        print(f"Contracts created by address {account_address}:")
        for address in contract_addresses:
            print(address)

    return contract_addresses
