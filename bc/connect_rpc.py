from bitcoinrpc.authproxy import AuthServiceProxy

# Define RPC connection parameters
rpc_user = "smartcookies"
rpc_password = "smartcookies"
rpc_port = 18443  # Default Regtest port

def get_rpc_connection():
    """Establishes and returns an RPC connection to bitcoind."""
    return AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@localhost:{rpc_port}")

# Test connection when running this script directly
if __name__ == "__main__":
    rpc_connection = get_rpc_connection()
    print("✅ RPC Connection Successful!")
    print("Blockchain Info:", rpc_connection.getblockchaininfo())
