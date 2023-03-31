print("Hai, selamat datang di aplikasi kalkulator, apa yang ingin anda lakukan? \n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian")
tujuan = input()
if tujuan == '1':
    print("Masukkan nilai pertama :")
    nilai_pertama = float(input())
    print("Masukkan nilai kedua :")
    nilai_kedua = float(input())
    jumlah = nilai_pertama + nilai_kedua
    print("Hasil penjumlahan anda adalah : ", jumlah)
    
elif tujuan == '2':
    print("Masukkan nilai pertama :")
    nilai_pertama = float(input())
    print("Masukkan nilai kedua :")
    nilai_kedua = float(input())
    jumlah = nilai_pertama - nilai_kedua
    print("Hasil penjumlahan anda adalah : ", jumlah)

elif tujuan == '3':
    print("Masukkan nilai pertama :")
    nilai_pertama = float(input())
    print("Masukkan nilai kedua :")
    nilai_kedua = float(input())
    jumlah = nilai_pertama * nilai_kedua
    print("Hasil penjumlahan anda adalah : ", jumlah)
    
elif tujuan == '4':
    print("Masukkan nilai pertama :")
    nilai_pertama = float(input())
    print("Masukkan nilai kedua :")
    nilai_kedua = float(input())
    jumlah = nilai_pertama / nilai_kedua
    print("Hasil penjumlahan anda adalah : ", jumlah)