from datetime import datetime

def hitung_usia(tahun_lahir):
    tahun_sekarang = datetime.now().year
    usia = tahun_sekarang - tahun_lahir
    return usia

# Meminta input nama dan tahun lahir
nama = input("Masukkan nama kamu: ")
try:
    tahun_lahir = int(input("Masukkan tahun lahir kamu: "))
    usia = hitung_usia(tahun_lahir)
    print(f"Halo {nama}! Usia kamu adalah {usia} tahun!")
except ValueError:
    print("Harap masukkan tahun dalam angka!")
