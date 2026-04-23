#!/usr/bin/env python3
"""
Base Chain Transaction Monitor
A simple, human-friendly script to monitor transactions on Base blockchain
Author: Richardweb1
"""

import requests
import time
from datetime import datetime
import json

class BaseTransactionMonitor:
    def __init__(self):
        # Base Mainnet RPC endpoint (you can use this free one or get your own from Alchemy/Infura)
        self.rpc_url = "https://mainnet.base.org"
        self.last_block = None
        
    def get_latest_block_number(self):
        """Get the latest block number from Base chain"""
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_blockNumber",
            "params": [],
            "id": 1
        }
        
        try:
            response = requests.post(self.rpc_url, json=payload, timeout=10)
            result = response.json()
            # Convert hex to decimal
            block_number = int(result['result'], 16)
            return block_number
        except Exception as e:
            print(f"❌ Error getting block number: {e}")
            return None
    
    def get_block_details(self, block_number):
        """Get detailed information about a specific block"""
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_getBlockByNumber",
            "params": [hex(block_number), True],  # True = include full transaction objects
            "id": 1
        }
        
        try:
            response = requests.post(self.rpc_url, json=payload, timeout=10)
            result = response.json()
            return result.get('result')
        except Exception as e:
            print(f"❌ Error getting block details: {e}")
            return None
    
    def format_transaction(self, tx):
        """Format transaction data in a human-readable way"""
        # Convert Wei to ETH (divide by 10^18)
        value_in_eth = int(tx['value'], 16) / 1e18
        
        # Only show transactions with value > 0 to reduce noise
        if value_in_eth == 0:
            return None
            
        return {
            'hash': tx['hash'],
            'from': tx['from'],
            'to': tx.get('to', 'Contract Creation'),
            'value': f"{value_in_eth:.6f} ETH",
            'gas_price': int(tx['gasPrice'], 16) / 1e9,  # Convert to Gwei
        }
    
    def monitor_transactions(self, duration_seconds=60):
        """
        Monitor Base chain transactions in real-time
        
        Args:
            duration_seconds: How long to monitor (default: 60 seconds)
        """
        print("🚀 Base Chain Transaction Monitor Started!")
        print(f"⏰ Monitoring for {duration_seconds} seconds...")
        print("=" * 80)
        
        start_time = time.time()
        transaction_count = 0
        
        while time.time() - start_time < duration_seconds:
            current_block = self.get_latest_block_number()
            
            if current_block is None:
                time.sleep(2)
                continue
            
            # Check if we have a new block
            if self.last_block is None or current_block > self.last_block:
                if self.last_block is not None:
                    # Process all blocks we might have missed
                    for block_num in range(self.last_block + 1, current_block + 1):
                        block_data = self.get_block_details(block_num)
                        
                        if block_data and block_data.get('transactions'):
                            timestamp = datetime.fromtimestamp(int(block_data['timestamp'], 16))
                            print(f"\n📦 Block #{block_num} | {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
                            print(f"   Transactions: {len(block_data['transactions'])}")
                            
                            # Show transactions with value
                            for tx in block_data['transactions']:
                                formatted_tx = self.format_transaction(tx)
                                if formatted_tx:
                                    transaction_count += 1
                                    print(f"\n   💰 Transaction {transaction_count}:")
                                    print(f"      Hash: {formatted_tx['hash']}")
                                    print(f"      From: {formatted_tx['from']}")
                                    print(f"      To:   {formatted_tx['to']}")
                                    print(f"      Value: {formatted_tx['value']}")
                                    print(f"      Gas Price: {formatted_tx['gas_price']:.2f} Gwei")
                
                self.last_block = current_block
            
            # Wait a bit before checking again (Base blocks are ~2 seconds)
            time.sleep(2)
        
        print("\n" + "=" * 80)
        print(f"✅ Monitoring complete! Found {transaction_count} transactions with value > 0")
    
    def get_transaction_details(self, tx_hash):
        """Get details of a specific transaction by hash"""
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_getTransactionByHash",
            "params": [tx_hash],
            "id": 1
        }
        
        try:
            response = requests.post(self.rpc_url, json=payload, timeout=10)
            result = response.json()
            return result.get('result')
        except Exception as e:
            print(f"❌ Error getting transaction: {e}")
            return None
    
    def track_address(self, address, duration_seconds=60):
        """
        Track transactions for a specific address
        
        Args:
            address: Ethereum address to track
            duration_seconds: How long to monitor
        """
        print(f"🔍 Tracking address: {address}")
        print(f"⏰ Monitoring for {duration_seconds} seconds...")
        print("=" * 80)
        
        start_time = time.time()
        found_count = 0
        
        while time.time() - start_time < duration_seconds:
            current_block = self.get_latest_block_number()
            
            if current_block and (self.last_block is None or current_block > self.last_block):
                if self.last_block is not None:
                    for block_num in range(self.last_block + 1, current_block + 1):
                        block_data = self.get_block_details(block_num)
                        
                        if block_data and block_data.get('transactions'):
                            for tx in block_data['transactions']:
                                # Check if address is sender or receiver
                                if tx['from'].lower() == address.lower() or \
                                   (tx.get('to') and tx['to'].lower() == address.lower()):
                                    found_count += 1
                                    formatted_tx = self.format_transaction(tx)
                                    
                                    print(f"\n🎯 Found transaction #{found_count}!")
                                    print(f"   Block: #{block_num}")
                                    print(f"   Hash: {tx['hash']}")
                                    print(f"   From: {tx['from']}")
                                    print(f"   To: {tx.get('to', 'Contract Creation')}")
                                    
                                    if formatted_tx:
                                        print(f"   Value: {formatted_tx['value']}")
                
                self.last_block = current_block
            
            time.sleep(2)
        
        print("\n" + "=" * 80)
        print(f"✅ Tracking complete! Found {found_count} transactions for this address")


def main():
    """Main function with interactive menu"""
    monitor = BaseTransactionMonitor()
    
    print("\n" + "=" * 80)
    print("🌊 BASE CHAIN TRANSACTION MONITOR")
    print("=" * 80)
    print("\nChoose an option:")
    print("1. Monitor recent transactions (60 seconds)")
    print("2. Track a specific address")
    print("3. Get current block number")
    print("4. Look up a transaction by hash")
    print("\n")
    
    choice = input("Enter your choice (1-4): ").strip()
    
    if choice == "1":
        print("\n")
        monitor.monitor_transactions(duration_seconds=60)
    
    elif choice == "2":
        address = input("\nEnter the address to track: ").strip()
        if address.startswith('0x') and len(address) == 42:
            print("\n")
            monitor.track_address(address, duration_seconds=60)
        else:
            print("❌ Invalid address format. Should start with 0x and be 42 characters long.")
    
    elif choice == "3":
        block_num = monitor.get_latest_block_number()
        if block_num:
            print(f"\n📊 Current Base block number: #{block_num:,}")
    
    elif choice == "4":
        tx_hash = input("\nEnter transaction hash: ").strip()
        if tx_hash.startswith('0x'):
            tx_data = monitor.get_transaction_details(tx_hash)
            if tx_data:
                print("\n📝 Transaction Details:")
                print(json.dumps(tx_data, indent=2))
            else:
                print("❌ Transaction not found")
        else:
            print("❌ Invalid transaction hash. Should start with 0x")
    
    else:
        print("❌ Invalid choice!")


if __name__ == "__main__":
    main()
