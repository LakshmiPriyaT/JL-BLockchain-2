import hashlib


#to create a hash


#print(hashlib.sha256("Hello world".encode()).hexdigest())
NONCE_LIMIT=1000000000000
zeroes=4


def mine(block_number,transactions,previous_hash):
    for nonce in range(NONCE_LIMIT):
        base_text=str(block_number)+transactions+previous_hash+str(nonce)
        hash_try=hashlib.sha256(base_text.encode()).hexdigest()
        if hash_try.startswith('0'*zeroes):
            print(f"Found Hash With Nonce: {nonce}")
            return hash_try
       
    return -1
block_number=24
transaction="76123fcc2142"
previous_hash="876de8756b967c87"


combined_text=str(block_number)+transaction+previous_hash+str(107617)
print(hashlib.sha256(combined_text.encode()).hexdigest())


mine(block_number, transaction, previous_hash)
