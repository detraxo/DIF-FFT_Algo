# DIF-FFT_Algo
Python script that computes Discrete Fourier Transform and Inverse Discrete Fourier Transform using Decimation in Frequency Fast Fourier Transform Algorithm. Computes FFT of upto 1000 point samples.

#### *Time Complexity :*
> ## ***O(n log n)***

#### *Method :*
> ## ***Recursion***

#### *Limitation :*
> ## ***Recursion call stack overflows at 1000 calls.***

#### *Algorithm :*
```
def fft(stg , first , last):
    for i in range(first , int((last + first)/2) + 1):
        nxt = int(i + 2**(stages - stg))
        x[i] , x[nxt] = x[i] + x[nxt] , (x[i] -  x[nxt])*w(n,stg*i)
    if(stg == stages):
        return 0
    else:
        return fft(stg + 1 , first , int((first + last)/2)) + fft(stg + 1 , int((first + last)/2) + 1  , last) 
```
