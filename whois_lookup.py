import whois

def lookup_domain(domain):
    try:
        info = whois.whois(domain)
        print(f"Domain: {domain}")
        print(f"Registrar: {info.registrar}")
        print(f"Creation Date: {info.creation_date}")
        print(f"Expiration Date: {info.expiration_date}")
        print(f"Name Servers: {info.name_servers}")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    domain = input("Enter a domain: ")
    lookup_domain(domain)