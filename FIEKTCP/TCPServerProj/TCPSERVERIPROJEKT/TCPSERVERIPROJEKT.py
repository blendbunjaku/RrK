from socket import *
import time
import datetime
import random
import math



def Timefunksioni():
    Kthimi = str(datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S %p'))
    connectionSocket.send(Kthimi.encode("ASCII"))
    print("Koha: " + Kthimi)

def Kenofunksioni():
    
                
        rand = random.sample(range(80),20)
        print("Keno numrat:" + str(rand))
        connectionSocket.send(str(rand).encode("ASCII"))
        
        
   

def NrZanoreve():
      test = "Ky eshte nje test tjeter"
      zanoret = 0

      for char in test:
        if(char ==('a') or char ==('e') or char ==('i') or char ==('o') or char ==('u')):
           zanoret += 1
      connectionSocket.send(str(zanoret).encode("ASCII"),)
      print("Numri i zanoreve ne fjaline 'Ky eshte nje test tjeter': " + str(zanoret))




def Hostfunksioni():
    try:
        host = gethostbyaddr(Host)
        Kthimi = "Hosti : " + str(host[0])
    except ValueError:
        Kthimi = "Hosti nuk dihet"
    Mesazhi = Kthimi
    connectionSocket.send(Mesazhi.encode("ASCII"))
    print("Hosti:" + Kthimi)



def ipfunksioni():
    pergjigja = "IP adresa e klientit eshte " + adresaKlientit[0]
    connectionSocket.send(str(pergjigja).encode("ASCII"))

def portfunksioni():
    
        
        Porti= connectionSocket.getsockname()[1]
        connectionSocket.send(str(Porti).encode("ASCII"))

def Printofunksioni():

    while True:
        connectionSocket , adresa = serverSocket.accept()
        mesazhiPranuar = connectionSocket.recv(1024)
             
        print(mesazhiPranuar.decode("ASCII"))
        connectionSocket.send(str(mesazhiPranuar).encode("ASCII"))

def Konvertofunksioni():
     def fahrenheitToCelsius(fahrenheit):
             celsius = fahrenheit - 32 
             print("Konvertimi: " , celsius , "C")

     def celsiusToFahrenheit(celsius):
            fahrenheit = celsius + 32
            print("Konvertimi: " ,fahrenheit , "F")

     def poundToKilogram(pound):
            kilogram = pound - 0.546408
            if kilogram != 1:
              print("%.2f" % round(kilogram,2) , "Kilograms")
            else:    
             print("%.2f" % round(kilogram,2) , "Kilogram")

     def kilogramToPound(kilogram):
           pound = kilogram + 0.546408
           if pound != 1:
             print("%.2f" % round(pound,2) , "Pounds")
           else:
             print("%.2f" % round(pound,2) , "Pound")

     while True:
        connectionSocket , adresaKlientit = serverSocket.accept()
        Opcioni = connectionSocket.recv(1024)
        
        print("Opcioni: " + Opcioni.decode("ASCII"))
        if Opcioni.decode("ASCII")=="FahrenheitToCelsius":
              fahrenheitToCelsius(52) 
              
        elif Opcioni.decode("ASCII")=="CelsiusToFahrenheit":
              celsiusToFahrenheit(10)

        elif Opcioni.decode("ASCII")=="PoundToKilogram":
              poundToKilogram(30)

        elif Opcioni.decode("ASCII")=="KilogramToPound":
              kilogramToPound(78)

        else:
             mesazhi = "Opcioni i zgjedhur nuk ekziston"

     connectionSocket.send(str(mesazhi).encode("ASCII"))
     print("" + str(mesazhi))

def Faktorielfunksioni(n):
  faktorieli=str(math.factorial(5))
  connectionSocket.send(str(faktorieli).encode("ASCII"))
  print("Faktorieli : " + faktorieli)
  

port = 13000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',port))

serverSocket.listen(1)

while True:
        print("Serveri eshte i gatshem per pranim te te dhenave ... ")
        connectionSocket, adresaKlientit = serverSocket.accept()
        Kerkesa = connectionSocket.recv(1024)
        print("Kerkesa: " + Kerkesa.decode("ASCII"))
        if Kerkesa.decode("ASCII") == "IP":
            ipfunksioni()
        elif Kerkesa.decode("ASCII") == "PORT":
            portfunksioni()
        elif Kerkesa.decode("ASCII") == "ZANORET":
            NrZanoreve()
        elif Kerkesa.decode("ASCII") == "PRINTO":
            Printofunksioni()
        elif Kerkesa.decode("ASCII") == "HOST":
            Hostfunksioni()
        elif Kerkesa.decode("ASCII") == "TIME":
            Timefunksioni()
        elif Kerkesa.decode("ASCII") == "KENO":
            Kenofunksioni()
        elif Kerkesa.decode("ASCII") == "FAKTORIEL":
            Faktorielfunksioni(5)
        elif Kerkesa.decode("ASCII") == "KONVERTO":
            Konvertofunksioni()
        else:
            mesazhi = "Kryeni njerin per operacioneve te lartepermendura..."
            connectionSocket.send(mesazhi.encode("ASCII"))
connectionSocket.close()