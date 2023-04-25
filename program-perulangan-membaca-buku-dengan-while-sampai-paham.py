"""
Program perulangan membaca buku dengan while
"""

jumlah_buku = 10
print('Ibu berkata "Baca semua bukumu"')
print(f"jumlah_buku {jumlah_buku} ")

jumlah_buku_yang_sudah_dibaca_dan_dipahami = 0
total_jumlah_baca = 0

print(f"jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami} ")


while total_jumlah_baca < jumlah_buku :
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_yang_sudah_dibaca_dan_dipahami == 8:
        print(f"Buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1} belum dipahami")

        if total_jumlah_baca == 2:
            print(f"sudah baca {total_jumlah_baca} kali, ya sudah istirahat dulu")
            #jumlah_buku_yang_sudah_dibaca_dan_dipahami == 10
        #else:
        #    print("harusnya tidak ada kondisi ini")

    else:
        jumlah_buku_yang_sudah_dibaca_dan_dipahami = jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1
        print(f"buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami} sudah dibaca dan dipahami")

print(f"Jumlah buku yang sudah dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}")


if jumlah_buku_yang_sudah_dibaca_dan_dipahami == jumlah_buku:
    print("Semua buku sudah dibaca dan sudah dipahami")
else:
    print(f"Tidak semua buku selesai dibaca dan dipahami, hanya {jumlah_buku_yang_sudah_dibaca_dan_dipahami} buku yang sudah dibaca dan dipahami")

#i+1

