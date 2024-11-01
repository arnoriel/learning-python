import os
import time

# Pilihan warna ANSI untuk terminal
colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m", "\033[97m"]
reset_color = "\033[0m"

# Fungsi teks berjalan
def teks_berjalan(text):
    text += "   "  # Tambahkan beberapa spasi di akhir teks
    width = os.get_terminal_size().columns  # Mendapatkan lebar terminal
    color_index = 0  # Mulai dari warna pertama dalam daftar warna
    
    try:
        while True:
            os.system("cls" if os.name == "nt" else "clear")  # Bersihkan layar
            print(colors[color_index] + text.center(width) + reset_color)  # Tampilkan teks di tengah layar dengan warna
            
            # Pindah ke warna berikutnya
            color_index = (color_index + 1) % len(colors)
            
            # Geser teks ke kiri
            text = text[1:] + text[0]
            
            # Jeda sebelum loop berikutnya
            time.sleep(0.2)
    except KeyboardInterrupt:
        os.system("cls" if os.name == "nt" else "clear")
        print("Thank you!")  # Pesan saat interupsi

# Meminta input teks dari pengguna
user_text = input("Masukkan teks untuk dijalankan: ")
teks_berjalan(user_text)
