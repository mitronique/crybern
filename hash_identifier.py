import hashlib

def identify_hash(hash_str):
    hash_lengths = {
        32: "MD5",
        40: "SHA1",
        64: "SHA256",
        128: "SHA512"
    }

    hash_type = hash_lengths.get(len(hash_str), "Unknown")
    print(f"[*] Hash Type: {hash_type}")

if __name__ == "__main__":
    h = input("Enter the hash: ")
    identify_hash(h)
