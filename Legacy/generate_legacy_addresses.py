from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# Connect to bitcoind
rpc_user = "smartcookies"
rpc_password = "smartcookies"
rpc_port = 18443  # Regtest port
rpc_url = f"http://{rpc_user}:{rpc_password}@127.0.0.1:{rpc_port}"

try:
    # Establish RPC connection
    bitcoind = AuthServiceProxy(rpc_url)

    # Generate three legacy (P2PKH) addresses
    address_A = bitcoind.getnewaddress("", "legacy")
    address_B = bitcoind.getnewaddress("", "legacy")
    address_C = bitcoind.getnewaddress("", "legacy")

    # Print the addresses
    print(f"Address A: {address_A}")
    print(f"Address B: {address_B}")
    print(f"Address C: {address_C}")

except JSONRPCException as e:
    print(f"JSON-RPC error: {e}")

except Exception as e:
    print(f"Connection failed: {e}")