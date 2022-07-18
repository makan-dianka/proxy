import requests

proxies_file = "socket.txt"

def get_proxy(file: str):
    cpt = 1
    proxy_valid = []
    with open(file) as f:
        proxies = f.readlines()
        for socket in proxies:
            proxy = socket.strip()
            print(f"\033[34m[{cpt}] [testing] {proxy}")
            try:
                # url for testing proxy
                http = requests.get("https://httpbin.org/ip", proxies={'http':proxy, 'https':proxy}, timeout=5)
            except:
                print(f"\033[31m[{cpt}] [failed]  {proxy}")
                pass
            else:
                print(f"\033[32m[{cpt}] [OK]  {proxy}")
                proxy_valid.append(proxy)
            cpt += 1
    
    print(f"\033[32m\ndone with: {len(proxy_valid)}/{len(proxies)} proxy valid")
    for proxy in proxy_valid:
        print(f"\033[32mProxy [OK] - {proxy}")
    return proxy_valid
    
get_proxy(proxies_file)