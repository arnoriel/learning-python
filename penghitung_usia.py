from datetime import datetime

def hitung_usia(tahun_lahir):
    tahun_sekarang = datetime.now().year
    usia = tahun_sekarang - tahun_lahir
    return usia

try:
    tahun_lahir = int(input("Masukkan tahun lahir kamu: "))
    usia = hitung_usia(tahun_lahir)
    print(f"Usia kamu adalah {usia} tahun.")
except ValueError:
    print("Harap masukkan tahun dalam angka!")
