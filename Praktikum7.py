class Mahasiswa:
    '''Dasar kelas untuk semua Mahasiswa'''
    jumlah_mahasiswa = 0

    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
        Mahasiswa.jumlah_mahasiswa += 1
  
    def tampilkan_jumlah(self):
        print("Total Mahasiswa:", Mahasiswa.jumlah_mahasiswa)
    
    def tampilkan_profil(self):
        print("Nama :", self.nama)
        print("NPM :", self.npm)

mahasiswa1 = Mahasiswa("Imsal Yunus", 312110597)
mahasiswa2 = Mahasiswa("Doni Mahendra", 312110596)
mahasiswa2 = Mahasiswa("Gabriela Angellica", 312110595)

mahasiswa1.tampilkan_profil()
mahasiswa2.tampilkan_profil()
print("Total Mahasiswa :", Mahasiswa.jumlah_mahasiswa)