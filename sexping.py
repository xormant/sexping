import argparse
import socket
import time
import requests

def get_isp(ip): return requests.get(f"https://api.incolumitas.com/?q={ip}").json()['asn']['org']

def tcp_ping(ip, port, isp):
    try:
        start = time.time()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((ip, port))
        end = time.time()
        print(f"Connected to {ip} port={port} isp={isp} time={round((end - start) * 1000, 2)}ms protocol=TCP")
        sock.close()
    except:
        print(f"Host {ip} port={port} Timed Out....")

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        print(f"[x] Error, Invalid arguments\nUsage: {argv[0]} <ip> <port>")
        exit(0)

    print(f"Pinging {args[1]} on port {args[2]}...")

    while True:
        """
            This thread should take 2 seconds max to respond. If host is offline threads will be stacked 
            upto like 2-3 per second on the 2 socket timeout delay
        """
        threading.Thread(target=tcp_ping, args=(args[1], args[2], get_isp(args[1]),).start()
        time.sleep(1)
