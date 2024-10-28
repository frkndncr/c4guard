import socket
import json
import platform

SERVER_IP = '10.154.2.26'  # Ana makine IP'si
SERVER_PORT = 5000          # Ana makine portu

connected_agents = []  # Bağlı agentların bilgilerini saklamak için

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(5)
    print(f"Sunucu {SERVER_IP}:{SERVER_PORT} üzerinde çalışıyor...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Yeni bağlantı: {addr}")
        data = client_socket.recv(1024)
        try:
            agent_info = json.loads(data.decode('utf-8'))
            agent_info['os'] = platform.system()  # İşletim sistemini ekleyin
            connected_agents.append(agent_info)
            print(f"Agent kaydedildi: {agent_info}")
            client_socket.sendall(b"Agent basariyla kaydedildi!")
        except json.JSONDecodeError:
            print("Geçersiz veri alındı.")
        client_socket.close()

if __name__ == "__main__":
    start_server()