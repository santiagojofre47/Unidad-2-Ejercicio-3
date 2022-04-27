from ManejadorRegistro import Registro

class Menu:
    __op = None

    def __init__(self, opcion = 'a'):
        self.__op = opcion

    def Mostrar(self, unManejador):
        cerrar = False
        while cerrar == False:
            print('a- Mostrar dia y hora de mayor valor de cada variable (Temperatura - Presion - Humedad)')
            print('b- Mostrar tempertaura promedio mensual de cada hora')
            print('c- Mostrar el registro Temperatura, presion y humedad de un día dado')
            print('d- Salir')
            self.__op = input('Ingrese una opcion: ')   

            if self.__op == 'a':
                self.EjecutarA(unManejador)
                print('\n\n')

            elif self.__op == 'b':
                self.EjecutarB(unManejador)
                print('\n\n')


            elif self.__op == 'c':
                self.EjecutarC(unManejador)
                print('\n\n')
            
            elif self.__op == 'd':
                print('Cerrando Menu...')
                cerrar = True
            else:
                print('Opcion ingresada invalida!')
                input('Presione ENTER para continuar...')    
            

    def EjecutarA(self, unManejador):
        print(unManejador.MaximoTemperatura())
        print(unManejador.MinimoTemperatura())
        print(unManejador.MaximaHumedad())
        print(unManejador.MinimaHumedad())
        print(unManejador.MaximoPresion())
        print(unManejador.MinimoPresion())    

    def EjecutarB(self, unManejador):
        unManejador.mostrarPromedios()    


    def EjecutarC(self, unManejador):
        dia = input('Ingrese el numero de dia (1-30): ')
        unManejador.mostrarDatos(int(dia))




