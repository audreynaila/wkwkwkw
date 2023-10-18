import time

class DSLRCamera_IOT:
    def __init__(self):
        self.input_nilai = 0

    def ambil_gambar(self):
        print("Kamera Mengambil gambar.....")

    def nilai_ketajaman(self):
        print ("PROGRAM IOT KAMERA DSLR TINGKAT KE BLURAN\n")
        while True:
            try:
                self.input_nilai = float(input("Masukkan nilai ketajaman range (1-1000): "))
                if 0 <= self.input_nilai<= 1000:
                    break
                else:
                    print("Masukan Nilai ketajaman dengan benar.")
            except ValueError:
                print("Masukan tidak valid. Harap masukkan angka")

    def fokus_kameradslr(self):
        nilai_ambang = 500

        self.nilai_ketajaman()  
        self.input_nilai = float(input("Masukkan nilai ketajaman range (1-1000): "))

        while True:
            if self.input_nilai > nilai_ambang:
                print("Memutar fokus ke kanan")
                break
            elif self.input_nilai < nilai_ambang:
                print("Memutar fokus ke kiri")
                break
            elif self .input_nilai == nilai_ambang :
                print("Ambil Gambar")
                self.ambil_gambar()
                break

            nilai_ambang = self.input_nilai
            #time.sleep(3)  # Pause selama 3 detik sebelum mengukur kembali
            #ini ditandai opsional jika ingin mencoba terus menerus angka dengan sekali run

    #perumpaan saat kamera menangkap citra agar lebih mudah diproses citra pada kamera sehingga ubah ke grayscale kemudian laplacian untuk ketajaman citra
    def hitung_ketajaman(self, frame):
        tinggi, lebar, _ = frame.shape
        citra_abu = [[0 for _ in range(lebar)] for _ in range(tinggi)]

        for y in range(tinggi):
            for x in range(lebar):
                pixel = frame[y, x]
                nilai_keabuan = int(0.299 * pixel[2] + 0.587 * pixel[1] + 0.114 * pixel[0])
                citra_abu[y][x] = nilai_keabuan
        
        ketajaman = cv2.laplacian(citra_gray1, cv2.CV_64F).var()
        return ketajaman

    def hubungkan_iot(self):
        # Contoh koneksi ke perangkat IoT
        print("Menghubungkan ke perangkat IoT...")
        
if __name__ == "__main__":
    dslr = DSLRCamera_IOT()
    dslr.fokus_kameradslr()