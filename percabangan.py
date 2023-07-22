abs = 1
kosam = 0
rokai = abs or kosam
kokai = kosam and abs
print(rokai)
if (abs < kosam):
    print(f"{abs}\n hasilnya sudah benar")

elif (abs > kosam):
    print("hasil tergantung kondisi いつか",kosam-abs and kosam+abs)

elif(rokai):
    print(rokai)    
else:
    print("hasilnya sudah salah sekali いつか ",abs)
