import os
import sys

def banner():
    print("""
========================
     SPYHOST TOOL
 VPS Automation System
========================
""")

def install_panel():
    print("[+] Installing Panel...")
    os.system("apt update -y && apt install nginx mariadb-server curl wget -y")

def install_node():
    print("[+] Installing Node...")
    os.system("apt update -y && apt install docker.io -y")

def cloudflare():
    print("[+] Cloudflare Setup (manual mode)")
    domain = input("Domain: ")
    ip = input("VPS IP: ")
    print(f"Create DNS: panel.{domain} -> {ip}")

def main():
    banner()

    if "--panel" in sys.argv:
        install_panel()

    elif "--node" in sys.argv:
        install_node()

    elif "--cf" in sys.argv:
        cloudflare()

    else:
        print("""
Usage:
  --panel   Install panel base
  --node    Install node
  --cf      Cloudflare setup
""")

if __name__ == "__main__":
    main()