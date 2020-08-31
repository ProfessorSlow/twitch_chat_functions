import CONSTANTS
import socket

from time import sleep


def connect_to_chat_channel(host=CONSTANTS.HOST, port=CONSTANTS.PORT):
    twitch_socket = socket.socket()
    twitch_socket.connect((host, port))
    twitch_socket.send("PASS {}\r\n".format(CONSTANTS.PASS).encode('utf-8'))
    twitch_socket.send("NICK {}\r\n".format(CONSTANTS.NICK).encode('utf-8'))
    twitch_socket.send("JOIN {}\r\n".format(CONSTANTS.CHAN).encode('utf-8'))
    while True:
        response = twitch_socket.recv(1024).decode('utf-8')
        print(response)
        sleep(0.1)


def main():
    connect_to_chat_channel()


if __name__ == '__main__':
    main()
