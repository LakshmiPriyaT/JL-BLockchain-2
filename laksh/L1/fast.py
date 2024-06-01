from web3 import Web3
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
print(w3.is_connected())
if w3.is_connected():
    print("Transaction Initiated")
else:
    print("Please open your ganache to see the results")

def balance(address):
    balance = w3.eth.get_balance(address)
    balance_eth = w3.from_wei(balance,"ether")
    print ("The balance of account " + address + " is " +str (balance_eth) +"ether")

#public key of accl

acc1="0x3ec8E2D4Aa50eB9ea5E0ffE887cCD38baf4A3e4C"

#private key of accl

acc1_pk="0x75f878980ac915bf1848023a8fe7e945a73e08b8fd363c283184e761742e67c9"

#public key of acc2

acc2="0xb82288B847B39f75B94DC533E013330643ea18Cf"
balance(acc1)
balance(acc2)
nonce=w3.eth.get_transaction_count(acc1)
tx={
    'nonce':nonce,
    'to': acc2,
    'value':w3.to_wei(10,'ether'),
    'gas':200000,
    'gasPrice':w3.to_wei(50,'gwei')
}
print(tx)


#step2
signed_tx=w3.eth.account.sign_transaction(tx,acc1_pk)


#step3
tx_hash=w3.eth.send_raw_transaction(signed_tx.rawTransaction)


print(w3.to_hex(tx_hash))




balance(acc1)
balance(acc2)
