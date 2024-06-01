import hashlib  
from time import time


class blockchain():
    def __init__(self):
        self.blocks = []
        """ the secret variable will be used for building the previous hash for the genesis block"""
        self.__secret = ''
        self.__difficulty = 4 
        # guessing the nonce
        nonce = 0
        secret_string = '/*SECRET*/'
        while True:
            _hash = hashlib.sha256(str(secret_string+str(nonce)).encode('utf-8')).hexdigest()
            if(_hash[:self.__difficulty] == '0'*self.__difficulty):
                self.__secret = _hash
                break
            nonce+=1
    def create_block(self, sender:str, information:str):
        block = {
            'index': len(self.blocks),
            'sender': sender,
            'timestamp': time(),
            'info': information
        }
        if(block['index'] == 0): 
            block['previous_hash'] = self.__secret # for genesis block
        else: 
            block['previous_hash'] = self.blocks[-1]['hash']
        # guessing the nonce
        i = 0
        while True:
            block['nonce'] = i
            _hash = hashlib.sha256(str(block).encode('utf-8')).hexdigest()
            if(_hash[:self.__difficulty] == '0'*self.__difficulty):
                block['hash'] = _hash
                break
            i+=1
        self.blocks.append(block)
    def validate_blockchain(self):
        valid = True
        n = len(self.blocks)-1
        i = 0
        while(i<n):
            if(self.blocks[i]['hash'] != self.blocks[i+1]['previous_hash']):
                valid = False
                break
            i+=1
        if valid: 
            print('The blockchain is valid...')
        else: 
            print('The blockchain is not valid...')
    def show_blockchain(self):
        for block in self.blocks: 
            print(block)

b = blockchain()
b.create_block('Ram', 'Python is the best programming language!!')
b.create_block('Vishnu', 'I love cybersecurity')
b.create_block('Sanjay', 'AI is the future')
b.show_blockchain()
b.validate_blockchain()