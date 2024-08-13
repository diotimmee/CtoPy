import time

import ctypes

code = ctypes.CDLL('./add.so')
#
# start = time.time()
# # python
# arr = list(range(1, 1000001))
# arr_len = len(arr)
# py_sum = sum(arr)
# end = time.time()
# natija = end - start
# print(natija)
# print("_____")
#
# code.sum_array.restype = ctypes.c_int
# c_arr = (ctypes.c_int * arr_len)(*arr)
# start1 = time.time()
# code.sum_array(c_arr, arr_len)
# end1 = time.time()
# print(end1 - start1)
code.sum_array.restype = ctypes.c_int

arr = list(range(1, 1000001))  # 1,000,000 elementli massiv
arr_len = len(arr)

# C tilidagi massivni yaratish uchun Python massivini ctypes massiviga o'giramiz
c_array = (ctypes.c_int * arr_len)(*arr)

# 1. Python kodini sinash
start_time = time.time()
python_sum = sum(arr)
python_time = time.time() - start_time
print(f"Python'da vaqt: {python_time:.6f} soniya")

# 2. C kodini sinash
start_time = time.time()
c_sum = code.sum_array(c_array, arr_len)
c_time = time.time() - start_time
print(f"C'da vaqt: {c_time:.6f} soniya")

# Natijalarini tekshiramiz
# assert python_sum == c_sum, "Natijalar bir xil emas!"
# print("Natijalar bir xil!")

# Vaqt farqini chiqaramiz
print(f"C kodining tezligi Python'dan {python_time / c_time:.2f} marta tezroq")

#  gcc -shared -o add.so -fPIC main.c
