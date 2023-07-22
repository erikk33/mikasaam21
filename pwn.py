from pwn import xor

flag = "KSL 2023{t3s_doank}"

print(xor(flag,7))


import numpy as np 

a = np.array([1,2,3,4,5])

print(np.max(a))
print(a * 5)
