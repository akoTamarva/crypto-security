import re

def is_btc_address(addr: str) -> bool:
    return bool(re.match(r"^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$", addr))

def is_eth_address(addr: str) -> bool:
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", addr))

if __name__ == "__main__":
    btc = "1BoatSLRHtKNngkdXEeobR76b53LETtpyT"
    eth = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"

    print("BTC valid?", is_btc_address(btc))
    print("ETH valid?", is_eth_address(eth))
