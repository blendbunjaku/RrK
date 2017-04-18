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
    pergjigja , serverAddress=clientSocket.recvfrom(1024)
    print("Pergjigja: " + pergjigja.decode("ASCII"))
