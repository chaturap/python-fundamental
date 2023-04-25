daftar_buku = ['how to influence people', 'habbit', 'Muhammad AL fatih']
print(daftar_buku)

# menampilkan dengan for in , semua di tampilkan
print("\nMenampilkan semua element list")
for buku in daftar_buku:
    print(buku)

# menampilkan dengan for in, dengan range  tertentu
daftar_buku = ['how to influence people', 'habbit', 'Muhammad AL fatih','Karima']
print("\nmenampilkan dengan for in")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# menampilkan list dengan tipe element yang berbeda
daftar_buku = ['habbit' ,360 , 3.14 , -10]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# Menambahkan element baru di dalam list
daftar_buku = ['how to influence people', 'habbit', 'Muhammad AL fatih']
print("menambahkan buku baru")
daftar_buku.append('Hijrah')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


# clear list
print("clear list")
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# hapus element tertentu dengan pop
print("hapus element tertentu dengan pop")
daftar_buku = ['how to influence people', 'habbit', 'Muhammad AL fatih']
daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# hapus element tertentu dengan pop default
print("hapus element tertentu dengan pop")
daftar_buku = ['how to influence people', 'habbit', 'Muhammad AL fatih']
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# hapus element tertentu dengan pop minus
print("hapus element tertentu dengan pop minus")
daftar_buku = ['how to influence people', 'habbit', 'Muhammad AL fatih']
daftar_buku.pop(-1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# hapus element dengan perintah del
print("hapus element tertentu dengan dell, semua")
daftar_buku = ['how to influence people', 'habbit', 'Muhammad AL fatih']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# hapus element dengan perintah del dari index ke 0 sebanyak 1
print("hapus element tertentu dengan dell, dari index ke 0 sebanyak 1")
daftar_buku = ['how to influence people', 'habbit', 'Muhammad AL fatih']
del daftar_buku[0:1]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# hapus element dengan perintah del dengan step
print("hapus element tertentu dengan dell, minus")
daftar_buku = ['how to influence people', 'habbit', 'Muhammad AL fatih','karimah']
del daftar_buku[0:-2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# hapus element dengan perintah del dengan step
print("hapus element tertentu dengan dell, dengan step")
daftar_buku = ['how to influence people', 'habbit', 'Muhammad AL fatih','karimah']
del daftar_buku[0::2] #index:sebanyak berapa:step
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])