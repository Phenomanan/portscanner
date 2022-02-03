#!/usr/bin/env python3
import socket

# Attempt to connect to the host on a particular port
# Simply return True or False
def scan_port(hostname, port) -> bool:

    sock = socket.socket()

    # Attempt to connect on the port
    try:
        sock.connect((hostname, port))
    except:
        return False
    else:
        return True



def main():
    hostname = input("Enter which host you'd like to scan (default localhost): ") or "127.0.0.1"
    port_range = int(input("Enter how many ports you'd like to scan (default 65535): ") or "65535")

    if port_range < 0 or port_range > 65535:
        sys.exit("Error: Invalid port range. Must be between 0-65535")

    open_ports = []

    # Scan those ports
    for port in range(1, port_range):
        if scan_port(hostname, port):
            open_ports.append(port) 

    # Print out ports comma separated
    print("\nHost {} has the following ports exposed:\n\n{}".format(hostname, '\n'.join(map(str, open_ports))))



if __name__ == "__main__":
    main()
