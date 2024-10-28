import os
import socket
import json

# Sunucu adresi (ana makinenin IP'si ve portu)
SERVER_IP = '0.0.0.0'  # Tüm IP adreslerinden bağlantı kabul etmek için
SERVER_PORT = 5000     # Ana makinenin belirlediği port

def search_files(directory, filename):
    results = []
    if os.path.exists(directory):
        for root, dirs, files in os.walk(directory):
            for file in files:
                if filename.lower() in file.lower():
                    file_path = os.path.join(root, file)
                    results.append({
                        'name': file_path,
                        'size': os.path.getsize(file_path) / 1024,  # KB cinsinden boyut
                        'result': 'Bulundu'
                    })
    return results

def main():
    # Socket oluştur
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((SERVER_IP, SERVER_PORT))
        s.listen()

        print(f"Dinleme: {SERVER_IP}:{SERVER_PORT}")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Bağlantı kuruldu: {addr}")
                data = conn.recv(1024)
                if not data:
                    break

                # JSON verisini ayrıştır
                request = json.loads(data.decode('utf-8'))
                directory = request['directory']
                filename = request['filename']

                # Dosya arama işlemi
                search_results = search_files(directory, filename)

                # Sonuçları geri gönder
                conn.sendall(json.dumps(search_results).encode('utf-8'))

if __name__ == "__main__":
    main()