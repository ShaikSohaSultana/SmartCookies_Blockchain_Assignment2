from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# RPC Connection Details (Replace with your actual values)
rpc_user = "smartcookies"
rpc_password = "smartcookies"
rpc_port = 18443  # Regtest port
rpc_url = f"http://{rpc_user}:{rpc_password}@127.0.0.1:{rpc_port}"

try:
    # Connect to bitcoind
    bitcoind = AuthServiceProxy(rpc_url)

    # Address A (Replace with actual generated address)
    address_A = "mfcvYJWpesCurDa4Sxe6RZL5PbwPCHasa9"

    # Send 10 BTC to Address A
    txid = bitcoind.sendtoaddress(address_A, 10)
    
    print(f"Sent 10 BTC to {address_A}")
    print(f"Transaction ID: {txid}")

except JSONRPCException as e:
    print(f"JSON-RPC error: {e}")

except Exception as e:
    print(f"Connection failed: {e}")