print("este archivo es un archivo modificado por mi")
x = 6
y = 9
c = xwhile x < y:
    print("bucle infinito")
    
    """
Algoritmo Genético simple en Python
Evoluciona una población de cadenas hasta igualar la frase objetivo.
Ejecutar: python ga_frase.py
"""

import random
import string

# --- Parámetros (ajustables) ---
OBJETIVO = "hola mundo"             # frase objetivo
POP_SIZE = 200                      # tamaño de la población
MUTATION_RATE = 0.01                # probabilidad de mutación por carácter
TOURNAMENT_SIZE = 5                 # tamaño del torneo para selección
MAX_GENERATIONS = 1000              # número máximo de generaciones
ELITISM = True                      # conservar mejor individuo

# Caracteres permitidos (puedes ampliarlo)
CHARSET = string.ascii_lowercase + " ,.!?;:áéíóúñ"  # incluir acentos si usas español

# --- Funciones de GA ---
def random_char():
    return random.choice(CHARSET)

def random_individual(length):
    return ''.join(random_char() for _ in range(length))

def fitness(individuo):
    """Fitness = cantidad de caracteres que coinciden en la misma posición."""
    puntuacion = sum(1 for a, b in zip(individuo, OBJETIVO) if a == b)
    return puntuacion

def torneo_seleccion(poblacion, k=TOURNAMENT_SIZE):
    """Selecciona un individuo por torneo."""
    participantes = random.sample(poblacion, k)
    # ordenar por fitness descendente y devolver el mejor
    return max(participantes, key=fitness)

def crossover(padre1, padre2):
    """Single-point crossover: devuelve dos hijos."""
    if len(padre1) != len(padre2):
        raise ValueError("Padres de diferente longitud")
    punto = random.randint(1, len(padre1)-1)
    hijo1 = padre1[:punto] + padre2[punto:]
    hijo2 = padre2[:punto] + padre1[punto:]
    return hijo1, hijo2

def mutate(individuo, rate=MUTATION_RATE):
    """Mutar cada carácter con probabilidad 'rate'."""
    lista = list(individuo)
    for i in range(len(lista)):
        if random.random() < rate:
            lista[i] = random_char()
    return ''.join(lista)

# --- Algoritmo principal ---
def run_ga():
    longitud = len(OBJETIVO)
    # Inicializar población
    poblacion = [random_individual(longitud) for _ in range(POP_SIZE)]

    mejor_global = max(poblacion, key=fitness)
    mejor_score = fitness(mejor_global)
    print(f"Objetivo: '{OBJETIVO}'")
    print(f"Mejor inicial: '{mejor_global}' (fitness={mejor_score})\n")

    for gen in range(1, MAX_GENERATIONS + 1):
        nueva_poblacion = []

        # Elitismo: conservar el mejor
        if ELITISM:
            mejor = max(poblacion, key=fitness)
            nueva_poblacion.append(mejor)

        # Generar nueva población por selección, cruce y mutación
        while len(nueva_poblacion) < POP_SIZE:
            # Selección
            padre1 = torneo_seleccion(poblacion)
            padre2 = torneo_seleccion(poblacion)
            # Cruce
            hijo1, hijo2 = crossover(padre1, padre2)
            # Mutación
            hijo1 = mutate(hijo1)
            hijo2 = mutate(hijo2)
            nueva_poblacion.extend([hijo1, hijo2])

        # recortar si supera tamaño
        poblacion = nueva_poblacion[:POP_SIZE]

        # Evaluar
        mejor = max(poblacion, key=fitness)
        mejor_score = fitness(mejor)

        # Mostrar progreso cada X generaciones o si hay mejora
        if gen % 10 == 0 or mejor_score == len(OBJETIVO):
            print(f"Gen {gen:4d} | Mejor: '{mejor}' | Fitness: {mejor_score}/{len(OBJETIVO)}")

        # Condición de terminación
        if mejor_score == len(OBJETIVO):
            print("\n✅ ¡Objetivo alcanzado!")
            break

    print("\nResultado final:")
    print(f"Generación: {gen}")
    print(f"Mejor individuo: '{mejor}'")
    print(f"Fitness: {mejor_score}/{len(OBJETIVO)}")

if __name__ == "__main__":
    run_ga()
