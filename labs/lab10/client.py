"""
https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
"""

import socket,sys


def client_program(host=None):
    if host == None:
        host = socket.gethostbyname(socket.gethostname())  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        if data.lower().strip() == 'bye':
            break

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    if len(sys.argv) > 1:
        host = sys.argv[1]
    else:
        host = None
    client_program(host)
    
