import socket
import sys
import argparse


def test_socket_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Default socket timeout: " + str(s.gettimeout()))
    s.settimeout(200)
    print("After Change timeout: " + str(s.gettimeout()))


def argument_parse():
    parse = argparse.ArgumentParser(description='Socket Error Sample')
    parse.add_argument('--host', action='store', dest='host', reuired=False)
    parse.add_argument('--port', action='store', dest='port', type=int, reuired=False)
    parse.add_argument('--file', action='store', dest='file', reuired=False)

    input_args = parse.parse_args()
    host = input_args.host
    port = input_args.port
    filename = input_args.file

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print("Error create socket: " + str(socket.error))
        sys.exit(-1)

    try:
        s.connect(host, port)
    except socket.error:
        print("Error connect host: " + str(socket.error))
        sys.exit(-1)

    try:
        s.sendall("GET %s HTTP/1.0\r\n\r\n" %filename)
    except socket.error:
        print("Error get file: " + str(socket.error))
        sys.exit(-1)

    while 1:
        try:
            buffer = s.recv(4096)
        except socket.error:
            print("recv data error: " + str(socket.error))
            sys.exit(-1)

        if not len(buffer):
            break

        sys.stdout.write(buffer)

    s.close()


if __name__ == "__main__":
    test_socket_timeout()
