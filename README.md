# DIF-FFT_Algo
Discrete time Fourier Transform using DIF-FFT (radix-2). Upto 1000 samples.

#### *Time Complexity :*
> ## ***O(n log n)***

#### *Method :*
> ## ***Recursion***

#### *Limitation :*
> ## ***Recursion call stack overflows at 1000 calls.***

#### *Algorithm :*
```
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
```
> w(n , k) : twiddle factor 
#### *Explaination :*
*Implementing butterfly diagram using recursion tree.*

![Butterfly Diagram](https://cnx.org/resources/b5ad07e2befa0fbce5e9f477dd61092d46adab40/image3.png)
