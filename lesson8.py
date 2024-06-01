# 1. Instantiate a new Blockchain object called my_blockchain

# 2. Add a new block to my_blockchain and pass in new_transactions as the argument. Print out the contents of my_blockchain to see the new block!

# 3. Select the transactions found in my_blockchain‘s chain attribute. Set the transactions variable of Block 1 to the string "fake_transactions"

# 4. Now let’s check if the blockchain is still valid by calling the correct method on my_blockchain!

from blockchain import Blockchain
from block import Block

new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]


my_blockchain = Blockchain()
my_blockchain.add_block(new_transactions)
#my_blockchain.print_blocks()
my_blockchain.chain[1].transactions = 'fake_transactions'
my_blockchain.validate_chain()