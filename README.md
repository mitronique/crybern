# crybern

> A lightweight and modular Cybersecurity CLI Toolkit for ethical hackers, pentesters, and researchers — built with Python and C++.

---

## Overview

**crybern** is a command-line based toolkit that provides essential cybersecurity utilities in one place — think of it as your Swiss Army Knife for the terminal. Built with extensibility in mind, it includes tools for:

- 🔍 Port scanning  
- 🌐 Subdomain enumeration  
- 🔐 Hash identification and generation  
- 🔎 WHOIS lookup  
- 🧰 Base64 encoding/decoding (C++)  
- 🧠 Custom password dictionary generation  
- ☁️ Ping sweeping *(coming soon)*


---

## Features

| Tool                     | Description                                      |
|--------------------------|--------------------------------------------------|
| `portscan`               | Scan open ports on a host                        |
| `subenum`                | Enumerate subdomains using a wordlist           |
| `hashid`                 | Identify types of common hashes (MD5, SHA1...)  |
| `hash`                   | Generate hashes (MD5, SHA1, SHA256)             |
| `pwgen`                  | Create password dictionaries from basewords     |
| `whois`                  | Perform WHOIS lookups                           |
| `base64_tool` *(C++)*    | Encode or decode Base64 strings                 |

---

## Installation

### Python Dependencies

```bash
git clone https://github.com/yourusername/crybern.git
cd crybern
pip install -r requirements.txt
```

### Compile C++ Tools (Optional)

```bash
g++ cpp_tools/base64_tool.cpp -o base64_tool -lssl -lcrypto
```

---

## Usage

```bash
python3 main.py <command> [options]
```

### Examples:

```bash
python3 main.py portscan 192.168.1.1 --ports 20-100
python3 main.py subenum example.com
python3 main.py hashid 5f4dcc3b5aa765d61d8327deb882cf99
python3 main.py hash sha256 "mysecret"
python3 main.py pwgen welcome123 --output weakpass.txt
python3 main.py whois example.org
./base64_tool encode "cyberswiss"
```

---

## Directory Structure

```
crybern/
├── main.py
├── requirements.txt
├── README.md
├── tools/
│   ├── port_scanner.py
│   ├── subdomain_enum.py
│   ├── hash_identifier.py
│   ├── password_dict_gen.py
│   ├── whois_lookup.py
│   └── hasher.py
├── cpp_tools/
│   └── base64_tool.cpp
```

---

## Roadmap

- [ ] Add Ping Sweep tool (Python or raw socket in C++)
- [ ] Add CVE checker via API
- [ ] Add Shodan/AbuseIPDB integration
- [ ] Add TUI mode with curses
- [ ] Package as PyPI installable CLI tool

---

## Contributing

Pull requests are welcome! If you'd like to contribute a new tool or improve an existing one, feel free to fork the project and submit a PR.

---

## Legal Disclaimer

This toolkit is intended **only for educational and authorized penetration testing** purposes. The developer is not responsible for any misuse of this software.

---

## Author

[mitronique](https://github.com/mitronique)

---

## License

MIT License
