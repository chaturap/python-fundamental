
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

# mengcopy list
daftar_buku = ['how to influence people', 'habbit', 'Muhammad AL fatih', 'karimah']
print("mengcopy list")
daftar_buku_baru = daftar_buku[:]
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
    
print("tampilkan daftar buku baru")
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])
