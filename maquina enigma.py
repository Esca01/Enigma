#


alfabeto_espanol = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                    'x', 'y', 'z', 'á', 'é', 'í', 'ó', 'ú', 'ü', '¿', '¡', '!', '?', ',', '.', '-', '_', '(', ')', '*', '+', '/', '<', '>', '=', '@', '#', '$', '%', '^', '&', '{', '}', '[', ']', ';', ':', '"', "'", '|', '\\', '~', '`', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

rotor1 = [['A', 3, False], ['B', 11, False], ['C', 91, False], ['D', 71, True], ['E', 86, False], ['F', 78, False], ['G', 40, False], ['H', 0, False], ['I', 60, False], ['J', 50, False], ['K', 54, False], ['L', 77, False], ['M', 98, False], ['N', 76, False], ['Ñ', 84, False], ['O', 87, False], ['P', 16, False], ['Q', 104, False], ['R', 26, False], ['S', 42, False], ['T', 2, False], ['U', 96, False], ['V', 83, False], ['W', 97, False], ['X', 82, False], ['Y', 81, False], ['Z', 19, False], ['a', 57, False], ['b', 12, False], ['c', 52, False], ['d', 43, False], ['e', 102, False], ['f', 9, False], ['g', 27, False], ['h', 61, False], ['i', 79, False], ['j', 28, False], ['k', 99, False], ['l', 63, False], ['m', 15, False], ['n', 18, False], ['ñ', 100, False], ['o', 73, False], ['p', 36, False], ['q', 103, False], ['r', 31, False], ['s', 6, False], ['t', 41, False], ['u', 51, False], ['v', 10, False], ['w', 55, False], ['x', 22, False], [
    'y', 25, False], ['z', 101, False], ['á', 93, False], ['é', 38, False], ['í', 30, False], ['ó', 44, False], ['ú', 35, False], ['ü', 4, False], ['¿', 89, False], ['¡', 88, False], ['!', 48, False], ['?', 67, False], [',', 37, False], ['.', 70, False], ['-', 56, False], ['_', 66, False], ['(', 53, False], [')', 92, False], ['*', 29, False], ['+', 5, False], ['/', 72, False], ['<', 75, False], ['>', 46, False], ['=', 8, False], ['@', 90, False], ['#', 49, False], ['$', 1, False], ['%', 64, False], ['^', 62, False], ['&', 68, False], ['{', 14, False], ['}', 45, False], ['[', 95, False], [']', 85, False], [';', 17, False], [':', 33, False], ['"', 47, False], ["'", 69, False], ['|', 34, False], ['\\', 23, False], ['~', 21, False], ['`', 94, False], [' ', 20, False], ['0', 58, False], ['1', 7, False], ['2', 32, False], ['3', 24, False], ['4', 74, False], ['5', 39, False], ['6', 13, False], ['7', 59, False], ['8', 80, False], ['9', 65, False]]
rotor2 = [['A', 104, False], ['B', 100, False], ['C', 33, False], ['D', 21, True], ['E', 83, False], ['F', 70, False], ['G', 93, False], ['H', 27, False], ['I', 53, False], ['J', 10, False], ['K', 54, False], ['L', 4, False], ['M', 36, False], ['N', 14, False], ['Ñ', 2, False], ['O', 23, False], ['P', 34, False], ['Q', 59, False], ['R', 89, False], ['S', 90, False], ['T', 87, False], ['U', 39, False], ['V', 94, False], ['W', 69, False], ['X', 63, False], ['Y', 32, False], ['Z', 28, False], ['a', 103, False], ['b', 19, False], ['c', 48, False], ['d', 91, False], ['e', 42, False], ['f', 82, False], ['g', 64, False], ['h', 77, False], ['i', 60, False], ['j', 15, False], ['k', 67, False], ['l', 98, False], ['m', 62, False], ['n', 49, False], ['ñ', 61, False], ['o', 66, False], ['p', 18, False], ['q', 55, False], ['r', 8, False], ['s', 29, False], ['t', 97, False], ['u', 17, False], ['v', 12, False], ['w', 68, False], ['x', 25, False], [
    'y', 7, False], ['z', 85, False], ['á', 11, False], ['é', 5, False], ['í', 76, False], ['ó', 16, False], ['ú', 78, False], ['ü', 31, False], ['¿', 79, False], ['¡', 50, False], ['!', 20, False], ['?', 86, False], [',', 47, False], ['.', 9, False], ['-', 75, False], ['_', 102, False], ['(', 73, False], [')', 101, False], ['*', 22, False], ['+', 37, False], ['/', 99, False], ['<', 52, False], ['>', 46, False], ['=', 24, False], ['@', 95, False], ['#', 58, False], ['$', 45, False], ['%', 1, False], ['^', 71, False], ['&', 3, False], ['{', 43, False], ['}', 72, False], ['[', 51, False], [']', 92, False], [';', 81, False], [':', 44, False], ['"', 35, False], ["'", 41, False], ['|', 56, False], ['\\', 40, False], ['~', 88, False], ['`', 0, False], [' ', 80, False], ['0', 84, False], ['1', 30, False], ['2', 6, False], ['3', 74, False], ['4', 65, False], ['5', 13, False], ['6', 26, False], ['7', 38, False], ['8', 96, False], ['9', 57, False]]
rotor3 = [['A', 94, False], ['B', 21, False], ['C', 52, False], ['D', 74, True], ['E', 33, False], ['F', 76, False], ['G', 69, False], ['H', 31, False], ['I', 10, False], ['J', 42, False], ['K', 14, False], ['L', 51, False], ['M', 1, False], ['N', 73, False], ['Ñ', 99, False], ['O', 0, False], ['P', 85, False], ['Q', 98, False], ['R', 41, False], ['S', 29, False], ['T', 95, False], ['U', 20, False], ['V', 38, False], ['W', 103, False], ['X', 56, False], ['Y', 84, False], ['Z', 18, False], ['a', 35, False], ['b', 75, False], ['c', 34, False], ['d', 59, False], ['e', 27, False], ['f', 80, False], ['g', 91, False], ['h', 16, False], ['i', 47, False], ['j', 68, False], ['k', 78, False], ['l', 64, False], ['m', 13, False], ['n', 82, False], ['ñ', 32, False], ['o', 101, False], ['p', 65, False], ['q', 92, False], ['r', 2, False], ['s', 19, False], ['t', 63, False], ['u', 58, False], ['v', 70, False], ['w', 11, False], ['x', 96, False], [
    'y', 100, False], ['z', 40, False], ['á', 53, False], ['é', 93, False], ['í', 57, False], ['ó', 77, False], ['ú', 81, False], ['ü', 39, False], ['¿', 8, False], ['¡', 90, False], ['!', 104, False], ['?', 24, False], [',', 46, False], ['.', 88, False], ['-', 15, False], ['_', 89, False], ['(', 87, False], [')', 25, False], ['*', 55, False], ['+', 12, False], ['/', 3, False], ['<', 23, False], ['>', 83, False], ['=', 37, False], ['@', 26, False], ['#', 4, False], ['$', 44, False], ['%', 36, False], ['^', 9, False], ['&', 50, False], ['{', 67, False], ['}', 28, False], ['[', 22, False], [']', 86, False], [';', 17, False], [':', 7, False], ['"', 43, False], ["'", 49, False], ['|', 48, False], ['\\', 54, False], ['~', 5, False], ['`', 71, False], [' ', 72, False], ['0', 6, False], ['1', 62, False], ['2', 60, False], ['3', 97, False], ['4', 30, False], ['5', 66, False], ['6', 79, False], ['7', 45, False], ['8', 61, False], ['9', 102, False]]
rotor4 = [['A', 13, False], ['B', 37, False], ['C', 24, False], ['D', 53, True], ['E', 84, False], ['F', 18, False], ['G', 87, False], ['H', 101, False], ['I', 55, False], ['J', 27, False], ['K', 86, False], ['L', 56, False], ['M', 91, False], ['N', 54, False], ['Ñ', 82, False], ['O', 23, False], ['P', 76, False], ['Q', 9, False], ['R', 41, False], ['S', 42, False], ['T', 96, False], ['U', 62, False], ['V', 33, False], ['W', 43, False], ['X', 100, False], ['Y', 34, False], ['Z', 40, False], ['a', 46, False], ['b', 66, False], ['c', 0, False], ['d', 57, False], ['e', 59, False], ['f', 103, False], ['g', 58, False], ['h', 19, False], ['i', 102, False], ['j', 22, False], ['k', 77, False], ['l', 48, False], ['m', 32, False], ['n', 69, False], ['ñ', 99, False], ['o', 78, False], ['p', 70, False], ['q', 12, False], ['r', 31, False], ['s', 45, False], ['t', 10, False], ['u', 14, False], ['v', 61, False], ['w', 36, False], ['x', 44, False], [
    'y', 73, False], ['z', 2, False], ['á', 7, False], ['é', 71, False], ['í', 90, False], ['ó', 64, False], ['ú', 47, False], ['ü', 79, False], ['¿', 20, False], ['¡', 97, False], ['!', 92, False], ['?', 65, False], [',', 4, False], ['.', 85, False], ['-', 80, False], ['_', 5, False], ['(', 50, False], [')', 60, False], ['*', 25, False], ['+', 67, False], ['/', 38, False], ['<', 51, False], ['>', 52, False], ['=', 81, False], ['@', 28, False], ['#', 21, False], ['$', 29, False], ['%', 16, False], ['^', 17, False], ['&', 68, False], ['{', 83, False], ['}', 93, False], ['[', 49, False], [']', 98, False], [';', 95, False], [':', 15, False], ['"', 104, False], ["'", 74, False], ['|', 26, False], ['\\', 39, False], ['~', 8, False], ['`', 89, False], [' ', 30, False], ['0', 35, False], ['1', 72, False], ['2', 63, False], ['3', 3, False], ['4', 88, False], ['5', 6, False], ['6', 11, False], ['7', 1, False], ['8', 94, False], ['9', 75, False]]
rotor5 = [['A', 17, False], ['B', 27, False], ['C', 51, False], ['D', 48, True], ['E', 10, False], ['F', 30, False], ['G', 97, False], ['H', 94, False], ['I', 66, False], ['J', 57, False], ['K', 101, False], ['L', 40, False], ['M', 95, False], ['N', 24, False], ['Ñ', 39, False], ['O', 41, False], ['P', 54, False], ['Q', 26, False], ['R', 69, False], ['S', 99, False], ['T', 23, False], ['U', 43, False], ['V', 21, False], ['W', 70, False], ['X', 18, False], ['Y', 25, False], ['Z', 72, False], ['a', 16, False], ['b', 28, False], ['c', 35, False], ['d', 60, False], ['e', 83, False], ['f', 3, False], ['g', 77, False], ['h', 31, False], ['i', 7, False], ['j', 37, False], ['k', 104, False], ['l', 1, False], ['m', 98, False], ['n', 85, False], ['ñ', 13, False], ['o', 49, False], ['p', 2, False], ['q', 56, False], ['r', 50, False], ['s', 38, False], ['t', 67, False], ['u', 47, False], ['v', 78, False], ['w', 100, False], ['x', 75, False], [
    'y', 89, False], ['z', 11, False], ['á', 33, False], ['é', 9, False], ['í', 74, False], ['ó', 19, False], ['ú', 92, False], ['ü', 81, False], ['¿', 63, False], ['¡', 55, False], ['!', 71, False], ['?', 15, False], [',', 79, False], ['.', 36, False], ['-', 73, False], ['_', 90, False], ['(', 84, False], [')', 5, False], ['*', 8, False], ['+', 82, False], ['/', 53, False], ['<', 62, False], ['>', 14, False], ['=', 102, False], ['@', 103, False], ['#', 91, False], ['$', 96, False], ['%', 68, False], ['^', 80, False], ['&', 0, False], ['{', 34, False], ['}', 88, False], ['[', 64, False], [']', 32, False], [';', 29, False], [':', 59, False], ['"', 22, False], ["'", 46, False], ['|', 4, False], ['\\', 86, False], ['~', 6, False], ['`', 52, False], [' ', 12, False], ['0', 65, False], ['1', 58, False], ['2', 20, False], ['3', 44, False], ['4', 87, False], ['5', 61, False], ['6', 45, False], ['7', 42, False], ['8', 76, False], ['9', 93, False]]
reflector = [16, 99, 39, 48, 3, 49, 38, 100, 43, 103, 5, 15, 10, 73, 94, 1, 85, 64, 102, 75, 69, 26, 54, 8, 24, 27, 47, 65, 63, 9, 88, 57, 97, 19, 34, 7, 101, 72, 18, 13, 78, 62, 53, 45, 70, 14, 2, 82, 89, 74, 67,
             37, 50, 60, 35, 91, 83, 76, 58, 59, 92, 71, 84, 55, 4, 80, 81, 20, 6, 21, 56, 41, 93, 17, 28, 32, 61, 23, 33, 46, 30, 0, 66, 11, 79, 68, 42, 12, 86, 44, 22, 25, 52, 51, 36, 40, 77, 95, 98, 29, 31, 90, 87, 96]
configuracion = ''
cantidad_rotores = 0
orden = ''
opcEnc = input('Deseas encriptar(Y) o desencriptar(N) ')
caracteres = input('ingresa una palabra a encriptar ')
salida = ''


def verificarConfig():
    for c in configuracion:
        if c not in alfabeto_espanol:
            return False

    return True


def getCountAndConf():
    global cantidad_rotores
    global configuracion
    correct = True
    cantidad_rotores = int(input(
        'Ingresa la cantidad de rotores a usar para encriptación o desencriptación de 1 a 5 '))
    configuracion = input(
        'Ingresa la configuración a usar recordando la cantidad de rotores a usar y que es sensible a minusculas y mayusculas ')
    while correct:
        if (verificarConfig()):
            if len(configuracion) == cantidad_rotores:
                print(
                    'la configuración se encuentra en el alfabeto español y tiene la misma catidad de rotores ')
                correct = False
            else:
                print(
                    'la configuración no tiene la misma cantidad de rotores, recordar que cada letra es 1 rotor ')
                configuracion = input(
                    'Ingresa de nuevo la configuración a usar recordando la cantidad de rotores a usar y que es sensible a minusculas y mayusculas')

        else:
            configuracion = input(
                'Ingresa de nuevo la configuración a usar recordando la cantidad de rotores a usar y recordando que es sensible a minusculas y mayusculas')


def getOrden():
    global orden
    orden = input(
        'digite el orden de los rotores(#5rotores) dependiendo del numero de rotorres 243: ')
    noCorrecto = True
    while noCorrecto:
        if len(orden) == cantidad_rotores:
            noCorrecto = False
            print('Orden correctamente digitado')
        else:
            print(orden, cantidad_rotores)
            orden = input(
                'digite de nuevo el orden de los rotores(#5rotores) dependiendo del numero de rotorres 243: ')


def ordernarRotores():
    global orden
    global rotor1
    global rotor2
    global rotor3
    global rotor4
    global rotor5
    finder = False
    for o in orden:
        if int(o) == 1:
            nuevo_rotor = []
            for r in rotor1:
                if r[0] == configuracion[orden.index(o)]:
                    finder = True
                if finder:
                    nuevo_rotor.append(r)
            for r in rotor1:
                if r[0] == configuracion[orden.index(o)]:
                    finder = False
                if finder:
                    nuevo_rotor.append(r)
            rotor1 = nuevo_rotor

        elif int(o) == 2:
            nuevo_rotor = []
            finder = False
            for r in rotor2:
                if r[0] == configuracion[orden.index(o)]:
                    finder = True
                if finder:
                    nuevo_rotor.append(r)
            for r in rotor2:
                if r[0] == configuracion[orden.index(o)]:
                    finder = False
                if finder:
                    nuevo_rotor.append(r)
            rotor2 = nuevo_rotor
        elif int(o) == 3:
            nuevo_rotor = []
            finder = False
            for r in rotor3:
                if r[0] == configuracion[orden.index(o)]:
                    finder = True
                if finder:
                    nuevo_rotor.append(r)
            for r in rotor3:
                if r[0] == configuracion[orden.index(o)]:
                    finder = False
                if finder:
                    nuevo_rotor.append(r)
            rotor3 = nuevo_rotor
        elif int(o) == 4:
            nuevo_rotor = []
            finder = False
            for r in rotor4:
                if r[0] == configuracion[orden.index(o)]:
                    finder = True
                if finder:
                    nuevo_rotor.append(r)
            for r in rotor4:
                if r[0] == configuracion[orden.index(o)]:
                    finder = False
                if finder:
                    nuevo_rotor.append(r)
            rotor4 = nuevo_rotor
        elif int(o) == 5:
            nuevo_rotor = []
            finder = False
            for r in rotor5:
                if r[0] == configuracion[orden.index(o)]:
                    finder = True
                if finder:
                    nuevo_rotor.append(r)
            for r in rotor5:
                if r[0] == configuracion[orden.index(o)]:
                    finder = False
                if finder:
                    nuevo_rotor.append(r)
            rotor5 = nuevo_rotor


def rotar():
    global orden
    global rotor1
    global rotor2
    global rotor3
    global rotor4
    global rotor5
    rotar_sgte = False
    for o in orden:
        if int(o) == 1:
            if orden.index(o) == 0:
                primerElemento = rotor1.pop(0)
                if primerElemento[2]:
                    rotar_sgte = True
                else:
                    rotar_sgte = False
                    rotor1.append(primerElemento)
            else:
                if rotor1[0][2] or rotar_sgte:
                    primerElemento = rotor1.pop(0)
                    if primerElemento[2]:
                        rotar_sgte = True
                    else:
                        rotar_sgte = False
                        rotor1.append(primerElemento)

        if int(o) == 2:
            if orden.index(o) == 0:
                primerElemento = rotor2.pop(0)
                if primerElemento[2]:
                    rotar_sgte = True
                else:
                    rotar_sgte = False
                    rotor2.append(primerElemento)
            else:
                if rotor2[0][2] or rotar_sgte:
                    primerElemento = rotor2.pop(0)
                    if primerElemento[2]:
                        rotar_sgte = True
                    else:
                        rotar_sgte = False
                        rotor2.append(primerElemento)
        if int(o) == 3:
            if orden.index(o) == 0:
                primerElemento = rotor3.pop(0)
                if primerElemento[2]:
                    rotar_sgte = True
                else:
                    rotar_sgte = False
                    rotor3.append(primerElemento)
            else:
                if rotor3[0][2] or rotar_sgte:
                    primerElemento = rotor3.pop(0)
                    if primerElemento[2]:
                        rotar_sgte = True
                    else:
                        rotar_sgte = False
                        rotor3.append(primerElemento)
        if int(o) == 4:
            if orden.index(o) == 0:
                primerElemento = rotor4.pop(0)
                if primerElemento[2]:
                    rotar_sgte = True
                else:
                    rotar_sgte = False
                    rotor4.append(primerElemento)
            else:
                if rotor4[0][2] or rotar_sgte:
                    primerElemento = rotor4.pop(0)
                    if primerElemento[2]:
                        rotar_sgte = True
                    else:
                        rotar_sgte = False
                        rotor4.append(primerElemento)
        if int(o) == 5:
            if orden.index(o) == 0:
                primerElemento = rotor5.pop(0)
                if primerElemento[2]:
                    rotar_sgte = True
                else:
                    rotar_sgte = False
                    rotor5.append(primerElemento)
            else:
                if rotor5[0][2] or rotar_sgte:
                    primerElemento = rotor5.pop(0)
                    if primerElemento[2]:
                        rotar_sgte = True
                    else:
                        rotar_sgte = False
                        rotor5.append(primerElemento)


def encriptar(caracter):
    apuntador = 0
    rotar()
    indexInput = alfabeto_espanol.index(caracter)

    # encriptar hacia reflector
    for o in orden:
        if int(o) == 1:
            if orden.index(o) == 0:
                if opcEnc.lower() == 'y':
                    apuntador = rotor1[indexInput][1]
                elif opcEnc.lower() == 'n':
                    for rot in rotor1:
                        if rot[1] == indexInput:
                            apuntador = rotor1.index(rot)
                            break
            else:
                if opcEnc.lower() == 'y':
                    apuntador = rotor1[apuntador][1]
                elif opcEnc.lower() == 'n':
                    for rot in rotor1:
                        if rot[1] == apuntador:
                            apuntador = rotor1.index(rot)
                            break

        if int(o) == 2:
            if orden.index(o) == 0:
                if opcEnc.lower() == 'y':
                    apuntador = rotor2[indexInput][1]
                elif opcEnc.lower() == 'n':
                    for rot in rotor2:
                        if rot[1] == indexInput:
                            apuntador = rotor2.index(rot)
                            break
            else:
                if opcEnc.lower() == 'y':
                    apuntador = rotor2[apuntador][1]
                elif opcEnc.lower() == 'n':
                    for rot in rotor2:
                        if rot[1] == apuntador:
                            apuntador = rotor2.index(rot)
                            break

        if int(o) == 3:
            if orden.index(o) == 0:
                if opcEnc.lower() == 'y':
                    apuntador = rotor3[indexInput][1]
                elif opcEnc.lower() == 'n':
                    for rot in rotor3:
                        if rot[1] == indexInput:
                            apuntador = rotor3.index(rot)
                            break
            else:
                if opcEnc.lower() == 'y':
                    apuntador = rotor3[apuntador][1]
                elif opcEnc.lower() == 'n':
                    for rot in rotor3:
                        if rot[1] == apuntador:
                            apuntador = rotor3.index(rot)
                            break

        if int(o) == 4:
            if orden.index(o) == 0:
                if opcEnc.lower() == 'y':
                    apuntador = rotor4[indexInput][1]
                elif opcEnc.lower() == 'n':
                    for rot in rotor4:
                        if rot[1] == indexInput:
                            apuntador = rotor4.index(rot)
                            break
            else:
                if opcEnc.lower() == 'y':
                    apuntador = rotor4[apuntador][1]
                elif opcEnc.lower() == 'n':
                    for rot in rotor4:
                        if rot[1] == apuntador:
                            apuntador = rotor4.index(rot)
                            break

        if int(o) == 5:
            if orden.index(o) == 0:
                if opcEnc.lower() == 'y':
                    apuntador = rotor5[indexInput][1]
                elif opcEnc.lower() == 'n':
                    for rot in rotor5:
                        if rot[1] == indexInput:
                            apuntador = rotor5.index(rot)
                            break
            else:
                if opcEnc.lower() == 'y':
                    apuntador = rotor5[apuntador][1]
                elif opcEnc.lower() == 'n':
                    for rot in rotor5:
                        if rot[1] == apuntador:
                            apuntador = rotor5.index(rot)
                            break

    # encriptar desde reflector hacia output en el alfabeto
    if opcEnc.lower() == 'y':
        apuntador = reflector[apuntador]
    elif opcEnc.lower() == 'n':
        for ref in reflector:
            if ref == apuntador:
                apuntador = reflector.index(ref)
                break

    for i in range((cantidad_rotores - 1), -1, -1):
        order = int(orden[i])
        if order == 1:
            if orden.index(str(order)) == 0:
                if opcEnc.lower() == 'y':
                    apuntador = rotor1[apuntador][1]
                elif opcEnc.lower() == 'n':
                    for rot in rotor1:
                        if rot[1] == apuntador:
                            apuntador = rotor1.index(rot)
                            break
            else:
                if opcEnc.lower() == 'y':
                    apuntador = rotor1[apuntador][1]
                    break
                elif opcEnc.lower() == 'n':
                    for rot in rotor1:
                        if rot[1] == apuntador:
                            apuntador = rotor1.index(rot)
                            break

        if order == 2:
            if orden.index(str(order)) == 0:
                if opcEnc.lower() == 'y':
                    apuntador = rotor2[apuntador][1]
                    break
                elif opcEnc.lower() == 'n':
                    for rot in rotor2:
                        if rot[1] == apuntador:
                            apuntador = rotor2.index(rot)
                            break
            else:
                if opcEnc.lower() == 'y':
                    apuntador = rotor2[apuntador][1]
                elif opcEnc.lower() == 'n':
                    for rot in rotor2:
                        if rot[1] == apuntador:
                            apuntador = rotor2.index(rot)
                            break
        if order == 3:
            if orden.index(str(order)) == 0:
                if opcEnc.lower() == 'y':
                    apuntador = rotor3[apuntador][1]
                elif opcEnc.lower() == 'n':
                    for rot in rotor3:
                        if rot[1] == apuntador:
                            apuntador = rotor3.index(rot)
                            break
            else:
                if opcEnc.lower() == 'y':
                    apuntador = rotor3[apuntador][1]
                elif opcEnc.lower() == 'n':
                    for rot in rotor3:
                        if rot[1] == apuntador:
                            apuntador = rotor3.index(rot)
                            break
        if order == 4:
            if orden.index(str(order)) == 0:
                if opcEnc.lower() == 'y':
                    apuntador = rotor4[apuntador][1]
                elif opcEnc.lower() == 'n':
                    for rot in rotor4:
                        if rot[1] == apuntador:
                            apuntador = rotor4.index(rot)
                            break
            else:
                if opcEnc.lower() == 'y':
                    apuntador = rotor4[apuntador][1]
                elif opcEnc.lower() == 'n':
                    for rot in rotor4:
                        if rot[1] == apuntador:
                            apuntador = rotor4.index(rot)
                            break
        if order == 5:
            if orden.index(str(order)) == 0:
                if opcEnc.lower() == 'y':
                    apuntador = rotor5[apuntador][1]
                elif opcEnc.lower() == 'n':
                    for rot in rotor5:
                        if rot[1] == apuntador:
                            apuntador = rotor5.index(rot)
                            break
            else:
                if opcEnc.lower() == 'y':
                    apuntador = rotor5[apuntador][1]
                elif opcEnc.lower() == 'n':
                    for rot in rotor5:
                        if rot[1] == apuntador:
                            apuntador = rotor5.index(rot)
                            break
    return alfabeto_espanol[apuntador]


def enigma():
    global salida
    # coger letra
    for caracter in caracteres:
        encriptada = encriptar(caracter)
        salida = salida + encriptada
    print('Encriptado:')
    print(salida)


# inicia proceso
getCountAndConf()
getOrden()
ordernarRotores()
enigma()
