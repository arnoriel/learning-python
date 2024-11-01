import time
import os
import sys

# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Warna ANSI untuk teks
colors = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
]

reset_color = "\033[0m"  # Reset warna kembali ke default

def color_changing_text(text):
    text = " " * 20 + text  # Menambahkan spasi untuk efek scroll dari kanan
    try:
        while True:
            for i in range(len(text)):
                clear_screen()
                color = colors[i % len(colors)]  # Mengubah warna sesuai urutan
                print(color + text[i:] + reset_color)  # Menampilkan teks dengan warna
                time.sleep(0.1)  # Menunggu sebelum pindah ke frame berikutnya
    except KeyboardInterrupt:
        print("\nAnimasi dihentikan.")

def main():
    clear_screen()
    text = input("Masukkan teks yang ingin dianimasikan: ")
    print("Animasi Teks Berwarna Berjalan. Tekan Ctrl+C untuk berhenti.")
    color_changing_text(text)

if __name__ == "__main__":
    main()
