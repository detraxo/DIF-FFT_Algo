#DIF FFT using Radix-2
#Author : Dakshin Sundar

import math
import cmath

#reverse bit 
def reverseBits(num,bitSize): 
     binary = bin(num)  
     reverse = binary[-1:1:-1]
     reverse = reverse + (bitSize - len(reverse))*'0'
     return int(reverse,2)

#twiddle factor
def w(n, k , conj):
    return complex(math.cos((2*math.pi*k)/n) , ((-1)**(not conj))*math.sin((2*math.pi*k)/n))

print("Enter the number of samples : " , end = "")
n = int(input())

#to find smalles power of 2 greater than or equal to n
p = 1
if not(n and not(n & (n-1))):
    while(p < n):
        p <<= 1
    n = p

#find the number of stages
stages = int(math.log(n,2))
x = [] # list of complex values

print("Enter the real values : " , end = "")
real = list(map(float , input().split()))
real += [0]*(n - len(real))

print("Enter the imaginary values : " , end = "")
imag = list(map(float , input().split()))
imag += [0]*(n - len(imag))

print("Press 0 for DFT or 1 for IDFT : ",end = "")
conj = int(input()) #DFT or IDFT

for i in range(n):
    x.append(complex(real[i] , imag[i]))

if conj:
     print("X(k) =" , end='')
else:
     print("x[n] =", end='')
print("[" , x[0] , end= '')
for i in range(n):
     print (",","{0:.3f}".format(x[reverseBits(i,stages)]/n), end = "")
#fft algorithm
def fft(stg , first , last , conj):
     if stg == 3:
          x[first] , x[last] = x[first] + x[last] , (x[first] - x[last])*w(n,0, conj)
     else:     
          for i in range(first , int((last + first)/2) + 1):
               nxt = int(i + 2**(stages - stg))
               x[i] , x[nxt] = x[i] + x[nxt] , (x[i] -  x[nxt])*w(n,stg*i , conj)
     if(stg == stages):
          return 0
     else:
          return fft(stg + 1 , first , int((first + last)/2) , conj) + fft(stg + 1 , int((first + last)/2) + 1  , last , conj) 
fft(1 , 0 , n - 1 , conj) #function call
print()
if conj:
     for i in range(n):
         print ("x[",i,"] :","{0:.3f}".format(x[reverseBits(i,stages)]/n))
else:
     for i in range(n):
         print ("X[",i,"] :","{0:.3f}".format(x[reverseBits(i,stages)]))
