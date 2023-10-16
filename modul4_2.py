#Nama : Bambang Aji Wicaksono
#NIM : 065002300006
#Prodi : Sistem Informasi

print("Program akan menentukan hari dari bulan yang diinput")
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
ulang = "y"
while ulang == "y": 
    pilih = int(input("Masukkan bulan ( 1 - 12 ) :"))
    if pilih >= 1 and pilih <= 12:
        if pilih == 1 or pilih == 3 or pilih == 5 or pilih == 7 or pilih == 8 or pilih == 10 or pilih == 12 :
            print(f"Ini bulan {bulan[pilih-1]} dan sebulan sebanyak 31 Hari")
        elif pilih == 2:
            feb = int(input("Masukkan tahun nya :"))
            if (feb % 4 == 0) and (feb % 100 != 0 or feb % 400 == 0):
                print(f"Ini bulan {bulan[pilih-1]} dan sebulan sebanyak 29 Hari")
            else :
                print(f"Ini bulan {bulan[pilih-1]} dan sebulan sebanyak 28 Hari")
        elif pilih ==  4 or pilih == 6 or pilih == 9 or pilih == 11:
            print (f"Ini bulan {bulan[pilih-1]} dan sebulan sebanyak 30 hari")

    else:
        print("Input harus dari 1 - 12")  
        
    ulang = str(input("Lagi? (y / n): "))
    if ulang.lower() != "y":
        break
