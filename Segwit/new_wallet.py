from connect_rpc import get_rpc_connection

# Establish RPC connection
rpc_connection = get_rpc_connection()

# Check if wallet exists and load it if necessary
try:
    wallets = rpc_connection.listwallets()
    if "segwit_wallet" not in wallets:
        rpc_connection.createwallet("segwit_wallet")
        print("✅ Wallet 'segwit_wallet' created successfully!")
    else:
        print("✅ Wallet 'segwit_wallet' already exists!")
    
    rpc_connection.loadwallet("segwit_wallet")
    print("✅ Wallet 'segwit_wallet' loaded!")

except Exception as e:
    if "Wallet file verification failed" in str(e):
        print("⚠️ Wallet already exists on disk.")
    elif "Wallet \"segwit_wallet\" is already loaded" in str(e):
        print("✅ Wallet is already loaded. Proceeding...")
    else:
        print(f"❌ Error: {e}")

