#DIF FFT using Radix-2
#Author : Dakshin

import math
import cmath


def reverseBits(num,bitSize): 
     binary = bin(num)  
     reverse = binary[-1:1:-1]
     reverse = reverse + (bitSize - len(reverse))*'0'
     return int(reverse,2)


def w(n, k):
    return complex(math.cos((2*math.pi*k)/n) , -math.sin((2*math.pi*k)/n))


print("Enter the number of samples : " , end = "")
n = int(input())
p = 1
if not(n and not(n & (n-1))):
    while(p < n):
        p <<= 1
    n = p
stages = int(math.log(n,2))
x = []
print("Enter the real values : " , end = "")
real = list(map(int , input().split()))
real += [0]*(n - len(real))
print("Enter the imaginary values : " , end = "")
imag = list(map(int , input().split()))
imag += [0]*(n - len(imag))
for i in range(n):
    x.append(complex(real[i] , imag[i]))
def fft(stg , first , last):
    for i in range(first , int((last + first)/2) + 1):
        nxt = int(i + 2**(stages - stg))
        x[i] , x[nxt] = x[i] + x[nxt] , (x[i] -  x[nxt])*w(n,stg*i)
    if(stg == stages):
        return 0
    else:
        return fft(stg + 1 , first , int((first + last)/2)) + fft(stg + 1 , int((first + last)/2) + 1  , last) 
fft(1 , 0 , n - 1)
for i in range(n):
    print ("{0:.3f}".format(x[reverseBits(i,stages)])) 
