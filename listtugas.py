list =["namaKendaraan","JenisKendaraan","ccKendaraan","warnakendaraan","rodakendaraan"]
list.append("hargakendaraan")
list.append("tipekendaraan")
list.insert(2,"merkkendaraan")
print(list)

pilihan = input("pilih operasi 1.hitung persegi, 2.hitung lingkaran, 3.hitung segitiga, masukkan pilihan: ")
match pilihan :
  case "1":
    s = int(input("masukkan sisi: "))
    persegi = s*s
    print('luas persegi', persegi)
  case "2":
    phi = 3.14
    r = int(input("masukkan jari: "))
    lingkaran = phi*r*r
    print('luas lingkara', lingkaran)
  case "3":
    l = 1/2
    a = int(input("masukkan alas: "))
    t = int(input("masukkan tinggi: "))
    segitiga = l*a*t
    print('luas segitiga', segitiga)
  case _:
    print("pilihan tidak tersedia")



