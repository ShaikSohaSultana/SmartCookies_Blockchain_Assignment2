# SmartCookies_Blockchain_Assignment2

# **Bitcoin Transaction Debugging Project**

## **Team Members**
1. **E.Lathika Priya** - 230001026
2. **Shaik Soha Sultana** - 230001071
3. **G.Harshitha** - 230001027


---

## **RPC Connection Process**
This project uses Bitcoin Core’s JSON-RPC API to interact with the Bitcoin network. Follow these steps to establish an RPC connection:

### **1. Configure Bitcoin Core (`bitcoin.conf`)**
Ensure Bitcoin Core is running and configured for RPC access. Add the following lines to your `bitcoin.conf` file:
```ini
server=1
rpcuser=your_rpc_username
rpcpassword=your_rpc_password
rpcallowip=127.0.0.1
rpcport=8332
```

### **2. Start Bitcoin Core with RPC**
Run:
```sh
bitcoind -daemon
```

### **3. Connect to RPC in Python**
A sample `rpc_connection.py` file:
```python
from bitcoinrpc.authproxy import AuthServiceProxy

rpc_user = "your_rpc_username"
rpc_password = "your_rpc_password"

rpc_connection = AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@127.0.0.1:8332")
print(rpc_connection.getblockchaininfo())
```

---

## **Project Structure**
```plaintext
project_folder/
│-- rpc_connection.py  # Handles the RPC connection to Bitcoin Core
│-- send_to_address.py  # Sends Bitcoin to a specified address
│-- send_A_to_B.py # Handles transaction from A to B
|-- send_B_to_C.py # Handles transaction from B to C
│   
│-- README.md  # Documentation
```

### **1. `rpc_connection.py`**
- Establishes a connection with Bitcoin Core.
- Enables interaction with the blockchain.

### **2. `send_to_address.py`**
- Sends funds to a specified address using:
```python
rpc_connection.sendtoaddress("destination_address", amount)
```

### **3. `send_A_to_B.py` and `send_B_to_C.py`**
- Constructs and signs transactions using UTXOs.
- Uses `createrawtransaction`, `signrawtransactionwithwallet`, and `sendrawtransaction`.

---

## **Transaction Flow (A → B → C)**
1. **A to B Transaction:**
   - A sends Bitcoin to B.
   - B’s address is stored as the recipient.
   - The transaction is broadcast to the network.

2. **B to C Transaction:**
   - B uses the received funds to send Bitcoin to C.
   - The previous transaction’s output is used as an input.
   - The transaction is broadcast and confirmed.

---

## **Legacy vs. SegWit Transactions**

### **Legacy Transactions**
- Uses traditional Bitcoin transaction formats (P2PKH, P2SH).
- Stores unlocking data (`scriptSig`) inside the transaction.
- Higher fees due to larger transaction sizes.

Example:
```asm
OP_DUP OP_HASH160 <PubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
```

### **SegWit Transactions**
- Uses segregated witness (P2WPKH, P2WSH) to separate signature data (`witness`).
- Reduces transaction size and fees.
- Enables advanced scripting capabilities.

Example (`scriptPubKey` for P2WPKH):
```asm
0 <PubKeyHash>
```

---

## **Conclusion**
This project demonstrates how to create and send Bitcoin transactions using RPC, including legacy and SegWit formats. It also provides a structured way to debug transaction propagation using tools like `btcdeb` and `bitcoind` logs.

---


