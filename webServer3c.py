import socket
import time
import os

SERVER_ADDRESS = (HOST, PORT) = "", 8888
REQUEST_QUEUE_SIZE = 5


def handle_request(client_conn):
    request = client_conn.recv(1024)

    print(
        'Child PID: {pid}, Parent PID: {ppid}\n'.format(
            pid = os.getpid(),
            ppid = os.getppid())
    )
    
    print(request.decode())
    http_response = b"""\
HTTP/1.1 200 OK

Hello world!
"""
    client_conn.sendall(http_response)
    time.sleep(60)


def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print("Serving HTTP on PORT {port} ...".format(port=PORT))
    print('PARENT PID (PPID): {pid}\n'.format(pid = os.getpid()))

    while True:
        client_conn, client_addr = listen_socket.accept()
        pid = os.fork()
        if pid == 0: # child
            listen_socket.close() # close child copy
            handle_request(client_conn)
            client_conn.close()
            os._exit(0) # child exits
        else: # parent
            client_conn.close() # parent close and loop over


if __name__ == "__main__":
    serve_forever()
