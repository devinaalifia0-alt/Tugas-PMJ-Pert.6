import socket

# Dapatkan IP laptop server
host = socket.gethostbyname(socket.gethostname())
port = 5000  # port bisa diganti jika dibutuhkan

print(f"Server berjalan di {host}:{port}")

# Buat socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print("Menunggu koneksi dari client...")

conn, addr = server_socket.accept()
print(f"Terhubung dengan client: {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data or data.lower() == 'exit':
        print("Client memutuskan koneksi.")
        break

    print(f"Pesan dari client: {data}")
    pesan_balasan = input("Balas ke client: ")
    conn.send(pesan_balasan.encode())

conn.close()
server_socket.close()