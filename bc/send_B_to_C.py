from bitcoinrpc.authproxy import AuthServiceProxy

# Configure RPC connection
rpc_user = "smartcookies"
rpc_password = "smartcookies"
rpc_connection = AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@127.0.0.1:18443")

# Define addresses
address_B = "2N7cMLw3VppE3MuAwZVRrtiKJjpQzJGhHnz"
address_C = "2N6sAQwvv4V8c1BJ6juirCSZAmvgMomPw5q"

# Get UTXO from Address B
utxos = rpc_connection.listunspent(1, 9999999, [address_B])

if not utxos:
    print("No UTXOs found for Address B. Ensure it has funds.")
    exit()

utxo = utxos[0]  # Use the first UTXO
txid = utxo['txid']
vout = utxo['vout']
amount = utxo['amount']

# Transaction fee
tx_fee = 0.0001

# Create raw transaction
raw_tx = rpc_connection.createrawtransaction(
    [{"txid": txid, "vout": vout}],
    {address_C: float(amount) - tx_fee}  # Convert Decimal to float
)

# Sign transaction
signed_tx = rpc_connection.signrawtransactionwithwallet(raw_tx)
signed_hex = signed_tx['hex']

# Broadcast transaction
txid_C = rpc_connection.sendrawtransaction(signed_hex)
print(f"Transaction B' → C' broadcasted with txid: {txid_C}")

