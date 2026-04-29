# 🌊 Base Chain Transaction Monitor

A simple, human-friendly Python script to monitor real-time transactions on the Base blockchain

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Base](https://img.shields.io/badge/Base-Mainnet-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🎯 Features

- **Real-time monitoring**: Watch Base chain transactions as they happen
- **Address tracking**: Monitor specific wallet addresses
- **Transaction lookup**: Get details about any transaction by hash
- **Human-readable output**: Clean, emoji-enhanced terminal interface
- **No API key required**: Uses public Base RPC endpoint

##  Requirements

- Python 3.7 or higher
- `requests` library

##  Installation

1. Clone this repository:
```bash
git clone https://github.com/Richardweb1/base-transaction-monitor.git
cd base-transaction-monitor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

Run the script:
```bash
python base_monitor.py
```

You'll see an interactive menu with 4 options:

### Option 1: Monitor Recent Transactions
Monitors the Base blockchain for 60 seconds and displays all transactions with value > 0

```
🚀 Base Chain Transaction Monitor Started!
⏰ Monitoring for 60 seconds...
==========================================================================

📦 Block #12345678 | 2026-04-23 14:30:45
   Transactions: 15

   💰 Transaction 1:
      Hash: 0xabc123...
      From: 0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb
      To:   0x1234567890123456789012345678901234567890
      Value: 0.050000 ETH
      Gas Price: 0.25 Gwei
```

### Option 2: Track a Specific Address
Enter any Base address to monitor all incoming and outgoing transactions

```
Enter the address to track: 0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb

🔍 Tracking address: 0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb
⏰ Monitoring for 60 seconds...
```

### Option 3: Get Current Block Number
Shows the latest block number on Base chain

```
📊 Current Base block number: #12,345,678
```

### Option 4: Look Up a Transaction
Enter a transaction hash to see full details

```
Enter transaction hash: 0xabc123def456...

📝 Transaction Details:
{
  "hash": "0xabc123def456...",
  "from": "0x742d35Cc...",
  "to": "0x123456...",
  ...
}
```

## 🔧 Customization

You can easily customize the script:

**Change monitoring duration:**
```python
monitor.monitor_transactions(duration_seconds=120)  # Monitor for 2 minutes
```

**Use a different RPC endpoint:**
```python
self.rpc_url = "https://base-mainnet.g.alchemy.com/v2/YOUR_API_KEY"
```

**Filter by transaction value:**
```python
# In format_transaction(), change the threshold
if value_in_eth < 0.1:  # Only show transactions > 0.1 ETH
    return None
```

## 📊 What You'll Learn

Building this project teaches you:

- ✅ How to interact with blockchain RPC endpoints
- ✅ Understanding blockchain data structures (blocks, transactions)
- ✅ Making HTTP requests to blockchain APIs
- ✅ Converting between hex and decimal numbers
- ✅ Working with timestamps and formatting data
- ✅ Building command-line interfaces in Python

## 🌐 Base Chain Information

- **Network**: Base Mainnet (Layer 2 on Ethereum)
- **Block time**: ~2 seconds
- **RPC Endpoint**: https://mainnet.base.org
- **Explorer**: https://basescan.org

## 🛡️ Safety Notes

- This script only **reads** blockchain data - it cannot send transactions
- No private keys or wallet connections required
- All data is publicly available on the blockchain
- Safe to run and share publicly

## 🚀 Future Improvements

Ideas to extend this project:

- [ ] Add webhook notifications (Discord, Telegram)
- [ ] Save transactions to a database
- [ ] Create a web dashboard with Flask
- [ ] Add filters for contract interactions
- [ ] Track token transfers (ERC-20)
- [ ] Monitor gas prices and suggest optimal transaction times
- [ ] Add support for Base Testnet (Sepolia)

## 📝 License

MIT License - feel free to use this for learning and portfolio projects!

## 👨‍💻 Author

Created by **Richardweb1**

## 🤝 Contributing

Feel free to open issues or submit pull requests!

---

**⭐ If you found this helpful, please star the repository!*
