from connect_rpc import get_rpc_connection

rpc_connection = get_rpc_connection()

# Mine blocks to get test BTC
print("⛏️  Mining 101 blocks...")
miner_address = rpc_connection.getnewaddress()
rpc_connection.generatetoaddress(101, miner_address)

# Send 1 BTC to A'
addr_A = input("Enter Address A': ")
txid_funding = rpc_connection.sendtoaddress(addr_A, 20)
print(f"✅ Funded Address A' with TXID: {txid_funding}")
