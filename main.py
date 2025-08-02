import argparse
from tools import port_scanner, subdomain_enum, hash_identifier, password_dict_gen, whois_lookup, hasher

parser = argparse.ArgumentParser(description="cyberswiss")

subparsers = parser.add_subparsers(dest="command")

# Add subcommands
port_parser = subparsers.add_parser("portscan")
port_parser.add_argument("target", help="Target IP or domain")
port_parser.add_argument("--ports", default="1-1024", help="Ports to scan (default 1-1024)")

sub_enum = subparsers.add_parser("subenum")
sub_enum.add_argument("domain", help="Target domain")

hash_id = subparsers.add_parser("hashid")
hash_id.add_argument("hash", help="Hash to identify")

pwgen = subparsers.add_parser("pwgen")
pwgen.add_argument("baseword", help="Base word for dictionary")
pwgen.add_argument("--output", help="Output file", default="dict.txt")

whois = subparsers.add_parser("whois")
whois.add_argument("domain", help="Domain to lookup")

hasher_cmd = subparsers.add_parser("hash")
hasher_cmd.add_argument("algo", choices=["md5", "sha1", "sha256"])
hasher_cmd.add_argument("string", help="String to hash")

args = parser.parse_args()

if args.command == "portscan":
    port_scanner.scan(args.target, args.ports)
elif args.command == "subenum":
    subdomain_enum.enumerate(args.domain)
elif args.command == "hashid":
    hash_identifier.identify(args.hash)
elif args.command == "pwgen":
    password_dict_gen.generate(args.baseword, args.output)
elif args.command == "whois":
    whois_lookup.lookup(args.domain)
elif args.command == "hash":
    hasher.hash_string(args.algo, args.string)
else:
    parser.print_help()

