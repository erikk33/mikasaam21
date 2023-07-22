mahasiswa = {
    "nama":"erikun",
    "nim" : 220040149,
    "prodi" : "TI"
    }
for key,value in mahasiswa.items() :
    print(f"{key}:{value}")

print(mahasiswa["nama"])
mahasiswa["jenis_kelamin"] = True
del mahasiswa["nim"]


#penggunaaan set

set1 = {1,2,3,4,5,5}
set2 = {2,3,4,5,6,7}

set1.add(10)#menambahkan element pada set
set1.remove(4) #menghapus element pada set

gabungan = set1.union(set2)#menggabungkan set1 dan set2
persamaan = set1.intersection(set2)#irisan set1 & set 2
perbedaan = set1.difference(set2)

print(gabungan)