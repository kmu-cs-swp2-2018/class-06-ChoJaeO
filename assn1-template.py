import time
import random

def iterfibo(n):
    fibo_num = []
    fibo_num.append(0)
    fibo_num.append(1)
    for i in range(2,n+1):
        next_num = fibo_num[i-2] + fibo_num[i-1]
        fibo_num.append(next_num)
    return fibo_num[n]

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


while True:
    try:
        nbr = int(input("Enter a number: "))
    except KeyboardInterrupt:
        print()
        break
    except:
        print("Error : input integer")
        continue
    if nbr == -1:
        print("Quit")
        break
    if nbr < -1:
        print("Error : input over zero to start or -1 to quit")
        continue
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d) = %d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
