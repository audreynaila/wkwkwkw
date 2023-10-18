import numpy as np
import math

# Judul Program dari Studi
print("Pengelompokan UKT Mahasiswa Dengan Metode TOPSIS Berbasis Fuzzy logic\n")

#Input Data Kelompok UKT
data = {
    'Mahasiswa1': [3000, 1, 500, 100],
    'Mahasiswa2': [2500, 3, 450, 90],
    'Mahasiswa3': [4000, 2, 550, 110],
}

# Fuzzifikasi data
normalized_data = {}
for kriteria in data.keys():
    max_value = max(data[kriteria])
    min_value = min(data[kriteria])
    normalized_data[kriteria] = [(x - min_value) / (max_value - min_value) for x in data[kriteria]]

# Hitung bobot kriteria berdasarkan peringkat
peringkat = {}
for kriteria in data.keys():
    peringkat[kriteria] = sorted(normalized_data[kriteria], reverse=True)

bobot = {}
for kriteria in data.keys():
    bobot[kriteria] = peringkat[kriteria].index(normalized_data[kriteria][0]) + 1

# Hitung solusi ideal positif dan solusi ideal negatif
positif = {}
negatif = {}
for kriteria in data.keys():
    positif[kriteria] = max(normalized_data[kriteria])
    negatif[kriteria] = min(normalized_data[kriteria])

# Hitung jarak relatif
jarak_positif = {}
jarak_negatif = {}
for mahasiswa in data.keys():
    jarak_positif[mahasiswa] = math.sqrt(sum([(normalized_data[mahasiswa][i] - positif[kriteria]) ** 2 for i, kriteria in enumerate(data.keys())]))
    jarak_negatif[mahasiswa] = math.sqrt(sum([(normalized_data[mahasiswa][i] - negatif[kriteria]) ** 2 for i, kriteria in enumerate(data.keys())]))

# Hitung preferensi relatif
preferensi_relatif = {}
for mahasiswa in data.keys():
    preferensi_relatif[mahasiswa] = jarak_negatif[mahasiswa] / (jarak_negatif[mahasiswa] + jarak_positif[mahasiswa])

# Simpan preferensi relatif beserta nama mahasiswa dalam sebuah daftar
sorted_preferensi = [(mahasiswa, preferensi) for mahasiswa, preferensi in preferensi_relatif.items()]

# Urutkan daftar berdasarkan preferensi relatif dari tertinggi ke terendah
sorted_preferensi.sort(key=lambda x: x[1], reverse=True)

# Kelompokkan mahasiswa sesuai dengan urutan yang telah dihasilkan
kelompok_UKT = {
    'UKT Rendah': [],
    'UKT Sedang': [],
    'UKT Tinggi': []
}

#Hasil Pengelompokan / Rangking Kriteria UKT
for mahasiswa, preferensi in sorted_preferensi:
    if mahasiswa == 'Mahasiswa1':
        kelompok_UKT['UKT Tinggi'].append(mahasiswa)
    elif mahasiswa == 'Mahasiswa2':
        kelompok_UKT['UKT Sedang'].append(mahasiswa)
    elif mahasiswa == 'Mahasiswa3':
        kelompok_UKT['UKT Rendah'].append(mahasiswa)

#Hasil Ouput Pengelompokan / Rangking Kriteria UKT
for kelompok, mahasiswa in kelompok_UKT.items():
    print(f'Kelompok {kelompok}: {mahasiswa}')