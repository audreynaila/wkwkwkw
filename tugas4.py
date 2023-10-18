# Daftar list 
nama_karyawan = ["Dani", "Duki", "Duke", "Deni", "Dena"]
masakerja = [2, 1, 1, 5, 6]
gajikerja = [4200000, 4800000, 5300000, 5900000, 6400000]

#nilai umr
umrbdg = 5000000

# jumlah total gaji karyawan dengan indeks ganjil
total_ganjil = sum(gaji for i, gaji in enumerate(gajikerja) if i % 2 != 0)

#  jumlah total gaji
total_gaji = sum(gajikerja)

#  jumlah karyawan
jumlah_karyawan = len(nama_karyawan)

# rata-rata gaji
ratarata_gaji = total_gaji / jumlah_karyawan

kenaikan_gaji_per_tahun = 1250000
total_gaji_setelah_kenaikan = [gaji + (masa - 1) * kenaikan_gaji_per_tahun for masa, gaji in zip(masakerja, gajikerja)]

#setting nama
cari= 'Dena'  

# cari indeks nama daftar nama_karyawan
indeks_dicari = nama_karyawan.index(cari)

# Mengecek apakah nama yang dicari  memenuhi UMR Bandung atau tidak
status_dicari = "memenuhi" if gajikerja[indeks_dicari] >= umrbdg else "tidak memenuhi"

# Menampilkan output
print("Maka Hasil Yang didapatkan :")
print(f"{cari} {status_dicari} UMR Bandung.")
print(f"Total gaji karyawan dengan indeks ganjil = {total_ganjil}")
print(f"Rata-rata gaji karyawan = {ratarata_gaji}")
print(f"Total gaji setelah kenaikan = {total_gaji_setelah_kenaikan}")