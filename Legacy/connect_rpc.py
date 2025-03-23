from bitcoinrpc.authproxy import AuthServiceProxy

rpc_user = "smartcookies"
rpc_password = "smartcookies"
rpc_url = f"http://{rpc_user}:{rpc_password}@127.0.0.1:18443"

rpc_connection = AuthServiceProxy(rpc_url)
print(rpc_connection.getblockchaininfo())