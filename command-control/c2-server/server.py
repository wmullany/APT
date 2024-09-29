import socket

# Setup the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 9999))
server.listen(5)

print("[*] Listening on 0.0.0.0:9999")

while True:
    client_socket, addr = server.accept()
    print(f"[*] Accepted connection from {addr}")

    # Handle client commands
    command = input("Enter command to send to the client: ")
    if command.lower() == 'exit':
        break

    client_socket.send(command.encode())
    response = client_socket.recv(4096)
    print(response.decode())

client_socket.close()
server.close()
