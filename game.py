import random

def main():
    print("Selamat datang di Game Tebak Angka!")
    print("Komputer telah memilih angka secara acak antara 1 dan 100.")
    print("Cobalah tebak angka tersebut dalam maksimal 10 kesempatan.")
    
    target = random.randint(1, 100)  # Angka yang harus ditebak
    attempts = 10  # Jumlah maksimal kesempatan
    
    for attempt in range(1, attempts + 1):
        guess = int(input(f"Tebakan {attempt}/{attempts}: Masukkan angka: "))
        
        if guess < target:
            print("Terlalu rendah!")
        elif guess > target:
            print("Terlalu tinggi!")
        else:
            print(f"Selamat! Kamu berhasil menebak angka {target} dalam {attempt} kali percobaan!")
            break
    else:
        print(f"Maaf, kamu kehabisan kesempatan. Angka yang benar adalah {target}.")
    
if __name__ == "__main__":
    main()
