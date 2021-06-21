# Fibonacci Sequence

def fibonacci(i):
    if type(i)!= int:
        raise TyperError("It must be an integer number")
    if i<1:
        raise ValueError("It must be a postitive integer number")
    if i==1:
        return 1
    elif i==2:
        return 2
    elif i>2:
        return fibonacci(i-1) + fibonacci(i-2)

for i in range(1,10):
    print( ' For i=',i,'fibonacci is', fibonacci(i))


print(fibonacci(5))

'''The code works just fine. But if we put a large number in the iteration
python is slow, so we need to fix that problem '''

cache_memo = {} # dictionary to store recent values

def fibonacci_with_cache(n):
    if n in cache_memo:
        return cache_memo[n]
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n>2:
        value= fibonacci_with_cache(n-1) + fibonacci_with_cache(n-2)
        
    cache_memo[n] = value
    return value

for n in range(1,100):
    print(n,':',fibonacci_with_cache(n))

print('####################')
# Fibonacci with LRU algorithm (least recently used)

import functools
@functools.lru_cache(maxsize=128)
def fibonacci_lru(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)

for n in range(1,128):
    print(n,':',fibonacci_lru(n))
