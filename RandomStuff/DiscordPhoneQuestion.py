'''
Write a socket-server chat-server that accepts clients that connect to it over TCP. An example client would be netcat or telnet.

In order to start we will focus on creating an MVP version with the most basic functionality. As time permits we will have some follow-ups, so let's focus on getting the MVP running first:

Connect and disconnect with multiple client support

The chat server should be capable of handling multiple clients connecting at the same time.
Disconnection should be handled in a clean way.

> yo
< whats up?
> Nothing much!!
< same here, hbu?
> same ol' same
'''

# import socket 
# import sys 
# import time  

'''
new_socket = socket.socket() 
host_name = socket.gethostname() 
s_ip = socket.gethostbyname(host_name) 
port = 8080   
new_socket.bind((host_name, port))

print("Binding Successful!")
print("This is your IP: ", s_ip)   
name = input('Enter name:') 
new_socket.listen(1)   
conn, add= new_socket.accept() 
print("Received connection from ", add[0]) 
print('Connection Established. Connected From: ',add[0])   
client = (conn.recv(1024)).decode() 
print(client + ' has connected.') 
conn.send(name.encode())  
while True:     
    message = input('Me : ')     
    conn.send(message.encode())     
    message = conn.recv(1024)     
    message = message.decode()     
    print(client, ':', message) 
'''


# # Create a socket object
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Bind the socket to a specific port
# server_socket.bind(("localhost", 5000))

# # Listen for incoming connections
# server_socket.listen(5)

# # Accept incoming connections
# while True:
#     (client_socket, client_address) = server_socket.accept()

#     # Get the client's name
#     client_name = client_socket.recv(1024).decode("utf-8")

#     # Send a welcome message to the client
#     client_socket.send("Welcome to the chat room, {}!".format(client_name).encode("utf-8"))

#     # Start a loop to receive messages from the client
#     while True:
#         message = client_socket.recv(1024).decode("utf-8")

#         # If the client sends a message that says "quit", then close the connection
#         if message == "quit":
#             break

#         # Otherwise, broadcast the message to all other clients
#         for other_client in clients:
#             other_client.send(message.encode("utf-8"))

#     # Close the connection to the client
#     client_socket.close()

import socket
import threading

# List to store connected clients
clients = []

def handle_client(client_socket):
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            
            # Send the received message to all other clients
            for client in clients:
                if client != client_socket:
                    try:
                        client.send(message.encode("utf-8"))
                    except:
                        clients.remove(client)
        except:
            break

def main():
    host = "127.0.0.1"
    port = 12345
    
    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Chat server started on {}:{}".format(host, port))

    while True:
        client_socket, _ = server_socket.accept()
        clients.append(client_socket)
        print("Client connected")

        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()
