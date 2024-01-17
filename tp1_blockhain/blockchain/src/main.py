from blockchain import BlockChain

blockchain = BlockChain()

blockchain.create_block_from_transaction(["Billys sends 2 CB to Alison"])
blockchain.display_chain()

nb_transaction = 5
print("\n")
for i in range(nb_transaction):
    transaction = f"Block #{i+1}"
    blockchain.create_block_from_transaction([transaction])

blockchain.display_chain()

print(blockchain.is_valid())


for i in range(nb_transaction):
    if(i == 2):
        blockchain.chain[i].transaction_list = ["Billys sends 2 CB to Alison"]
print(blockchain.is_valid())    