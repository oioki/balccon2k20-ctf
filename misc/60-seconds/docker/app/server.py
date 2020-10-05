#!/usr/bin/env python3

import socketserver
import threading
import time

from game import Game


class Service(socketserver.BaseRequestHandler):

    def handle(self):
        game = Game()

        while True:
            result = game.check_game_over()
            if result:
                self.send(result)
                return

            self.send(game.state())

            pos = self.receive().decode('ascii')
            column = ord(pos[0]) - ord('a')
            row = int(pos[1]) - 1
            game.move(row, column)


    def send(self, string, newline=True):
        if isinstance(string, str):
            string = string.encode("utf-8")

        if newline:
            string = string + b"\n"
        self.request.sendall(string)


    def receive(self, prompt="> "):
        self.send(prompt, newline=False)
        return self.request.recv(4096).strip()


class ThreadedService(
        socketserver.ThreadingMixIn,
        socketserver.TCPServer,
):
    pass

if __name__ == '__main__':
    host = "0.0.0.0"
    port = 1100

    service = Service
    server = ThreadedService((host, port), service)
    server.allow_reuse_address = True

    server_thread = threading.Thread(target=server.serve_forever)

    server_thread.daemon = True
    server_thread.start()

    print("Server started on " + str(server.server_address))

    while True:
        time.sleep(10)
