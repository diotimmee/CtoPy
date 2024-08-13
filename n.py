import time

import ctypes

code = ctypes.CDLL('./add.so')

code.fib.argtypes = (ctypes.c_int,)
code.fib.restype = ctypes.c_int

# Fibonacci sonini Python'da hisoblash
def python_fib(n):
    if n <= 1:
        return n
    else:
        return python_fib(n-1) + python_fib(n-2)

n = 35  # N-ni aniqlash

# 1. Python kodini sinash
start_time = time.time()
python_result = python_fib(n)
python_time = time.time() - start_time
print(f"Python'da vaqt: {python_time:.6f} soniya, Natija: {python_result}")

# 2. C kodini sinash
start_time = time.time()
c_result = code.fib(n)
c_time = time.time() - start_time
print(f"C'da vaqt: {c_time:.6f} soniya, Natija: {c_result}")

# Natijalarini tekshiramiz
# assert python_result == c_result, "Natijalar bir xil emas!"
# print("Natijalar bir xil!")

# Vaqt farqini chiqaramiz
print(f"C kodining tezligi Python'dan {python_time / c_time:.2f} marta tezroq")

#  gcc -shared -o add.so -fPIC main.c
