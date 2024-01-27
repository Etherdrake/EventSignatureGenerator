from web3 import Web3
import json

def handle_custom_event(event_name, event):
    print(f"Event {event_name} triggered with data: {event['args']}")
