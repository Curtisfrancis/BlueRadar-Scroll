from web3 import Web3
import json

# --- CONFIGURATION ---
# 1. Scroll Sepolia RPC URL (The phone line to the blockchain)
SCROLL_RPC_URL = "https://sepolia-rpc.scroll.io/"

# 2. CONTRACT ADDRESS (CRITICAL: Replace this with your deployed address)
CONTRACT_ADDRESS = "0xDdc82357BFf240D3aBCBE66A6d6F89F2D2fF7caf"

# 3. CONTRACT ABI (The Interface Manual)
# This tells Python exactly how to talk to your specific contract functions
CONTRACT_ABI = [
    {
        "inputs": [{"internalType": "address", "name": "_user", "type": "address"}],
        "name": "hasActiveSubscription", 
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function"
    }
]

class BlockchainService:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(SCROLL_RPC_URL))
        # Set this to False to enforce real payments. 
        # Set to True if you want to skip payment checks during testing.
        self.mock_mode = True 

    def check_payment_status(self, wallet_address: str) -> bool:
        if self.mock_mode:
            print(f"⚠️ MOCK MODE: Granting access to {wallet_address}")
            return True

        try:
            # checksum address ensures the capitalization is correct (required by Web3)
            safe_address = Web3.to_checksum_address(wallet_address)
            
            contract = self.w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)
            
            # Call the 'hasActiveSubscription' function on the blockchain
            has_paid = contract.functions.hasActiveSubscription(safe_address).call()
            
            print(f"🔍 Checking Wallet {safe_address}: Subscription Active? {has_paid}")
            return has_paid
            
        except Exception as e:
            print(f"❌ Blockchain Error: {e}")
            return False # Default to deny if blockchain is unreachable

blockchain_service = BlockchainService()