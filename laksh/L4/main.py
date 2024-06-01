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
block_number=20
transaction="38a6391d59bd76392c93821c4d13f4f78e6d8c0579c1139b50f5a418cf79df4c"
previous_hash="000012fa9b916eb9078f8d98a7864e697ae83ed54f5146bd84452cdafd043c19"

mine(block_number, transaction, previous_hash)
combined_text=str(block_number)+transaction+previous_hash+str(99687)
print(hashlib.sha256(combined_text.encode()).hexdigest())



