import socket

HOST = "127.0.0.1"
PORT = 6666

with socket.socket() as s :
	s.bind((HOST,PORT))
	s.listen()
	conn, address = s.accept()
	with conn:
		print(f"Connected by {address}")
		while True:
			data = conn.recv(1024)
			if not data:
				break
			conn.sendall(data)
