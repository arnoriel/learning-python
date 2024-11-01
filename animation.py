import time
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def spinning_ball():
    spinner = ['◐', '◓', '◑', '◒']
    try:
        while True:
            for frame in spinner:
                sys.stdout.write('\r' + frame)
                sys.stdout.flush()
                time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nAnimasi dihentikan.")

def dancing_bird():
    frames = [
        """
          ♪  (•_•)
           <)  )╯
           /   >
        """,
        """
          ♪  (•_•)
           <(  (>
            /   \\
        """
    ]
    try:
        while True:
            for frame in frames:
                clear_screen()
                print(frame)
                time.sleep(0.3)
    except KeyboardInterrupt:
        print("\nAnimasi dihentikan.")

def scrolling_text(text):
    text = " " * 20 + text
    try:
        while True:
            for i in range(len(text)):
                clear_screen()
                print(text[i:])
                time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nAnimasi dihentikan.")

def twinkling_stars():
    stars = [
        """
        *       *
           *       *
        *       *
           *       *
        """,
        """
           *       *
        *       *
           *       *
        *       *
        """,
        """
        *       *
           *       *
        *       *
           *       *
        """
    ]
    try:
        while True:
            for frame in stars:
                clear_screen()
                print(frame)
                time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nAnimasi dihentikan.")

def wave():
    frames = [
        "~~~    ~~~    ~~~",
        "    ~~~    ~~~    ",
        "~~~    ~~~    ~~~"
    ]
    try:
        while True:
            for frame in frames:
                clear_screen()
                print(frame)
                time.sleep(0.3)
    except KeyboardInterrupt:
        print("\nAnimasi dihentikan.")

def lightning():
    frames = [
        """
         \\
           \\
            ⚡
        """,
        """
            ⚡
         \\
           \\
        """,
        """
         \\
            ⚡
           \\
        """
    ]
    try:
        while True:
            for frame in frames:
                clear_screen()
                print(frame)
                time.sleep(0.2)
    except KeyboardInterrupt:
        print("\nAnimasi dihentikan.")

def main():
    while True:
        clear_screen()
        print("Pilih animasi yang ingin ditampilkan:")
        print("1. Animasi Bola Berputar")
        print("2. Animasi Burung Menari")
        print("3. Animasi Teks Berjalan")
        print("4. Animasi Bintang Berkedip")
        print("5. Animasi Gelombang")
        print("6. Animasi Petir")
        print("7. Keluar")
        
        choice = input("Masukkan pilihan (1/2/3/4/5/6/7): ")
        
        if choice == '1':
            clear_screen()
            print("Animasi Bola Berputar. Tekan Ctrl+C untuk berhenti.")
            spinning_ball()
        elif choice == '2':
            clear_screen()
            print("Animasi Burung Menari. Tekan Ctrl+C untuk berhenti.")
            dancing_bird()
        elif choice == '3':
            clear_screen()
            text = input("Masukkan teks yang ingin ditampilkan: ")
            print("Animasi Teks Berjalan. Tekan Ctrl+C untuk berhenti.")
            scrolling_text(text)
        elif choice == '4':
            clear_screen()
            print("Animasi Bintang Berkedip. Tekan Ctrl+C untuk berhenti.")
            twinkling_stars()
        elif choice == '5':
            clear_screen()
            print("Animasi Gelombang. Tekan Ctrl+C untuk berhenti.")
            wave()
        elif choice == '6':
            clear_screen()
            print("Animasi Petir. Tekan Ctrl+C untuk berhenti.")
            lightning()
        elif choice == '7':
            print("Terima kasih telah menggunakan program animasi!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            time.sleep(2)

if __name__ == "__main__":
    main()
