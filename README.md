### CHATROOM

This is a simple clients-server chatroom.

The server file basically is a listening socket and it listens for connections from clients.
When a client connects, the server calls __.accept()__ to accept or complete the connection.

	- socket()
	- .bind()
	- .listen()
	- .accept()
	
The above makes up the server side.


While on the client side is mainly to connect and make the 3-way handshake.

The primary component for the data exchange is now the __.send()__ and __.recv()__ .

