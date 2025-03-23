from connect_rpc import get_rpc_connection

rpc_connection = get_rpc_connection()

recipient = input("Enter recipient address: ")
amount = float(input("Enter amount to send: "))

txid = rpc_connection.sendtoaddress(recipient, amount)
print(f"✅ Sent {amount} BTC to {recipient} with TXID: {txid}")
