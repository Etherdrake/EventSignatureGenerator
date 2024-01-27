from web3 import Web3
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()
import json

rpc_url = os.getenv("RPC_URL")
abi_path = os.getenv("ABI_PATH")
caddress = os.getenv("CONTRACT_ADDRESS")

def listen_to_contract():
    # Connect to a local Ethereum node or Infura
    web3 = Web3(Web3.HTTPProvider(rpc_url))

    # Set this address to the actual contract address in .env
    contract_address = Web3.to_checksum_address(caddress)

    # Load ABI from the JSON file
    with open(abi_path, 'r') as file:
        contract_abi = json.load(file)

    contract = web3.eth.contract(address=contract_address, abi=contract_abi)

    # Get all event names from the ABI
    event_names = [entry['name'] for entry in contract_abi if entry['type'] == 'event']

    def handle_event(event):
        print(f"Event {event['event']} triggered with data: {event['args']}")

    # Listen to all events
    for event_name in event_names:
        event_filter = contract.events[event_name].create_filter(fromBlock='latest')

        while True:
            for event in event_filter.get_new_entries():
                handle_event(event)

listen_to_contract()