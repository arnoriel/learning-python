import os
import time

# Warna merah ANSI
red_color = "\033[91m"
reset_color = "\033[0m"

# Fungsi teks berjalan
def teks_berjalan(text):
    text += "   "  # Tambahkan beberapa spasi di akhir teks
    width = os.get_terminal_size().columns  # Mendapatkan lebar terminal
    
    # Bersihkan layar di awal
    os.system("cls" if os.name == "nt" else "clear")
    
    try:
        while True:
            # Pindahkan kursor ke baris pertama tanpa membersihkan layar setiap kali
            print("\033[H" + red_color + text.center(width) + reset_color, end="\r", flush=True)
            
            # Geser teks ke kiri
            text = text[1:] + text[0]
            
            # Jeda untuk kecepatan
            time.sleep(0.1)
    except KeyboardInterrupt:
        # Bersihkan layar lagi dan tampilkan pesan keluar
        os.system("cls" if os.name == "nt" else "clear")
        print("Thank you!")  # Pesan saat interupsi

# Meminta input teks dari pengguna
user_text = input("Masukkan teks untuk dijalankan: ")
teks_berjalan(user_text)
