from web3 import Web3
import json
import handlers

from dotenv import load_dotenv
import os

rpc_url = os.getenv("RPC_URL")
abi_path = os.getenv("ABI_PATH")
caddress = os.getenv("CONTRACT_ADDRESS")

# Connect to a local Ethereum node or Infura
web3 = Web3(Web3.HTTPProvider(rpc_url))

contract_address = Web3.to_checksum_address(caddress)

with open(abi_path, 'r') as file:
    contract_abi = json.load(file)

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Replace 'Swap' with the name of the event you want to listen for
event_name = 'Swap'

# Replace 'latest' with the block number or 'pending' if you want to listen for future events
event_filter = contract.events[event_name].create_filter(fromBlock='pending')

while True:
    for event in event_filter.get_new_entries():
        handlers.handle_custom_event(event_name, event)
