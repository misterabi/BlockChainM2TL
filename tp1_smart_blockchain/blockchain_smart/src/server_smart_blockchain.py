import hashlib
import json 
from time import time
from urllib.parse import urlparse
from flask import Flask, jsonify, request
from Smart_Blockchain import Smart_Blockchain
import sys 


app = Flask(__name__)
blockchain = Smart_Blockchain([],[])


@app.route('/mine', methods=['GET'])
def mine(): 
    last_block = blockchain.last_block
    previous_hash = blockchain.hash_block(last_block)
    block = blockchain.new_block(previous_hash)
    response = {
        'message': "New Block créee",
        'index': block['index'],
        'transactions': block['transactions'],
        'previous_hash': block['previous_hash']
    }

    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    required = ['sender','recipient','amount']
    if not all(k in values for k in required):
        return 'Missing values'+values, 400
    index = blockchain.new_transaction(values['sender'],values['recipient'],values['amount'])
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

@app.route('/nodes/register', methods=['POST'])
def register_nodes(): 
    nodes = request.get_json().get('nodes')
    if not nodes:
        return jsonify({'message': 'No nodes provided'}), 400
    for node in nodes:
        blockchain.register_node(node)
    response = { 
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes)
    } 
    return jsonify(response), 201

@app.route('/smart/chain', methods=['GET'])
def smart_chain():
    replaced = blockchain.smart_chain()
    response = None
    if replaced: 
        response = { 
            'message': 'Smart chain update by bpsc', 
            'smart chain': blockchain.chain, 
            'length': len(blockchain.chain) 
        } 
    else: 
        response = { 
            'message': 'Unsuccessful: Please try again',
            'old chain': blockchain.chain, 
            'length': len(blockchain.chain)
        } 
    return jsonify(response), 200
    

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=sys.argv[1])