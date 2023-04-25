# sequential
print('Ibu berkata, "Pergi ke toko"')
print('Budi menjawab,"Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab,"Beli 1 botol susu, dan jika ada telur  beli 6"')
print('Maka Budi berangkat ke toko')
print('Dan mulai berbelanja')

# percabangan
jumlah_botol_susu = 10
jumlah_telur = 5
print(f"jumlah_botol_susu : {jumlah_botol_susu} botol")
if jumlah_botol_susu > 1:
    print("Budi mengecek harga")
    print("Budi membeli 1 botol susu")
else:
    print("Budi tidak jadi membeli 1 botol susu")

if jumlah_telur > 6:
    print("Budi membeli 6 butir telur")
else:
    print("Budi tidak membeli telur")

print("Budi pulang kerumah")
print("lalu  hasil belanjaan ke Ibu")