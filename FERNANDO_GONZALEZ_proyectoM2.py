def longitud_palabra(palabra):
    if 4 <= len(palabra) <= 8:
        return f"La palabra '{palabra}' es correcta"
    elif len(palabra) < 4:
        return f"Hacen falta letras. La palabra '{palabra}' solo tiene {len(palabra)} letras"
    else:
        return f"Sobran letras. La palabra '{palabra}' tiene {len(palabra)} letras"

while True:
    palabra = input("Ingresa una palabra: ")
    resultado = longitud_palabra(palabra)
    print(resultado)
    
    if 4 <= len(palabra) <= 8:
        break



#CÓDIGO PARA ENCONTRAR EL CUADRANTE 
def encontrar_cuadrante(x, y):
    if x > 0 and y > 0:
        return "El punto se encuentra en el cuadrante I"
    elif x < 0 and y > 0:
        return "El punto se encuentra en el cuadrante II"
    elif x < 0 and y < 0:
        return "El punto se encuentra en el cuadrante III"
    elif x > 0 and y < 0:
        return "El punto se encuentra en el cuadrante IV"
    else:
        return "El punto no pertenece a ningún cuadrante (coordenadas en el origen)"

while True:
    print("\n ENCONTRAR EL CUADRANTE.")
    x = float(input("Ingrese X: "))
    y = float(input("Ingrese Y: "))
    
    if x == 0 or y == 0:
        print("Ninguna coordenada debe ser igual a 0. Por favor, inténtalo de nuevo.")
    else:
        resultado = encontrar_cuadrante(x, y)
        print(resultado)
    
    continuar = input("¿Desea ingresar otras coordenadas? (S/N): ")
    if continuar.upper() != 'S':
        break
