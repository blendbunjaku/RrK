from socket import *
import datetime
import time
import random
import math


server = "127.0.0.1"
port = 13000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((server,port))
print("Kerkesat qe mund te beni : IP , PORT, PRINTO, KENO, KONVERTO, HOST, TIME, FAKTORIEL, ZANORET")
while True:
    kerkesa=input("Shkruaj kerkesen : ")
       
    clientSocket.send(kerkesa.encode("ASCII"))
    if kerkesa=="KONVERTO":
         Opcioni=input("Opcioni: ")
         clientSocket.send(Opcioni.encode("ASCII"))
         mesazhiKthyer = clientSocket.recv(1024)
         print(mesazhiKthyer.decode("ASCII"))
    elif kerkesa=="PRINTO":
        mesazh = input("Fjalia juaj: ")
        clientSocket.send(mesazh.encode("ASCII"))
        mesazhiKthyer=clientSocket.recv(1024)
        print(mesazhiKthyer.decode("ASCII"))
    
    pergjigja = clientSocket.recv(1024)
    print("Pergjigja: " + pergjigja.decode("ASCII"))

clientSocket.close()