import hashlib

class CoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self._transaction_list = transaction_list
        self.block_data = f"{''.join(self.transaction_list)} : {str(self.previous_block_hash)}"
        self.block_hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256(self.block_data.encode('utf-8')).hexdigest()
    
    @property
    def transaction_list(self):
        return self._transaction_list
    
    @transaction_list.setter
    def transaction_list(self, new_transaction_list):
        self._transaction_list = new_transaction_list
        self.update_block_data()
        self.update_block_hash()

    def update_block_data(self):
        self.block_data = f"{''.join(self._transaction_list)} : {str(self.previous_block_hash)}"

    def update_block_hash(self):
        self.block_hash = self.calculate_hash()

    def __str__(self):
        return f"Hash: {self.block_hash}\nData: {self.block_data}\nPrevious Hash: {self.previous_block_hash}\n"


def new_block(previous_block, transaction_list):
    block_data = f"{''.join(transaction_list)} : {str(previous_block.block_hash)}"
    block = CoinBlock(previous_block.block_hash, transaction_list)
    return block

#init blockChain
genesis_block = CoinBlock("0", [])

#init transaction
transaction_1 = "Billys sends 2 CB to Alison"
genesis_block = new_block(genesis_block, [transaction_1])

print(f"Hash: {genesis_block.block_hash}")
print(f"Data: {genesis_block.block_data}")
print("\n")

#exercice 2.7

nb_transaction = 5

for i in range(nb_transaction):
    transaction = f"Block #{i+1}"
    genesis_block = new_block(genesis_block, genesis_block.transaction_list + [transaction])

#2.8

# La block chain devrait etre cassée car le hash du block 2 devrait etre le hash du block 1
    
#2.13







# def show_blockchain_until_empty(block):
#     current_block = block
#     print(current_block.block_data.split(":"))
#     while current_block and ":" in current_block.block_data.split(":"):
#         print(f"Block Hash: {current_block.block_hash}")
#         print(f"Block Data: {current_block.block_data}")
#         print(f"Previous Block Hash: {current_block.previous_block_hash}")
#         print("\n")
#         current_block = current_block.previous_block_hash

