class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, Warna: {self.warna}, Rasa: {self.rasa}")

buah1 = Buah("Mangga", "Kuning", "Manis")

print("Sebelum dihapus:")
buah1.tampilkan_info()

del buah1.rasa
try:
    print("\nSetelah 'rasa' dihapus:")
    buah1.tampilkan_info()
except AttributeError:
    print("Error: 'rasa' telah dihapus.")

del buah1
try:
    print("\nSetelah objek dihapus:")
    buah1.tampilkan_info()
except NameError:
    print("Error: Objek 'buah1' telah dihapus dan tidak dapat diakses lagi.")
