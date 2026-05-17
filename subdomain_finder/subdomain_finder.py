import requests
import threading

domain = input('Enter domain name: ')

with open("subdomains.txt") as file:
    subdomains = file.read().splitlines()

discovered_subdomain = []

lock = threading.Lock()

def check_subdomain(subdomain):
    url = f"http://{subdomain}.{domain}"
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print(f'[+] discovered Subdomains: ', url)
        with lock:
            discovered_subdomain.append(url)

threads = []

for subdomain in subdomains:
    thread = threading.Thread(target=check_subdomain, args=(subdomain,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

with open("discovered_subdomain.txt", 'w') as f:
    for subdomain in discovered_subdomain:
        print(subdomain, file=f)