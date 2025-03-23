from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from decimal import Decimal

# RPC Connection Details
rpc_user = "smartcookies"
rpc_password = "smartcookies"
rpc_port = 18443
rpc_url = f"http://{rpc_user}:{rpc_password}@127.0.0.1:{rpc_port}/wallet/mywallet"

try:
    # Connect to bitcoind
    bitcoind = AuthServiceProxy(rpc_url)

    # Define transaction details
    address_A = "mrAvE3VbaHnpquTiNNUruY4LjSzWViJoY8"  # Correct funding address
    address_B = "n3qmuq1eKHk4XsWYmyqFCjdeMJAWwap1se"  # Receiver

    # Get UTXOs for Address A
    utxos_A = bitcoind.listunspent(0, 9999999, [address_A])

    # Ensure there are UTXOs available
    if not utxos_A:
        raise Exception(f"No spendable UTXOs found for Address A ({address_A}). Fund the address first.")

    # Use the first available UTXO
    utxo_A = utxos_A[0]
    txid_A = utxo_A["txid"]
    vout_A = utxo_A["vout"]
    available_balance = Decimal(utxo_A["amount"])

    # Set transaction fee
    fee = Decimal("0.00001")

    # Calculate amount to send
    send_amount = available_balance - fee

    if send_amount <= 0:
        raise Exception(f"Insufficient funds. Available: {available_balance}, Fee: {fee}")

    # Create the raw transaction
    raw_tx = bitcoind.createrawtransaction(
        [{"txid": txid_A, "vout": vout_A}],  # Input UTXO
        {address_B: float(send_amount)}  # Output to Address B minus fee
    )

    print("Raw Transaction (Unsigned):", raw_tx)

    # Sign the raw transaction
    signed_tx = bitcoind.signrawtransactionwithwallet(raw_tx)

    # Check if signing was successful
    if not signed_tx.get("complete", False):
        raise Exception("Transaction signing failed.")

    # Broadcast the signed transaction
    txid_B = bitcoind.sendrawtransaction(signed_tx["hex"])

    print(f"Transaction successfully sent! TXID: {txid_B}")

except JSONRPCException as e:
    print(f"JSON-RPC error: {e}")

except Exception as e:
    print(f"Error: {e}")