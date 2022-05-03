from xmlrpc.client import ServerProxy
import msvcrt

s = ServerProxy('http://localhost:20064', allow_none=True)

while True:
    print('')
    print('Seleccione operación')
    print('---------------------------------')
    print("|Presione (+) para sumar         |")
    print("|Presione (-) para restar        |")
    print("|Presione (*) para multiplicación|")
    print("|Presione (/) para división      |")
    print('---------------------------------')

    operador = input('Ingresa el operador: ')

    if s.isValid(operador):
        a = int(input('Ingresa el primer valor: '))
        b = int(input('Ingresa el segundo valor: '))

        print(s.calc(a,b,operador))
    else:
        print('Operación no válida')
    
    print('')
    print("Presione 'x' para salir...")
    print("Presione cualquier tecla para continuar...")
    
    key = msvcrt.getwch()
    if key == 'x':
        exit()
