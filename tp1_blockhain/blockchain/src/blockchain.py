from coinBlock import CoinBlock

class BlockChain:
    def __init__(self, chain=None):
        if chain is None:
            self.chain = [self.generate_genesis_block()]
        else:
            self.chain = [chain]

    def generate_genesis_block(self):
        return CoinBlock("0", ["Genesis Block"])

    def create_block_from_transaction(self, transaction_list):
        block = CoinBlock(self.chain[-1].block_hash, transaction_list)
        self.chain.append(block)
        return block

    def display_chain(self):
        for block in self.chain:
            print(block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.previous_block_hash != previous_block.block_hash:
                return False

            if current_block.block_hash != current_block.calculate_hash():
                return False

        return True

