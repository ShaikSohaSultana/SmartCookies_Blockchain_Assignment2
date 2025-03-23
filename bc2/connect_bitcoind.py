from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# Configuration (use your credentials from bitcoin.conf)
rpc_user = "smartcookies"
rpc_password = "smartcookies"
rpc_port = 18443  # Regtest port

# Connect to bitcoind using JSON-RPC
rpc_url = f"http://{rpc_user}:{rpc_password}@127.0.0.1:{rpc_port}"
try:
    rpc_connection = AuthServiceProxy(rpc_url)

    # Test connection: get blockchain info
    blockchain_info = rpc_connection.getblockchaininfo()
    print("Connected to bitcoind successfully!")
    print("Blockchain Info:", blockchain_info)

except JSONRPCException as e:
    print(f"JSON-RPC error: {e}")

except Exception as e:
    print(f"Connection failed: {e}")