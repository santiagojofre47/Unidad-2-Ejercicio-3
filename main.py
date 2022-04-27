from claseRegistro import Registro
from claseMenu import Menu
from ManejadorRegistro import ManejadorRegistro

def test():
    print('Abriendo test...')
    Registro1 = Registro(1,24,19.0,100,13)
    Registro2 = Registro(2,23,18.0,150,14)
    print(Registro1)
    print(Registro2)
    print(Registro1.getHumedad())
    print('Cerrando test...\n\n')


if __name__ == '__main__':
    test()
    objetoMenu = Menu()
    unManejador = ManejadorRegistro()
    unManejador.cargarLista()
    print(unManejador)
    print('=== Menu de opciones === ')
    objetoMenu.Mostrar(unManejador)

