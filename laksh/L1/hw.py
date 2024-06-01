from web3 import Web3
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))


account1 = '0x4806F886c4487F74Be70EeeAA83A7F5f4Cbc085F'
account2 = '0x49913ad245e62B3A682bB4903a3cfBA0f9a66DdE'

w3.eth.send_transaction({
"from": account1,
"to": account2,
"value": w3.to_wei('5','ether')
})