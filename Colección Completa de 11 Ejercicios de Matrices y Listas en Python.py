import random

# =========================
# Utilidades y validaciones
# =========================
# En esta sección definimos funciones de uso general que se reutilizan
# en varios ejercicios. Separar utilidades facilita probar y mantener el código.

def pedir_entero(mensaje, minimo=None, maximo=None):
    """
    Pide un entero al usuario con validación de tipo y de rango.

    Parámetros:
    - mensaje: texto que se muestra al usuario para solicitar el número.
    - minimo: si se indica, el valor introducido debe ser >= minimo.
    - maximo: si se indica, el valor introducido debe ser <= maximo.

    Flujo:
    - Repite hasta que el usuario introduzca un entero válido.
    - Maneja ValueError si el usuario pone letras o números no enteros.
    - Comprueba rango si se han proporcionado minimo/maximo.
    - Devuelve el entero validado.
    """
    while True:
        try:
            # Intentamos convertir la entrada a entero
            valor = int(input(mensaje))
            # Validación de límite inferior (si se proporcionó)
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser >= {minimo}.")
                continue  # Pide de nuevo
            # Validación de límite superior (si se proporcionó)
            if maximo is not None and valor > maximo:
                print(f"El valor debe ser <= {maximo}.")
                continue  # Pide de nuevo
            return valor  # Valor válido: lo devolvemos
        except ValueError:
            # Si la conversión a entero falla, mostramos mensaje y repetimos
            print("Entrada inválida. Debes ingresar un número entero.")


def imprimir_matriz(matriz, ancho=4):
    """
    Imprime una matriz (lista de listas) con columnas alineadas.

    Parámetros:
    - matriz: lista de listas (cada sublista es una fila).
    - ancho: ancho mínimo para cada elemento (útil para alinear números).
    """
    # Recorremos cada fila y construimos una cadena con los elementos alineados
    for fila in matriz:
        # f"{elem:>{ancho}}" -> derecha-justificado con ancho fijo
        print(" ".join(f"{elem:>{ancho}}" for elem in fila))
    print()  # Línea en blanco después de la matriz para claridad


def crear_matriz(filas, columnas, valor=0):
    """
    Crea e inicializa una matriz (lista de listas) con un valor por defecto.

    - Evita compartir la misma lista interna usando comprensión anidada.
    - Devuelve una matriz con 'filas' filas y 'columnas' columnas inicializadas a 'valor'.
    """
    return [[valor for _ in range(columnas)] for _ in range(filas)]


# =========================
# Ejercicio 1
# =========================

def ejercicio_1():
    """
    Crea una matriz 3x3 con los números del 1 al 9 y la imprime.
    - Mantenemos un contador que va incrementando para rellenar la matriz.
    - Se construye fila a fila y al final se imprime con imprimir_matriz.
    """
    matriz = []
    contador = 1  # Primer número a insertar
    for _ in range(3):          # Repetir 3 veces para las 3 filas
        fila = []
        for _ in range(3):      # Repetir 3 veces para las 3 columnas
            fila.append(contador)  # Insertar contador en la fila
            contador += 1          # Incrementar el contador
        matriz.append(fila)     # Añadir la fila completa a la matriz

    print("Matriz 3x3 con números del 1 al 9:")
    imprimir_matriz(matriz)     # Mostrar la matriz en formato legible


# =========================
# Ejercicio 2
# =========================

def ejercicio_2():
    """
    Crea una matriz de 5 filas y n columnas (n introducido por usuario).
    - Rellena con números aleatorios entre 0 y 10 inclusive.
    - Utiliza comprensión de listas para crear la matriz de forma compacta.
    """
    n = pedir_entero("Número de columnas (n): ", minimo=1)  # Validamos n>=1
    # Creación: por cada una de las 5 filas generamos n números aleatorios
    matriz = [[random.randint(0, 10) for _ in range(n)] for _ in range(5)]

    print("Matriz 5 x n con aleatorios entre 0 y 10:")
    imprimir_matriz(matriz)


# =========================
# Ejercicio 3
# =========================

def ejercicio_3():
    """
    Crea dos matrices cuadradas A y B de tamaño n x n (n introducido por usuario),
    con valores aleatorios, y calcula su suma elemento a elemento en C.

    - A y B son matrices con números [0..9].
    - C[i][j] = A[i][j] + B[i][j].
    - Imprime A, B y C.
    """
    n = pedir_entero("Tamaño n para matrices n x n: ", minimo=1)
    # Generamos A y B con comprehension anidadas
    A = [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]
    B = [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]
    # Construimos C sumando elemento a elemento
    C = [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

    print("Matriz A:")
    imprimir_matriz(A)
    print("Matriz B:")
    imprimir_matriz(B)
    print("Suma C = A + B:")
    imprimir_matriz(C)


# =========================
# Ejercicio 4
# =========================
# Aquí definimos funciones auxiliares para operaciones sobre matrices cuadradas.

def suma_fila(matriz, idx):
    """Devuelve la suma de los elementos de la fila con índice idx."""
    return sum(matriz[idx])  # sum() suma todos los elementos de la lista fila

def suma_columna(matriz, idx):
    """Devuelve la suma de los elementos de la columna idx."""
    # Recorremos cada fila y extraemos el elemento en la columna idx
    return sum(fila[idx] for fila in matriz)

def suma_diagonal_principal(matriz):
    """Suma la diagonal principal (posiciones [0,0], [1,1], ...)."""
    return sum(matriz[i][i] for i in range(len(matriz)))

def suma_diagonal_inversa(matriz):
    """Suma la diagonal inversa (posiciones [0,n-1], [1,n-2], ...)."""
    n = len(matriz)
    return sum(matriz[i][n - 1 - i] for i in range(n))

def media_matriz(matriz):
    """
    Calcula la media aritmética de todos los valores de la matriz.
    - total: suma de todos los elementos
    - elementos: número total de celdas (filas * columnas)
    """
    total = sum(sum(fila) for fila in matriz)
    elementos = len(matriz) * len(matriz[0])
    return total / elementos if elementos > 0 else 0


def ejercicio_4():
    """
    Implementa un menú para operar sobre una matriz 4x4.
    Restricción importante:
      - No se pueden ejecutar las operaciones (2..6) hasta que la matriz
        haya sido rellenada por la opción 1.
    - La opción 1 rellena la matriz con aleatorios y marca 'rellena=True'.
    - El menú loop se repite hasta que el usuario elija salir (0).
    """
    n = 4
    matriz = crear_matriz(n, n, 0)  # Inicializamos matriz con ceros para tener estructura
    rellena = False  # Bandera que indica si se ha rellenado la matriz

    while True:
        print("Menú (matriz 4x4):")
        print("1. Rellenar TODA la matriz con aleatorios")
        print("2. Sumar una fila")
        print("3. Sumar una columna")
        print("4. Sumar diagonal principal")
        print("5. Sumar diagonal inversa")
        print("6. Media de todos los valores")
        print("0. Salir")
        opcion = pedir_entero("Elige una opción: ", minimo=0, maximo=6)

        if opcion == 0:
            break  # Salimos del bucle del menú y de la función

        if opcion == 1:
            # Rellenamos la matriz con valores aleatorios entre 0 y 20
            matriz = [[random.randint(0, 20) for _ in range(n)] for _ in range(n)]
            rellena = True
            print("Matriz rellenada:")
            imprimir_matriz(matriz)
            continue  # Volvemos al inicio del bucle para mostrar el menú

        # Si no se ha rellenado la matriz aún, las opciones 2..6 no deben ejecutarse
        if not rellena:
            print("Debes rellenar la matriz primero (opción 1).")
            continue

        # A partir de aquí, rellena == True, podemos ejecutar las operaciones
        if opcion == 2:
            idx = pedir_entero(f"Índice de fila [0..{n-1}]: ", minimo=0, maximo=n-1)
            print(f"Suma de la fila {idx}: {suma_fila(matriz, idx)}")
        elif opcion == 3:
            idx = pedir_entero(f"Índice de columna [0..{n-1}]: ", minimo=0, maximo=n-1)
            print(f"Suma de la columna {idx}: {suma_columna(matriz, idx)}")
        elif opcion == 4:
            print(f"Suma diagonal principal: {suma_diagonal_principal(matriz)}")
        elif opcion == 5:
            print(f"Suma diagonal inversa: {suma_diagonal_inversa(matriz)}")
        elif opcion == 6:
            print(f"Media de la matriz: {media_matriz(matriz):.3f}")


# =========================
# Ejercicio 5
# =========================

def ejercicio_5():
    """
    Genera una matriz 3x3 con números aleatorios sin repetirse.
    En lugar de intentar generar números únicos aleatoriamente (lo que puede ser
    ineficiente), construimos la lista [1..9], la barajamos y la colocamos por filas.
    """
    numeros = list(range(1, 10))  # Lista con los números 1 a 9
    random.shuffle(numeros)       # Mezclamos la lista en sitio (in-place)
    # Repartimos la lista en 3 sublistas (3 elementos cada una)
    matriz = [numeros[i*3:(i+1)*3] for i in range(3)]

    print("Matriz 3x3 sin repetidos:")
    imprimir_matriz(matriz)


# =========================
# Ejercicio 6
# =========================

def ejercicio_6():
    """
    Genera una matriz de tamaño filas x columnas con números aleatorios.
    Luego elige ALEATORIAMENTE si sumar una fila o una columna, y cuál índice usar.
    - Elegir fila o columna se hace con random.choice([True, False]).
    - Se muestra el resultado y cuál fue la elección aleatoria.
    """
    filas = pedir_entero("Número de filas: ", minimo=1)
    columnas = pedir_entero("Número de columnas: ", minimo=1)
    matriz = [[random.randint(0, 9) for _ in range(columnas)] for _ in range(filas)]
    print("Matriz generada:")
    imprimir_matriz(matriz)

    # Decisión aleatoria: True -> fila, False -> columna
    elegir_fila = random.choice([True, False])
    if elegir_fila:
        # Elegimos un índice de fila aleatorio dentro del rango válido
        idx = random.randint(0, filas - 1)
        total = suma_fila(matriz, idx)
        print(f"Se eligió ALEATORIAMENTE la FILA {idx}. Suma = {total}")
    else:
        # Elegimos un índice de columna aleatorio dentro del rango válido
        idx = random.randint(0, columnas - 1)
        total = suma_columna(matriz, idx)
        print(f"Se eligió ALEATORIAMENTE la COLUMNA {idx}. Suma = {total}")


# =========================
# Ejercicio 7 (3 en raya)
# =========================

def hay_ganador(tablero, marca):
    """
    Comprueba si el jugador con 'marca' (por ejemplo 'X' o 'O') ha ganado.
    - Revisa todas las filas: si alguna fila entera contiene la marca, hay ganador.
    - Revisa todas las columnas: misma lógica que filas.
    - Revisa las dos diagonales.
    Devuelve True si hay victoria, False en caso contrario.
    """
    # Revisar filas y columnas
    for i in range(3):
        if all(tablero[i][j] == marca for j in range(3)):  # fila i completa
            return True
        if all(tablero[j][i] == marca for j in range(3)):  # columna i completa
            return True
    # Diagonal principal
    if all(tablero[i][i] == marca for i in range(3)):
        return True
    # Diagonal inversa
    if all(tablero[i][2 - i] == marca for i in range(3)):
        return True
    return False

def tablero_lleno(tablero):
    """
    Devuelve True si no hay posiciones vacías ('-') en el tablero.
    - Usamos una comprensión que recorre todas las filas y todos los caracteres.
    """
    return all(c != '-' for fila in tablero for c in fila)

def imprimir_tablero(tablero):
    """Impresión simple y clara del tablero 3x3 para el juego."""
    for fila in tablero:
        print(" ".join(fila))
    print()

def ejercicio_7():
    """
    Juego 3 en raya (tic-tac-toe) para dos jugadores humanos:
    - tablero inicial con '-' indicando casilla vacía.
    - jugador_actual alterna entre 'X' y 'O'.
    - Se valida que la posición elegida esté dentro del rango y esté vacía.
    - Tras colocar la marca, se comprueba si hay ganador o si el tablero está lleno.
    """
    tablero = [['-' for _ in range(3)] for _ in range(3)]
    jugador_actual = 'X'

    while True:
        print(f"Turno del jugador {jugador_actual}:")
        imprimir_tablero(tablero)

        # Pedimos fila y columna validadas (0..2)
        fila = pedir_entero("Fila [0..2]: ", minimo=0, maximo=2)
        col = pedir_entero("Columna [0..2]: ", minimo=0, maximo=2)

        # Comprobamos que la casilla esté libre
        if tablero[fila][col] != '-':
            print("Posición ocupada. Elige otra.")
            continue  # Volvemos a pedir otra posición

        # Colocamos la marca
        tablero[fila][col] = jugador_actual

        # Comprobamos estado del juego: victoria o empate
        if hay_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"¡Gana {jugador_actual}!")
            break

        if tablero_lleno(tablero):
            imprimir_tablero(tablero)
            print("Empate: no hay más posiciones.")
            break

        # Alternamos jugador
        jugador_actual = 'O' if jugador_actual == 'X' else 'X'


# =========================
# Ejercicio 8 (Encuesta)
# =========================

def ejercicio_8():
    """
    Simula una encuesta a 10 personas con campos:
      - sexo: 1=masculino, 2=femenino
      - trabaja: 1=sí, 2=no
      - sueldo: si trabaja, número entre 600 y 2000; si no, 0
    Calcula porcentajes y sueldos promedio por grupo.
    - Los datos se generan aleatoriamente para simplificar la demostración.
    """
    n = 10
    encuesta = []
    for _ in range(n):
        sexo = random.randint(1, 2)
        trabaja = random.randint(1, 2)
        sueldo = random.randint(600, 2000) if trabaja == 1 else 0
        encuesta.append((sexo, trabaja, sueldo))

    # Cálculos de totales y promedios
    hombres = sum(1 for s, _, _ in encuesta if s == 1)
    mujeres = n - hombres
    hombres_trabajan = sum(1 for s, t, _ in encuesta if s == 1 and t == 1)
    mujeres_trabajan = sum(1 for s, t, _ in encuesta if s == 2 and t == 1)

    sueldos_hombres = [sueldo for s, t, sueldo in encuesta if s == 1 and t == 1]
    sueldos_mujeres = [sueldo for s, t, sueldo in encuesta if s == 2 and t == 1]

    pct_hombres = 100 * hombres / n
    pct_mujeres = 100 * mujeres / n
    pct_hombres_trabajan = 100 * hombres_trabajan / n
    pct_mujeres_trabajan = 100 * mujeres_trabajan / n

    prom_hombres = sum(sueldos_hombres) / len(sueldos_hombres) if sueldos_hombres else 0
    prom_mujeres = sum(sueldos_mujeres) / len(sueldos_mujeres) if sueldos_mujeres else 0

    # Salida de los resultados con formato legible
    print("Datos generados (sexo, trabaja, sueldo):")
    print(encuesta)
    print(f"Porcentaje de hombres: {pct_hombres:.1f}%")
    print(f"Porcentaje de mujeres: {pct_mujeres:.1f}%")
    print(f"Porcentaje de hombres que trabajan: {pct_hombres_trabajan:.1f}%")
    print(f"Porcentaje de mujeres que trabajan: {pct_mujeres_trabajan:.1f}%")
    print(f"Sueldo promedio de hombres que trabajan: {prom_hombres:.2f}")
    print(f"Sueldo promedio de mujeres que trabajan: {prom_mujeres:.2f}")


# =========================
# Ejercicio 9
# =========================

def seleccion_sort(lista):
    """
    Ordenamiento por selección (Selection Sort) sobre una lista en sitio.
    - Propósito didáctico: explicar cómo funciona un algoritmo O(n^2).
    - No es el método más eficiente para listas grandes (usar .sort() o sorted()).
    """
    n = len(lista)
    for i in range(n - 1):
        min_idx = i
        # Buscamos el mínimo en la parte no ordenada
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        # Si encontramos un mínimo distinto de i, intercambiamos
        if min_idx != i:
            lista[i], lista[min_idx] = lista[min_idx], lista[i]


def ejercicio_9():
    """
    Crea una matriz 5x5 con números aleatorios (0..99) y realiza:
      - Promedio de todos los elementos.
      - Determinar el mayor y cuántas veces aparece.
      - Mostrar todos los números pares.
      - Sumar diagonal principal.
      - Sumar la última fila.
      - Ordenar todos los elementos y reconstruir una matriz ordenada.
    """
    n = 5
    matriz = [[random.randint(0, 99) for _ in range(n)] for _ in range(n)]
    print("Matriz original 5x5:")
    imprimir_matriz(matriz)

    # Cálculo del promedio
    total = sum(sum(fila) for fila in matriz)
    promedio = total / (n * n)
    print(f"Promedio de la matriz: {promedio:.3f}")

    # Encontrar máximo y número de repeticiones
    plano = [elem for fila in matriz for elem in fila]  # convertimos a lista plana
    maximo = max(plano)
    repeticiones = sum(1 for x in plano if x == maximo)
    print(f"Número mayor: {maximo}, se repite {repeticiones} veces")

    # Extraer números pares de la lista plana
    pares = [x for x in plano if x % 2 == 0]
    print(f"Números pares ({len(pares)}): {pares}")

    # Suma diagonal principal
    diag_principal = suma_diagonal_principal(matriz)
    print(f"Suma diagonal principal: {diag_principal}")

    # Suma de la última fila (índice -1)
    suma_ultima_fila = sum(matriz[-1])
    print(f"Suma de la última fila: {suma_ultima_fila}")

    # Ordenamiento: ordenamos la lista plana y la repartimos por filas
    seleccion_sort(plano)
    matriz_ordenada = [plano[i*n:(i+1)*n] for i in range(n)]
    print("Matriz ordenada ascendentemente:")
    imprimir_matriz(matriz_ordenada)


# =========================
# Ejercicio 10
# =========================

def ejercicio_10():
    """
    Lee por teclado una matriz 5x4 (20 enteros), la imprime y muestra:
      - Mayor y sus posiciones.
      - Menor y sus posiciones.
    - Usamos pedir_entero para validar cada entrada.
    """
    filas, columnas = 5, 4
    matriz = []
    print(f"Introduce {filas * columnas} enteros para una matriz {filas}x{columnas}:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = pedir_entero(f"Elemento [{i},{j}]: ")
            fila.append(valor)
        matriz.append(fila)

    print("Matriz leída:")
    imprimir_matriz(matriz)

    plano = [elem for fila in matriz for elem in fila]
    mayor = max(plano)
    menor = min(plano)
    # Buscamos todas las posiciones donde aparece el mayor/menor
    pos_mayor = [(i, j) for i in range(filas) for j in range(columnas) if matriz[i][j] == mayor]
    pos_menor = [(i, j) for i in range(filas) for j in range(columnas) if matriz[i][j] == menor]

    print(f"Mayor: {mayor}, posiciones: {pos_mayor}")
    print(f"Menor: {menor}, posiciones: {pos_menor}")


# =========================
# Ejercicio 11
# =========================

def ejercicio_11():
    """
    Crea una matriz irregular (filas con distinto número de columnas).
    - El usuario indica cuántas filas (>=2).
    - Para cada fila, el usuario indica cuántas columnas (>=1).
    - Cada celda se rellena con un entero random entre 1 y 5.
    - Se imprime la matriz y la longitud de cada fila para clarificar la irregularidad.
    """
    filas = pedir_entero("Número de filas (>=2): ", minimo=2)
    matriz = []
    for i in range(filas):
        cols = pedir_entero(f"Número de columnas en fila {i} (>=1): ", minimo=1)
        fila = [random.randint(1, 5) for _ in range(cols)]
        matriz.append(fila)

    print("Matriz irregular generada:")
    for i, fila in enumerate(matriz):
        print(f"Fila {i} ({len(fila)} col): {fila}")


# =========================
# Menú principal
# =========================

def menu_principal():
    while True:
        print("\n======= MENÚ DE EJERCICIOS DE MATRICES =======")
        print("1. Ejercicio 1: Matriz 3x3 con números del 1 al 9")
        print("2. Ejercicio 2: Matriz 5xn con números aleatorios")
        print("3. Ejercicio 3: Suma de dos matrices n x n")
        print("4. Ejercicio 4: Menú de operaciones sobre matriz 4x4")
        print("5. Ejercicio 5: Matriz 3x3 sin números repetidos")
        print("6. Ejercicio 6: Suma aleatoria de fila o columna")
        print("7. Ejercicio 7: Juego del 3 en raya")
        print("8. Ejercicio 8: Encuesta a 10 personas")
        print("9. Ejercicio 9: Operaciones varias sobre matriz 5x5")
        print("10. Ejercicio 10: Leer matriz 5x4 desde teclado")
        print("11. Ejercicio 11: Matriz irregular generada")
        print("0. Salir")
        print("==============================================")

        opcion = pedir_entero("Elige un ejercicio (0-11): ", minimo=0, maximo=11)

        if opcion == 0:
            print("Saliendo del programa... ¡Hasta luego!")
            break
        elif opcion == 1: ejercicio_1()
        elif opcion == 2: ejercicio_2()
        elif opcion == 3: ejercicio_3()
        elif opcion == 4: ejercicio_4()
        elif opcion == 5: ejercicio_5()
        elif opcion == 6: ejercicio_6()
        elif opcion == 7: ejercicio_7()
        elif opcion == 8: ejercicio_8()
        elif opcion == 9: ejercicio_9()
        elif opcion == 10: ejercicio_10()
        elif opcion == 11: ejercicio_11()


# =========================
# Punto de entrada
# =========================
if __name__ == "__main__":
    menu_principal()