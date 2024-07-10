import bitcoinlib
from bitcoinlib.wallets import Wallet, wallet_delete
from bitcoinlib.keys import Key

# Replace these values with your actual data
source_address = 'xxxxxxxxxxxxxxxxxxxx'
source_private_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
destination_address = '3KgiK7FdnEHpBDt3uie9mU1QRnVN8sP81o'
amount_satoshis = 10000  # amount to send in satoshis (1 BTC = 100,000,000 satoshis)
fee = 1000  # transaction fee in satoshis

# Create a new wallet with the source private key
wallet_name = 'temp_wallet'

# Ensure the wallet does not already exist
try:
    wallet_delete(wallet_name)
except bitcoinlib.wallets.WalletError:
    print(f"Wallet '{wallet_name}' not found, continuing with creation.")

wallet = Wallet.create(wallet_name, keys=source_private_key)

# Create a new transaction
tx = wallet.transaction_create([(destination_address, amount_satoshis)], fee=fee)

# Sign the transaction
tx.sign()

# Broadcast the transaction to the Bitcoin network
tx.send()

print(f'Transaction created and sent. TXID: {tx.txid}')
