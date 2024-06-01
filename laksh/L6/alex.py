import hashlib
import datetime

class Block:
    block_nr=0
    data=None
    next_b=None
    hash=None
    nonce=0
    prev_hash=0x0
    timestamp=datetime.datetime.now()
    
    def __init__(self,data):
        self.data=data
    def hash(self):
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode("utf-8")+
            str(self.data).encode("utf-8")+
            str(self.prev_hash).encode("utf-8")+
            str(self.timestamp).encode("utf-8")+
            str(self.block_nr).encode("utf-8")
        )
        return h.hexdigest()
    def __str__(self):
        return "Block Hash:"+str(self.hash())+"\nBlockNo:"+str(self.block_nr)+"\nBlockData :"+str(self.data)+"\nNonce:"+str(self.nonce)+"\n--------"

class Blockchain:
    #By increasing the difficulty, we effectively decrease the target range. Decreasing the target range makes it harder to
    #mine a block, which is useful when dealing with a network that has many nodes working to find the acceptable hash
    diff=20
    #maximum nonce, set to 2 to the power of 32, which is the maximum number that can be stored in a 32-bit number. 
    #The nonce must be less than the target number to be accepted
    max_nonce=2**32
    #target number, set to 2 to the power of 256 minus the difficulty. In this case, the difficulty is 20
    target=2**(256-diff)

    block=Block("Genesis")
    #The start of any linked list is called the head. Since the head of our linked list is the Genesis block,
    #we write that down in code as head = block.A random variable must be written before the head variable 
    #(in this case, dummy), to tell the computer that head does not point to the same object as block
    dummy=head=block

    def addblock(self,block):
        block.prev_hash=self.block.hash()
        block.block_nr=self.block.block_nr+1
        self.block.next_b=block
        self.block=self.block.next_b
    def mine(self,block):
        for n in range(self.max_nonce):
            
            if int(block.hash(),16)<=self.target:
                self.addblock(block)
                print(block)
                break
            else:
                block.nonce +=1
blockchain=Blockchain()

for i in range(10):
    blockchain.mine(Block("Block"+str(i+1)))
while blockchain.head != None:
    print(blockchain.head)
    blockchain.head=blockchain.head.next_b
