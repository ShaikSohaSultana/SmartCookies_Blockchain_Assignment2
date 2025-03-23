from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from decimal import Decimal

# RPC Connection Details
rpc_user = "smartcookies"  # Replace with actual RPC username
rpc_password = "smartcookies"  # Replace with actual RPC password
rpc_port = 18443  # Regtest port
rpc_url = f"http://{rpc_user}:{rpc_password}@127.0.0.1:{rpc_port}/wallet/mywallet"

try:
    # Connect to bitcoind
    bitcoind = AuthServiceProxy(rpc_url)

    # Addresses
    address_B = "n3qmuq1eKHk4XsWYmyqFCjdeMJAWwap1se"  # Sender (B)
    address_C = "mtwdKZ3i5iEKPo8Ks82DxuZEwS2uWEVsHD"  # Receiver (C) - Replace with actual

    # Get UTXO for Address B
    unspent_B = bitcoind.listunspent(0, 9999999, [address_B])
    
    if not unspent_B:
        raise Exception("No UTXOs available for Address B!")

    # Use first UTXO
    utxo_B = unspent_B[0]
    txid_B = utxo_B["txid"]
    vout_B = utxo_B["vout"]
    amount_B = Decimal(utxo_B["amount"])  # Convert to Decimal

    # Set transaction fee
    fee = Decimal("0.0001")  # Use Decimal for precision

    # Calculate the amount to send (avoid floating-point errors)
    send_amount = amount_B - fee
    send_amount = send_amount.quantize(Decimal("0.00000001"))  # Round to 8 decimal places

    # Print debug info
    print(f"Amount_B: {amount_B}, Fee: {fee}, Send Amount: {send_amount}")

    # Create the raw transaction
    raw_tx_B_to_C = bitcoind.createrawtransaction(
        [{"txid": txid_B, "vout": vout_B}],  # Input (UTXO from B)
        {address_C: float(send_amount)}  # Output (sending BTC to C minus the fee)
    )

    print("Raw Transaction (Unsigned):", raw_tx_B_to_C)

    # Sign the raw transaction
    signed_tx_B_to_C = bitcoind.signrawtransactionwithwallet(raw_tx_B_to_C)

    # Broadcast the signed transaction
    txid_B_to_C = bitcoind.sendrawtransaction(signed_tx_B_to_C["hex"])
    print("Signed Transaction HEX:", signed_tx_B_to_C["hex"])

    print(f"Transaction successfully sent! TXID: {txid_B_to_C}")

except JSONRPCException as e:
    print(f"JSON-RPC error: {e}")

except Exception as e:
    print(f"Error: {e}")