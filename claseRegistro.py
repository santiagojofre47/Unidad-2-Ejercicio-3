class Registro:
    __dia = None
    __hora = None
    __temperatura = None
    __presionAtomsferica = None
    __humedad = None
    

    def __init__(self,dia = None, hora = None, temperatura = None, presion = None, humedad = None):
        self.__dia = dia
        self.__hora = hora
        self.__temperatura = temperatura
        self.__presionAtomsferica = presion
        self.__humedad = humedad
        

    def __str__(self):
        s = 'Dia: {}\nHora: {}\nTemperatura: {}°C\nPresion Atomsferica: {}\nHuemdad: {}%\n'.format(self.__dia,self.__hora,self.__temperatura,self.__presionAtomsferica,self.__humedad)
        return s    

    def getDia(self):
        return self.__dia    

    def getHora(self):
        return self.__hora    

    def getTemperatura(self):
        return self.__temperatura

    def getPresion(self):
        return self.__presionAtomsferica    

    def getHumedad(self):
        return self.__humedad

        
       