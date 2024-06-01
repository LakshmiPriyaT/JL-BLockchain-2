transaction1 = {
  'amount': '30',
  'sender': 'Alice',
  'receiver': 'Bob'}
transaction2 = { 
  'amount': '200',
  'sender': 'Bob',
  'receiver': 'Alice'}
transaction3 = { 
  'amount': '300',
  'sender': 'Alice',
  'receiver': 'Timothy' }
transaction4 = { 
  'amount': '300',
  'sender': 'Rodrigo',
  'receiver': 'Thomas' }
transaction5 = { 
  'amount': '200',
  'sender': 'Timothy',
  'receiver': 'Thomas' }
transaction6 = { 
  'amount': '400',
  'sender': 'Tiffany',
  'receiver': 'Xavier' }
mempool = [transaction1, transaction2, transaction3, transaction4, transaction5, transaction6]

# 1. Let’s create a transaction and add it to the mempool. Name the new transaction my_transaction and add amount, sender, and receiver as key-values.

transaction1 = {
  'amount': '30',
  'sender': 'Alice',
  'receiver': 'Bob'}
transaction2 = { 
  'amount': '200',
  'sender': 'Bob',
  'receiver': 'Alice'}
transaction3 = { 
  'amount': '300',
  'sender': 'Alice',
  'receiver': 'Timothy' }
transaction4 = { 
  'amount': '300',
  'sender': 'Rodrigo',
  'receiver': 'Thomas' }
transaction5 = { 
  'amount': '200',
  'sender': 'Timothy',
  'receiver': 'Thomas' }
transaction6 = { 
  'amount': '400',
  'sender': 'Tiffany',
  'receiver': 'Xavier' }
my_transaction = {
  'amount' : '2500',
  "sender" : "Arindam",
  "receiver" : "Bhowmick"
  }
print(my_transaction)
print("\n")
# 2. Add my_transaction to the mempool list

mempool = [transaction1, transaction2, transaction3, transaction4, transaction5, transaction6, my_transaction]
print(mempool)
print("\n")

# 3. Create a new list called block_transactions and add three transactions from the mempool list. This will allow us to prepare the transactions to be added to our future Block structure.
block_transactions = [transaction1, transaction2, transaction3]
print(block_transactions)















