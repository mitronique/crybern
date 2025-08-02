import requests
import sys

def find_subdomains(domain, wordlist):
    print(f"[+] Enumerating subdomains for: {domain}")
    with open(wordlist, "r") as f:
        for line in f:
            sub = line.strip() + "." + domain
            try:
                response = requests.get(f"http://{sub}", timeout=2)
                print(f"[+] Found: {sub}")
            except requests.ConnectionError:
                pass

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python subdomain_enum.py <domain> <wordlist.txt>")
        sys.exit(1)

    find_subdomains(sys.argv[1], sys.argv[2])
