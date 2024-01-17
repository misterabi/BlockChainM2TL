import time
import hashlib
import json
import requests
from urllib.parse import urlparse

class Smart_Blockchain:
    def __init__(self,current_transactions,chain):
        self.current_transactions = current_transactions
        self.chain = chain
        self.new_block(previous_hash=1)
        self.nodes = set()

    def new_block(self,previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.current_transactions,
            'previous_hash': previous_hash
        }
        self.current_transactions = []
        self.chain.append(block)
        return block
    
    def new_transaction(self,expéditeur,destinataire,montant):
        fees = 0.1
        self.current_transactions.append({
            'sender': expéditeur,
            'amount_send': montant,
            'bpsc': "bpsc_wallet_address",
            'amount_bpsc': float(montant) * fees,
            'recipient': destinataire,
            'amount_receive':(float(montant) * (float(1)-fees))
        })

        return self.last_block['index'] + 1
    
    @property
    def last_block(self):
        return self.chain[-1]
    
    def hash_block(self, block):
        block_string = json.dumps(block, sort_keys=True).encode('utf-8')
        return hashlib.sha256(block_string).hexdigest()

    def register_node(self, address):
        """ Add a new node to the list of nodes :param address: Address of node. Eg. 'http://192.168.0.5:5000' """
        parsed_url = urlparse(address) 
        if parsed_url.netloc:
            self.nodes.add(parsed_url.netloc) 
        elif parsed_url.path: 
        # Accepts an URL without scheme like '192.168.0.5:5000'. 
            self.nodes.add(parsed_url.path) 
        else: 
            raise ValueError('Invalid URL')
        
    def smart_chain(self):
        schain = None
        response = requests.get('http://127.0.0.1:5001/chain')

        if response.status_code == 200:
            schain = response.json().get('chain')

            if schain:
                self.chain = schain
                return True

        return False
    


