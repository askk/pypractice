import os
import socket
import threading
import SocketServer


BUF_SIZE = 2048
SERVER_HOST = 'localhost'
SERVER_PORT = 0


class ForkingClient():
    """ A client to test forking server"""
    def __init__(self, ip, port, msg):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, port))
        self.msg = msg

    def run(self):
        pid = os.getpid()
        print("PID " + str(pid) + " send echo message to server: " + self.msg)
        send_data_len = self.sock.send(self.msg)
        print("Send " + str(send_data_len) + " chars to server, so far...")

        response = self.sock.recv(BUF_SIZE)
        print("PID " + str(pid) + " received: " + response)

    def shutdown(self):
        self.sock.close()


class ForkingServer(SocketServer.ForkingMixIn, SocketServer.TCPServer):
    """ Do nothing..."""


class ForkingServerRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(BUF_SIZE)
        pid = os.getpid()
        response = str(pid) + ": " + data
        print("Server send response: " + response)
        self.request.send(response)


def main():
    server = ForkingServer((SERVER_HOST, SERVER_PORT), ForkingServerRequestHandler)
    ip, port = server.server_address

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()

    client1 = ForkingClient(ip, port, "Message from client 1")
    client1.run()

    client2 = ForkingClient(ip, port, "Message from client 2")
    client2.run()

    client1.shutdown()
    client2.shutdown()
    server.shutdown()
    server.socket.close()


if __name__ == '__main__':
    main()