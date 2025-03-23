from bitcoinrpc.authproxy import AuthServiceProxy

# Configure RPC connection
rpc_user = "smartcookies"
rpc_password = "smartcookies"
rpc_connection = AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@127.0.0.1:18443")

# Address to check
address_B = "2N6sAQwvv4V8c1BJ6juirCSZAmvgMomPw5q"

# Get unspent transactions
utxos = rpc_connection.listunspent(1, 9999999, [address_B])

# Calculate balance
balance = sum(float(utxo["amount"]) for utxo in utxos)
print(f"Balance for {address_B}: {balance} BTC")

