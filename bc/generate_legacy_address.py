from connect_rpc import get_rpc_connection

rpc_connection = get_rpc_connection()

addr_A = rpc_connection.getnewaddress("", "p2sh-segwit")
addr_B = rpc_connection.getnewaddress("", "p2sh-segwit")
addr_C = rpc_connection.getnewaddress("", "p2sh-segwit")

print(f"✅ Address A': {addr_A}")
print(f"✅ Address B': {addr_B}")
print(f"✅ Address C': {addr_C}")
