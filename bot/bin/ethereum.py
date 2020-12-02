from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
from sys import exit
from bin import infura_api, account

# contract application binary interface - a sort of contract schema
abi = '[{"inputs":[],"name":"data","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"}]'

# Web3 init
w3 = Web3(Web3.HTTPProvider(infura_api))
# proof-of-authority from geth, for a better compatibility
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

last_block = w3.eth.blockNumber
  
# iterating backward over blocks looking for last transaction of specified account
for i in range(last_block,-1,-1):
	block = w3.eth.getBlock(i, full_transactions=True)# ; print(i)
	
	for t in block.transactions:
		if t['from'] == account:
	
			t_hash = t['hash'].hex()
			t_receipt = w3.eth.getTransactionReceipt(t_hash)

			c_address = t_receipt['contractAddress'] # None if it is not a contract
			
			# once we get the address, we can build the actual contract and call its function
			contract = w3.eth.contract(address = c_address, abi = abi)
			ip =  contract.functions.data().call()

			print(ip)

			exit(0)