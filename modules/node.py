import os

def install_node():
    os.system("apt update -y")
    os.system("apt install docker.io -y")