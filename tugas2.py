# Program Biodata

print("Biodata Kewarganegaraan\n")

nama = input("Masukkan Nama Lengkap = ")
jenis_kelamin = input("Masukkan Jenis Kelamin = ")
umur = int(input("Masukkan Umur: "))
tanggal_tempat = input("Masukkan Tempat dan Tanggal Lahir = ")
tlp = input("Nomor Telepon: ")
alamat = input("Masukkan Alamat: ")

print("\nHasil Biodata\n")
print("Nama:", nama, "Tipe Data:", type(nama))
print("Jenis Kelamin:", jenis_kelamin, "Tipe Data:", type(jenis_kelamin))
print("Umur:", umur, "Tipe Data:", type(umur))
print("Nomor Telepon:", tlp, "Tipe Data:", type(tlp))
print("Tempat/Tanggal Lahir", tanggal_tempat, "Tipe Data:", type(tanggal_tempat))
print("Alamat:", alamat, "Tipe Data:", type(alamat))

print("")
print("Maka:")
if umur <= 20:
    print(f"{nama} berumur {umur} tahun status belum menikah.")
elif umur > 20:
    print(f"{nama} berumur {umur} tahun status sudah menikah.")

print("")
print("Selesai\n")
