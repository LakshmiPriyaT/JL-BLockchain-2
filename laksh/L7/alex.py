import hashlib
from time import time
class Blockchain():
    def __init__(self):
        self.blocks=[]
        self.secret=""
        self.difficulty=4
        self.nonce=0
        secret_string="efee"
        while True:
            _hash=hashlib.sha256((str(self.nonce)+secret_string).encode()).hexdigest()
            #print(_hash)
            if (_hash[:self.difficulty]=="0"*self.difficulty):
                self.secret=_hash
                break
            self.nonce+=1
    def createblock(self,sender:str, information:str):
        block={
            "index":len(self.blocks),
            "sender":sender,
            "timestamp":time(),
            "info":information
        }
        if block["index"]==0:
            block["prev_hash"]=self.secret
        else:
            block["prev_hash"]=self.blocks[-1]["hash"]
        i=0

        while True:
            block['nonce'] = i
            _hash=hashlib.sha256(str(block).encode()).hexdigest()
            if (_hash[:self.difficulty]=="0"*self.difficulty):
                block["hash"]=_hash
                break
            i+=1
        self.blocks.append(block)
        print("Blocks successfully created")
    def show_blocks(self):
        for block in self.blocks:
            print(block)
            print("/n")

block1=Blockchain()
block2=Blockchain()
block3=Blockchain()
block4=Blockchain()
block5=Blockchain()

print(block1.blocks)

block1.createblock("sender1","information1")
block2.createblock("sender2","information2")
block3.createblock("sender3","information3")
block4.createblock("sender4","information4")
block5.createblock("sender5","information5")

block1.show_blocks()
print(block1.blocks)


#show the blocks
