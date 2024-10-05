# Función que verifica la longitud de una palabra ingresada
def verificar_longitud_palabra(palabra):
    # Calcula la longitud de la palabra usando la función len()
    longitud = len(palabra)
    
    # Verifica si la longitud está en el rango correcto (entre 4 y 8 caracteres)
    if 4 <= longitud <= 8:
        print("La palabra es correcta.")
    # Si la palabra tiene menos de 4 caracteres, muestra un mensaje indicando cuántas letras faltan
    elif longitud < 4:
        print(f"Hacen falta letras. Solo tiene {longitud} letras.")
    # Si la palabra tiene más de 8 caracteres, muestra un mensaje indicando cuántas letras sobran
    else:
        print(f"Sobran letras. Tiene {longitud} letras.")

# Bucle para solicitar una palabra válida al usuario (sin espacios vacíos)
while True:
    palabra_ingresada = input("Ingresa una palabra: ").strip()
    if palabra_ingresada:
        break  # Sale del bucle si el usuario ingresa una palabra válida
    else:
        print("Por favor, ingresa una palabra válida.")  # Pide una nueva entrada si está vacía

# Llama a la función para verificar la longitud de la palabra ingresada
verificar_longitud_palabra(palabra_ingresada)

# Función que identifica en qué cuadrante está un punto en el plano cartesiano
def identificar_cuadrante(x, y):
    # Verifica si alguna de las coordenadas es igual a 0, lo que no es permitido
    if x == 0 or y == 0:
        print("Las coordenadas no deben ser 0.")
    # Si ambas coordenadas son positivas, el punto está en el cuadrante I
    elif x > 0 and y > 0:
        print("El punto se encuentra en el cuadrante I.")
    # Si X es negativa y Y es positiva, el punto está en el cuadrante II
    elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II.")
    # Si ambas coordenadas son negativas, el punto está en el cuadrante III
    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III.")
    # Si X es positiva y Y es negativa, el punto está en el cuadrante IV
    elif x > 0 and y < 0:
        print("El punto se encuentra en el cuadrante IV.")

# Bucle para solicitar las coordenadas X e Y al usuario, validando que sean numéricas
while True:
    try:
        # Pide al usuario que ingrese un valor numérico para X e Y
        x = float(input("Ingrese X (valor numérico): "))
        y = float(input("Ingrese Y (valor numérico): "))
        break  # Sale del bucle si los valores ingresados son válidos
    except ValueError:
        # Muestra un mensaje de error si el usuario no ingresa un número
        print("Por favor, ingrese valores numéricos válidos.")

# Llama a la función para identificar el cuadrante basado en las coordenadas ingresadas
identificar_cuadrante(x, y)
