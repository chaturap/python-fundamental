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