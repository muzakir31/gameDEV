# Nama: [Tulis Nama Anda]
# NIM: [Tulis NIM Anda]
# Kelas: [Tulis Kelas Anda]

from abc import ABC, abstractmethod
import uuid
import random

# Abstract class
class MakhlukHidup(ABC):
    total_makhluk = 0

    def __init__(self, spesies):
        self._spesies = spesies
        self._usia = 0
        self._dna = None    
        self.generate_dna()
        MakhlukHidup.total_makhluk += 1

    def get_spesies(self):
        return self._spesies

    def get_usia(self):
        return self._usia

    def get_dna(self):
        return self._dna

    def get_total_makhluk(self):
        return MakhlukHidup.total_makhluk

    def generate_dna(self):
        self._dna = str(uuid.uuid4())

    @abstractmethod
    def menua(self):
        pass


class Pelajar(ABC):
    @abstractmethod
    def belajar(self):
        pass


class Pekerja(ABC):
    @abstractmethod
    def bekerja(self):
        pass


# Class Manusia
class Manusia(MakhlukHidup, Pelajar, Pekerja):
    def __init__(self, nama):
        super().__init__("Homo Sapiens")
        self.nama = nama

    def menua(self):
        self._usia += 1

    def belajar(self):
        print(f"{self.nama} sedang belajar.")

    def bekerja(self):
        print(f"{self.nama} sedang bekerja.")

    def get_nama(self):
        return self.nama

# Uji coba 1 objek
orang = Manusia("Budi")
print("Nama:", orang.get_nama())
print("Spesies:", orang.get_spesies())
print("DNA:", orang.get_dna())

# Menjadi tua 3 kali
for _ in range(3):
    orang.menua()

print("Usia setelah menua 3x:", orang.get_usia())
orang.belajar()
orang.bekerja()

# Uji coba 1000 objek
data_manusia = []
usia_kategori = {
    "balita": 0,
    "anak-anak": 0,
    "remaja": 0,
    "dewasa": 0,
    "lansia": 0
}

for i in range(1000):
    m = Manusia(f"Orang_{i}")
    usia = random.randint(0, 80)
    for _ in range(usia):
        m.menua()
    data_manusia.append(m)

    if m.get_usia() <= 5:
        usia_kategori["balita"] += 1
    elif m.get_usia() <= 12:
        usia_kategori["anak-anak"] += 1
    elif m.get_usia() <= 17:
        usia_kategori["remaja"] += 1
    elif m.get_usia() <= 59:
        usia_kategori["dewasa"] += 1
    else:
        usia_kategori["lansia"] += 1

print("\n--- Statistik Usia ---")
print("Jumlah balita:", usia_kategori["balita"])
print("Jumlah anak-anak:", usia_kategori["anak-anak"])
print("Jumlah remaja:", usia_kategori["remaja"])
print("Jumlah dewasa:", usia_kategori["dewasa"])
print("Jumlah lansia:", usia_kategori["lansia"])
print("Total makhluk:", MakhlukHidup.total_makhluk)
