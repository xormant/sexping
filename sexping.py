import argparse
import socket
import time
import requests

def get_isp(ip):
    response = requests.get(f"https://api.incolumitas.com/?q={ip}")
    data = response.json()
    return data['asn']['org']

def tcp_ping(ip, port):
    try:
        start = time.time()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((ip, port))
        end = time.time()
        response_time = round((end - start) * 1000, 2)
        isp = get_isp(ip)
        print(f"Connected to {ip} port={port} isp={isp} time={response_time}ms protocol=TCP")
        sock.close()
    except Exception as e:
        print(f"Error connecting to {ip} port={port}: {e}")
    time.sleep(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ping a TCP port on a remote host.")
    parser.add_argument("ip", type=str, help="The IP address or hostname to ping.")
    parser.add_argument("-p", "--port", type=int, default=80, help="The port to ping.")
    args = parser.parse_args()

    print(f"Pinging {args.ip} on port {args.port}...")

    while True:
        tcp_ping(args.ip, args.port)
