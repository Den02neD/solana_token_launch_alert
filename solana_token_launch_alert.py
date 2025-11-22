import requests, time

def launch_alert():
    print("Solana instant launch alerts (pump.fun + raydium)")
    seen = set()
    while True:
        r = requests.get("https://pump-portal.fun/api/new-tokens")
        for token in r.json().get("tokens", []):
            mint = token["address"]
            if mint in seen: continue
            seen.add(mint)
            if token.get("raydium_pool"):
                print(f"LAUNCH CONFIRMED!\n"
                      f"{token['symbol']} | {token['name']}\n"
                      f"Mint: {mint}\n"
                      f"Pool: {token['raydium_pool']}\n"
                      f"https://dexscreamer.com/solana/{mint}\n"
                      f"https://pump.fun/{mint}\n"
                      f"{'-'*50}")
        time.sleep(2.5)

if __name__ == "__main__":
    launch_alert()
