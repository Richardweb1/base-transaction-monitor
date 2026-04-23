#!/usr/bin/env python3
"""
Example usage scenarios for Base Transaction Monitor
"""

from base_monitor import BaseTransactionMonitor
import time

def example_1_quick_check():
    """Quick check of current block"""
    print("\n" + "="*60)
    print("EXAMPLE 1: Quick Block Check")
    print("="*60)
    
    monitor = BaseTransactionMonitor()
    block_num = monitor.get_latest_block_number()
    print(f"✅ Current Base block: #{block_num:,}")
    time.sleep(2)

def example_2_short_monitor():
    """Monitor for a short time (10 seconds)"""
    print("\n" + "="*60)
    print("EXAMPLE 2: Short Monitoring Session (10 seconds)")
    print("="*60)
    
    monitor = BaseTransactionMonitor()
    monitor.monitor_transactions(duration_seconds=10)
    time.sleep(2)

def example_3_track_popular_address():
    """Track a popular DeFi contract or bridge address"""
    print("\n" + "="*60)
    print("EXAMPLE 3: Track Base Bridge Address")
    print("="*60)
    print("Monitoring the Base Bridge for 15 seconds...")
    
    # Base Bridge address (this is a real, popular address)
    base_bridge = "0x49048044D57e1C92A77f79988d21Fa8fAF74E97e"
    
    monitor = BaseTransactionMonitor()
    monitor.track_address(base_bridge, duration_seconds=15)
    time.sleep(2)

def example_4_lookup_recent_tx():
    """Show how to look up a transaction"""
    print("\n" + "="*60)
    print("EXAMPLE 4: Transaction Lookup Example")
    print("="*60)
    
    monitor = BaseTransactionMonitor()
    
    # First get latest block
    block_num = monitor.get_latest_block_number()
    if block_num:
        # Get that block's data
        block_data = monitor.get_block_details(block_num)
        
        if block_data and block_data.get('transactions'):
            # Get first transaction hash
            first_tx_hash = block_data['transactions'][0]['hash']
            
            print(f"Looking up transaction: {first_tx_hash}")
            tx_details = monitor.get_transaction_details(first_tx_hash)
            
            if tx_details:
                print("\n📝 Transaction found!")
                print(f"   From: {tx_details['from']}")
                print(f"   To: {tx_details.get('to', 'Contract Creation')}")
                print(f"   Block: {int(tx_details['blockNumber'], 16)}")


def main():
    """Run all examples"""
    print("\n" + "="*60)
    print("🌊 BASE TRANSACTION MONITOR - USAGE EXAMPLES")
    print("="*60)
    print("\nThis will demonstrate different ways to use the monitor.")
    print("Total runtime: ~45 seconds")
    
    input("\nPress Enter to start...")
    
    # Run examples
    example_1_quick_check()
    example_2_short_monitor()
    example_3_track_popular_address()
    example_4_lookup_recent_tx()
    
    print("\n" + "="*60)
    print("✅ All examples completed!")
    print("="*60)
    print("\nNow try running: python base_monitor.py")
    print("for the interactive menu!\n")


if __name__ == "__main__":
    main()
