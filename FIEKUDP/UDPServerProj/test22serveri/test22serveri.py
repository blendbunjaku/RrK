from socket import*
import time
import datetime
import random
import math



def Timefunksioni():
    Kthimi = str(datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S %p'))
    serverSocket.sendto(Kthimi.encode("ASCII"), adresaKlientit)
    print("Koha: " + Kthimi)

def Kenofunksioni():
              
        rand = random.sample(range(80),20)
        print("Keno numrat:" + str(rand))
        serverSocket.sendto(str(rand).encode("ASCII"), adresaKlientit)
        
        
   

def NrZanoreve():
      test = "Ky eshte nje test tjeter"
      zanoret = 0

      for char in test:
        if(char ==('a') or char ==('e') or char ==('i') or char ==('o') or char ==('u')):
           zanoret += 1
      serverSocket.sendto(str(zanoret).encode("ASCII"), adresaKlientit)
      print("Numri i zanoreve ne fjaline 'Ky eshte nje test tjeter': " + str(zanoret))

def Hostfunksioni():
    try:
        host = gethostbyaddr(Host)
        Kthimi = "Hosti : " + str(host[0])
    except ValueError:
        Kthimi = "Hosti nuk dihet"
    Mesazhi = Kthimi
    serverSocket.sendto(Mesazhi.encode("ASCII"), adresaKlientit)
    print("Hosti:" + Kthimi)

def ipfunksioni():
    pergjigja = "IP adresa e klientit eshte " + adresaKlientit[0]
    serverSocket.sendto(str(pergjigja).encode("ASCII"), adresaKlientit)

def portfunksioni():
    
        
        Porti= serverSocket.getsockname()[1]
        serverSocket.sendto(str(Porti).encode("ASCII"), adresaKlientit)

def Printofunksioni():

    while True:
        mesazhiPranuar, adresaKlientit =  serverSocket.recvfrom(2048)
        print(mesazhiPranuar.decode("ASCII"))
        serverSocket.sendto(mesazhiPranuar, adresaKlientit)
   
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
                
    def NUMfunksioni():
    num = float(input("Enter a number: "))
    if num > 0:
    print("Positive number")
    elif num == 0:
    print("Zero")
    else:
    print("Negative number")
    serverSocket.sendto(num.encode("ASCII"), adresaKlientit)           

     while True:
        Opcioni, adresaKlientit =  serverSocket.recvfrom(2048)
        
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

     serverSocket.sendto(mesazhi.encode("ASCII"), adresaKlientit)
     print("" + mesazhi)

def Faktorielfunksioni(n):
  faktorieli=str(math.factorial(5))
  serverSocket.sendto(faktorieli.encode("ASCII"), adresaKlientit)
  print("Faktorieli : " + faktorieli)
  


#-------------

Host = "127.0.0.1"
Port = 9000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('127.0.0.1',9000))



while True:
        print("Serveri eshte i gatshem per pranim te te dhenave ... ")
        Kerkesa, adresaKlientit =  serverSocket.recvfrom(1024)
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
        elif Kerkesa.decode("ASCII") == "NUM":
            NUMfunksioni()
        else:
            mesazhi = "Kryeni njerin per operacioneve te lartepermendura..."
            serverSocket.sendto(mesazhi.encode("ASCII"), adresaKlientit)
