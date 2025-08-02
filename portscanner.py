import socket

def scan(target, port_range):
    start_port, end_port = map(int, port_range.split("-"))
    print(f"[+] Scanning {target} from port {start_port} to {end_port}")
    for port in range(start_port, end_port + 1):
        s = socket.socket()
        s.settimeout(0.5)
        try:
            s.connect((target, port))
            print(f"  [OPEN] Port {port}")
        except:
            pass
        s.close()
