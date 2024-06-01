# 1. Inside the .proof_of_work() method, create a local variable proof and assign it the block’s hash.

# 2. Finish the rest of the method by creating a loop that increments the nonce value until the hash with the required difficulty has been generated. After finding the correct hash, set the value of the block.nonce back to 0 and return the correct hash outside of the loop.

from block import Block
from blockchain import Blockchain


def proof_of_work(self,block, difficulty=2):
    proof = block.generate_hash()
    while proof[:difficulty] != '0'*difficulty:
      block.nonce += 1
      proof = block.generate_hash()
    block.nonce = 0
    return proof