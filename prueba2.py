def calcular_promedio():
    print("Calculadora de Promedio")
    print("------------------------")
    try:
        # Pedir al usuario que ingrese los números separados por comas
        numeros = input("Introduce una lista de números separados por comas: ")
        
        # Convertir la entrada en una lista de números
        lista_numeros = [float(num) for num in numeros.split(",")]
        
        # Calcular el promedio
        promedio = sum(lista_numeros) / len(lista_numeros)
        
        print(f"El promedio de los números ingresados es: {promedio:.2f}")
    except ValueError:
        print("Error: Por favor, asegúrate de ingresar solo números separados por comas.")
    except ZeroDivisionError:
        print("Error: La lista no puede estar vacía.")

# Punto de entrada principal
if __name__ == "__main__":
    #Metodo principal
    calcular_promedio()
