from sys import stdin
import time

INF = float('inf')

'''
Entrada: Un arreglo P[0..N], N>=0 de dimensiones de matrices. P[0] y P[1] corresponden a las dimensiones de la primer matriz, P[1] y P[2] de la segunda y asi sucesivamente. 
Salida: Mínimo numero de multiplicaciones para multiplicar N-1 matrices, usando un orden de parentesis determinado.

Generalizacion:

0<i<=j<=N

Entrada: Un arreglo P[0..N], N>=0 de dimensiones de matrices y dos números i y j.
Salida: Mínimo numero de multiplicaciones realizadas para multiplicar las matrices desde i a j, usando un orden de parentesis determinado.


Respuesta = phi(0,len(P)-1)

Definición de phi(_,_)

    Para 0<i<=j<=N 

                0                       , i=j
    phi(n,x):   
                min(phi(i,k)+phi(k+1,j)+p[i-1]*p[k]*p[j])
                for k in i<=k<j        , i<j 

'''

# Se inicializa con i,j = 1, len(p)-1  debido que la posicion 0 de p esquivale a la primera dimension de la primera matriz, pero se puede asignar la posicion 1 a la primera matriz, 2 a la 2 y asi.
 
def matrix_chain(p,i,j):
  if i == j: ans = 0
  else:
    ans,k = float('inf'),i
    while k!=j:
      ans = min(ans,matrix_chain(p,i,k)+matrix_chain(p,k+1,j)+p[i-1]*p[k]*p[j])
      k+=1  

  return ans

def memo_matrix_chain(p,i,j,mem):
  c = (i,j)
  if c in mem: ans= mem[c]
  else:
    if i==j: ans=0
    else:
      ans,k=INF,i
      while k!=j:
        ans=min(ans,memo_matrix_chain(p,i,k,mem)+memo_matrix_chain(p,k+1,j,mem)+p[i-1]*p[k]*p[j])
        k+=1
    mem[c]=ans
  return ans


# Se inicializa con n = len(p)-1 y se empieza desde cero debido a que la posicion 0 de la tabla corresponde a la matriz 0 y asi.
# Se debe tener en cuenta que en esta forma cambia la manera de calcular la cantidad de multiplicaciones ya que en i se encuentra la primera dimension.
def tab_matrix_chain(p, n): 
  m = [[float('inf') for _ in range(n)] for _ in range(n)]
  for i in range(n):
    m[i][i] = 0
  # L is chain length. 
  for L in range(1, n+1): 
    for i in range(0, n-L): 
      j = i+L
      m[i][j] = float('inf') 
      for k in range(i, j): 
      # q = cost/scalar multiplications 
        q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1] 
        if q < m[i][j]: 
          m[i][j] = q 

  return (m[0][n-1]) 


def tab_matrix_chain_extended(p, n): 
  m = [[float('inf') for _ in range(n)] for _ in range(n)]
  s = [[0 for _ in range(n)] for _ in range(n)] 
  for i in range(n):
    m[i][i] = 0
  # L is chain length. 
  for L in range(1, n+1): 
    for i in range(0, n-L): 
      j = i+L
      m[i][j] = float('inf') 
      for k in range(i, j): 
      # q = cost/scalar multiplications 
        q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1] 
        if q < m[i][j]: 
          m[i][j] = q 
          s[i][j] = k
  return (m[0][n-1],s) 

def print_optimal_parents(s,i,j): 
  if i==j:
    print("A",end="")
    print(i+1,end="")
  else:
    print("(",end="")
    print_optimal_parents(s,i,s[i][j])
    print_optimal_parents(s,s[i][j]+1,j)
    print(")",end="")

def main():
  p = [ int(x) for x in stdin.readline().split() ]
  
  s0 = time.time()
  print(matrix_chain(p,1,len(p)-1))
  s1 = time.time()
  print(s1 - s0)

  s0 = time.time()
  mem=dict()
  print(memo_matrix_chain(p,1,len(p)-1,mem))
  s1 = time.time()
  print(s1 - s0)

  s0 = time.time()
  print(tab_matrix_chain(p,len(p)-1))
  s1 = time.time()
  print(s1 - s0)

  s0 = time.time()
  ans,s =tab_matrix_chain_extended(p,len(p)-1)
  print(ans)
  for col in s:
    print(col)
  s1 = time.time()
  print(s1 - s0)
  print_optimal_parents(s,0,len(p)-2) 
  print("")
  
main()




