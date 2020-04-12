"""
Entrada: un grafo[V][V] que representa la matriz de adyacencia del grafo
y C que representa el numero de colores

Salida: todas las posibles soluciones. Una solucion estara representada
por un arreglo de V posiciones, donde, en cada posicion se asigna un color
"""

def safe(A, v, colour, c):
    ans = True
    for i in range(len(A)):
        if A[v][i] == 1 and colour[i] == c:
            ans = False
    return ans

def solve(A, m, colour, v, all_sols):
    if v == len(A[0]):
        all_sols.append(list(colour))
    else:
        for c in range(1, m+1):
            if safe(A, v, colour, c):
                colour[v] = c
                solve(A, m, colour, v+1, all_sols)

def main():
    all_sols = []
    A = [[0,1,1,1], [1,0,1,0], [1,1,0,1], [1,0,1,0]]
    V = len(A[0])
    colour = [None for _ in range(V)]
    m = 3
    solve(A, m, colour, 0, all_sols)

main()
