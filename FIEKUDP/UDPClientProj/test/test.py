from socket import *
import datetime
import time
import random


server = "127.0.0.1"
port = 9000
clientSocket = socket(family = AF_INET, type=SOCK_DGRAM)
print("Kerkesat qe mund te beni : IP , PORT, PRINTO, KENO, KONVERTO, HOST, TIME, FAKTORIEL, ZANORET")
while True:
    kerkesa=input("Shkruaj kerkesen : ")
    
    clientSocket.sendto(kerkesa.encode("ASCII"),(server,port))
    if kerkesa=="KONVERTO":
         Opcioni=input("Opcioni: ")
         clientSocket.sendto(Opcioni.encode("ASCII"),(server,port))
         Opcioni, adresenEServerit = clientSocket.recvfrom(1024)
         print(Opcioni.decode("ASCII"))
    elif kerkesa=="PRINTO":
        mesazh = input("Fjalia juaj: ")
        clientSocket.sendto(mesazh. encode("ASCII"), (server, port))
        mesazhiKthyer, adresenEServerit = clientSocket.recvfrom(1024)
        print(mesazhiKthyer.decode("ASCII"))
   
   
    
    pergjigja , serverAddress=clientSocket.recvfrom(1024)
    print("Pergjigja: " + pergjigja.decode("ASCII"))