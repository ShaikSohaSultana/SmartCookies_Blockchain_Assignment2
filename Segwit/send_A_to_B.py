from bitcoinrpc.authproxy import AuthServiceProxy

# Configure RPC connection
rpc_user = "smartcookies"
rpc_password = "smartcookies"
rpc_connection = AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@127.0.0.1:18443")

# Define addresses
address_A = "2MzwTXeTFxokmKapzhUqtHqaXDuwS85mBVP"
address_B = "2N7cMLw3VppE3MuAwZVRrtiKJjpQzJGhHnz"

# Get UTXO from Address A
utxos = rpc_connection.listunspent(1, 9999999, [address_A])

if not utxos:
    print("No UTXOs found for Address A. Ensure it has funds.")
    exit()

utxo = utxos[0]  # Use the first UTXO
txid = utxo['txid']
vout = utxo['vout']
amount = utxo['amount']

# Create raw transaction
tx_fee = 0.0001
raw_tx = rpc_connection.createrawtransaction(
    [{"txid": txid, "vout": vout}],
    {address_B: float(amount) - tx_fee}  # Convert Decimal to float

)

# Sign transaction
signed_tx = rpc_connection.signrawtransactionwithwallet(raw_tx)
signed_hex = signed_tx['hex']

# Broadcast transaction
txid_B = rpc_connection.sendrawtransaction(signed_hex)
print(f"Transaction A' → B' broadcasted with txid: {txid_B}")


