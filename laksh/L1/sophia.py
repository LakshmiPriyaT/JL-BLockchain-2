from web3 import Web3 
W3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
print(W3.is_connected())

def balance (adress):
    BAL = W3.eth.get_balance(adress)
    BAL_eth=W3.from_wei(BAL,'ether')
    print ('the balance is ',BAL_eth)




Account_1 = '0x5367248ee2eeE01e69a2cDb0a2A12D4b31C66769'
Account_2 = '0x0a3c7f79E78A1FD88E5Ee838507a54E56922d72A'
Account_1_PK = '0x2fb759a96310bd3876b8ff23e8b3bed5ec4159dfaa06865af1598464310eeda5'
nonce=W3.eth.get_transaction_count(Account_1)
transaction = {
    'nonce':nonce,
    'to':Account_2,
    'value':W3.to_wei(5,'ether'),
    'gas':200000,
    'gasPrice': W3.to_wei(5,'gwei'),

}

sign_Tran=W3.eth.account.sign_transaction(transaction,Account_1_PK)
transactionHASH=W3.eth.send_raw_transaction(sign_Tran.rawTransaction)
balance(Account_1)
balance(Account_2)