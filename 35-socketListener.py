import socket

Listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
Listener.bind(("10.0.2.15",8080))
Listener.listen(0)
print('Listening...')
(Connection, Address) = Listener.accept()
print('Connection Successful from ' + str(Address))

while True:
    command_input = raw_input('Enter Command: ')
    Connection.send(command_input)
    command_output = Connection.recv(1024)
    print(command_output)
