import os

def install_panel():
    os.system("apt update -y")
    os.system("apt install nginx mariadb-server curl -y")