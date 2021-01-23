import socket
import json

class SocketListener:
    def __init__(self,ip,port):
        Listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        Listener.bind((ip, port))
        Listener.listen(0)
        print('Listening...')
        (self.Connection, Address) = Listener.accept()
        print('Connection Successful from ' + str(Address))

    def json_send(self,data):
        json_data = json.dumps(data)
        self.Connection.send(json_data)

    def json_receive(self):
        json_data = self.Connection.recv(1024)
        return json.loads(json_data)

    def command_execution(self, command_input):
        self.json_send(command_input)
        return self.json_receive()

    def start_listener(self):
        while True:
            command_input = raw_input('Enter Command: ')
            command_output = self.command_execution(command_input)
            print(command_output)

socket_listener = SocketListener('10.0.2.15',8080)
socket_listener.start_listener()
