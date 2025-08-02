import hashlib

def hash_string(data):
    print("[1] MD5")
    print("[2] SHA1")
    print("[3] SHA256")
    print("[4] SHA512")
    choice = input("Choose hashing algorithm: ")

    if choice == "1":
        print(hashlib.md5(data.encode()).hexdigest())
    elif choice == "2":
        print(hashlib.sha1(data.encode()).hexdigest())
    elif choice == "3":
        print(hashlib.sha256(data.encode()).hexdigest())
    elif choice == "4":
        print(hashlib.sha512(data.encode()).hexdigest())
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    s = input("Enter string to hash: ")
    hash_string(s)