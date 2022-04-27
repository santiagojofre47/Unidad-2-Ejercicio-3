import csv
from claseRegistro import Registro

class ManejadorRegistro:
    __lista = []

    def __init__(self):
        self.__lista = [[]]
        self.inicializarLista()

    def agregarRegistro(self, dia, unRegistro):
        self.__lista[dia].append(unRegistro)  

    
    def inicializarLista(self):
        for i in range(30):
            self.__lista.insert(0,[])
            for j in range(24):
                self.__lista[i].insert(0,'Sin datos registrados')     

    def cargarLista(self):
        archivo = open('registro.csv')
        reader = csv.reader(archivo, delimiter = ',')    
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                dia = int(fila[0])
                hora = int(fila[1])
                unRegistro = Registro(dia,hora,float(fila[2]),float(fila[3]),float(fila[4]))
                self.agregarRegistro(dia-1,unRegistro)
        archivo.close()  

    def MaximoTemperatura(self):
        maximo = -9999
        dia = None
        hora = None
        for i in range(len(self.__lista)):
            for j in range(len(self.__lista[i])):
                if type(self.__lista[i][j]) == Registro:
                    if self.__lista[i][j].getTemperatura() > maximo:
                        maximo = self.__lista[i][j].getTemperatura()
                        dia = self.__lista[i][j].getDia()
                        hora = self.__lista[i][j].getHora()
        return 'Temperatura maxima registrada: {} en el dia {} hora {}'. format(maximo, dia, hora)

    def MinimoTemperatura(self):
        minimo = 9999
        dia = None
        hora = None
        for i in range(len(self.__lista)):
            for j in range(len(self.__lista[i])):
                if type(self.__lista[i][j]) == Registro:
                    if self.__lista[i][j].getTemperatura() < minimo:
                        minimo = self.__lista[i][j].getTemperatura()
                        dia = self.__lista[i][j].getDia()
                        hora = self.__lista[i][j].getHora()
        return 'Temperatura minima registrada: {} en el dia {} hora {}'. format(minimo, dia, hora)


    def MaximoPresion(self):
        maximo = -9999
        dia = None
        hora = None
        for i in range(len(self.__lista)):
            for j in range(len(self.__lista[i])):
                if type(self.__lista[i][j]) == Registro:
                    if self.__lista[i][j].getPresion() > maximo:
                        maximo = self.__lista[i][j].getPresion()
                        dia = self.__lista[i][j].getDia()
                        hora = self.__lista[i][j].getHora()
        return 'Maxima presion atmosferica  registrada: {} en el dia {} hora {}'. format(maximo, dia, hora)

    def MinimoPresion(self):
        minimo = 9999
        dia = None
        hora = None
        for i in range(len(self.__lista)):
            for j in range(len(self.__lista[i])):
                if type(self.__lista[i][j]) == Registro:
                    if self.__lista[i][j].getPresion() < minimo:
                        minimo = self.__lista[i][j].getPresion()
                        dia = self.__lista[i][j].getDia()
                        hora = self.__lista[i][j].getHora()
        return 'Minima presion atmosferica  registrada: {} en el dia {} hora {}'. format(minimo, dia, hora)

    def MaximaHumedad(self):
        maximo = -9999
        dia = None
        hora = None
        for i in range(len(self.__lista)):
            for j in range(len(self.__lista[i])):
                if type(self.__lista[i][j]) == Registro:
                    if self.__lista[i][j].getHumedad() > maximo:
                        maximo = self.__lista[i][j].getHumedad()
                        dia = self.__lista[i][j].getDia()
                        hora = self.__lista[i][j].getHora()
        return 'Maxima humedad  registrada: {} en el dia {} hora {}'. format(maximo, dia, hora)

    def MinimaHumedad(self):
        minimo = 9999
        dia = None
        hora = None
        for i in range(len(self.__lista)):
            for j in range(len(self.__lista[i])):
                if type(self.__lista[i][j]) == Registro:
                    if self.__lista[i][j].getHumedad() < minimo:
                        minimo = self.__lista[i][j].getHumedad()
                        dia = self.__lista[i][j].getDia()
                        hora = self.__lista[i][j].getHora()
        return 'Minima humedad  registrada: {} en el dia {} hora {}'. format(minimo, dia, hora)

    def PromedioMensualHora(self, hora):
        total = 0
        count = 0
        for i in range(len(self.__lista)):
            for j in range(len(self.__lista[i])):
                if type(self.__lista[i][j]) == Registro:
                    if self.__lista[i][j].getHora() == hora:
                        count+=1
                        total += self.__lista[i][j].getTemperatura()
        total /= count                          
        return float(total)               

    def mostrarPromedios(self):
        hora = 0
        while hora <= 24:
            print('Promedio mensual de la hora {}: {} °C' .format(hora,self.PromedioMensualHora(hora)))
            hora+=1
           
    def __str__(self):
        s=''
        for i in range(len(self.__lista)):
            for j in range(len(self.__lista[i])):
                if type(self.__lista[i][j]) == Registro:
                    s+= str(self.__lista[i][j]) + '\n'
        return s      

    def mostrarDatos(self, dia):
        hora = 0
        if dia <= 30:
            print('Hora\t\tTemperatura\t\tHumedad\t\tPresion')
            while hora <= 24:
                print('{}\t\t{}°C\t\t\t{}%\t\t{}'.format(self.__lista[dia-1][hora].getHora(), self.__lista[dia-1][hora].getTemperatura(), self.__lista[dia-1][hora].getHumedad(), self.__lista[dia-1][hora].getPresion()))
                hora+=1
        else:
            print('Dia ingresado invalido')    
  

                      
if __name__ == '__main__':
    lista = ManejadorRegistro()
    lista.cargarLista()
   
    
   
            




   
