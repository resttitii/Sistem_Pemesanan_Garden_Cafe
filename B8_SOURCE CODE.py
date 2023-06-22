import os
import time
from datetime import datetime

pesan = {}
harga = []

waktu = datetime.now()
hari = waktu.day
bulan = waktu.month
tahun = waktu.year
tanggal = "{}/{}/{}".format(hari,bulan,tahun)


def pesanan(input_beli):
    data_menu = {
        '1' : {
            'nama':'Americano',
            'harga' : 12000
        },
        '2' : {
            'nama':'Cappucino',
            'harga':16000
        },
        '3' : {
            'nama':'Expresso',
            'harga':10000
        },
        '4' : {
            'nama':'Lemon tea',
            'harga':14000
        },
        '5' : {
            'nama':'Lychee tea',
            'harga':14000
        },
        '6' : {
            'nama':'Matcha tea',
            'harga':16000
        },
        '7' : {
            'nama':'Croissant',
            'harga':15000
        },
        '8' : {
            'nama':'Cheesecake',
            'harga':17000
        },
        '9' : {
            'nama':'French Fries',
            'harga':10000
        }
    }
    
    if data_menu.get(input_beli) is None:
        return None
    else:
        ambil_nama = list(map(lambda x : x, data_menu.get(input_beli).values()))[0]
        ambil_harga = list(map(lambda x : x, data_menu.get(input_beli).values()))[1]
        return ambil_nama, ambil_harga


def halamanBaru():
    os.system("cls" if os.name == "nt" else "clear")


def pesanMenu():
    halamanBaru()

    print("""
    ==================================
    ||            M E N U           ||
    ==================================

    C O F F E E
    [1] Americano           Rp 12.000
    [2] Cappucino           Rp 16.000
    [3] Expresso            Rp 10.000

    T E A
    [4] Lemon tea           Rp 14.000
    [5] Lychee tea          Rp 14.000
    [6] Matcha tea          Rp 16.000
    
    D E S S E R T
    [7] Croissant           Rp 15.000
    [8] Cheesecake          Rp 17.000
    [9] French Fries        Rp 15.000
    
    """)

    print("")

    beli = input(">> Masukan menu yang akan dibeli\n>> ")
    akses_menu = pesanan(beli)
    if akses_menu is None:
        print("Maaf menu yang anda pilih tidak terdaftar, pilih menu yang telah tertera!")
        time.sleep(1)
        pesanMenu()
    else:
        pesan[akses_menu[0]] = akses_menu[1]
        harga.append(akses_menu[1])
    tambah()


def tambah():
    pilih2 = input("\nTambah pesanan lagi? (y/t) ")

    if pilih2 == "y":
        pesanMenu()
    elif pilih2 == "t":
        os.system("CLS")
        total = sum(harga)
        print("")
        print("=============================  S  T  R  U  K  =============================")
        print("")
        print("Pesanan              : ", list(map(lambda x : x, pesan.keys())))
        print("Masing-masing harga  : ", list(map(lambda x : x, pesan.values())))
        print("Total harga          :  Rp. {:,},-".format(total))
        print("")
        print("Tanggal pembelian: {}".format(tanggal))
        c = "selamat menikmati!"
        print(c.center(75))
        print("=" * 75)
    else:
        print("Pilih y/t!")
        tambah()
    enterOut()


def enterOut():
    print("")
    input("Tekan [ENTER] untuk keluar ...")
    keluar()


def keluar():
    import itertools # pengulangan yang tak terbatas
    import threading # konkurensi dalam mengeksekusi sebuah operasi
    import time
    import sys # mengakses konfigurasi interpreter pada saat runtime dan berinteraksi dengan environment sistem operasi.

    done = False

    def animate():
        for c in itertools.cycle(['|','/','-','\\']):
            if done:
                break

            sys.stdout.write("\rloading" + c)
            sys.stdout.flush()
            time.sleep(0.1)

    t = threading.Thread(target=animate)
    t.start()
    time.sleep(5)
    done = True

    import os
    os.system("CLS")
    print("="*42)
    a = "Thank You, love <3"
    b = "Have a nice day!"
    print(a.center(42))
    print(b.center(42))
    print("="*42)
    exit()


def menu():     
    halamanBaru()
    nama = input("Masukan nama Anda: ")
    os.system("CLS")
    print("\nSelamat Datang, {}!\n".format(nama))
    print("="*42)
    print("          Menu Utama Garden Cafe         ")
    print("="*42)
    print("\n[1] Info Garden Cafe")
    print("")
    print("[2] Menu Pesanan")
    print("")
    
    jawabMenu = input(">>> Masukan Pilihan Menu: ")
    os.system("CLS")
    if jawabMenu == "1":
        print("""
                            GARDEN CAFE                                      

        Garden cafe merupakan tempat yang menyediakan berbagai 
        coffe, tea, dan dessert yang dapat dinikmati sambil 
        mengamati pemandangan yang hijau, sejuk, dan tentunya
        nyaman. Tidak hanya itu, Garden Cafe juga jauh dari 
        kebisingan loh! sehingga sangat cocok bagi mahasiswa 
        yang ingin mengerjakan tugas disana ^_^

        Buka setiap hari:
        10.00 - 21.00 WIB
        """)
        print("")
        input("Tekan [ENTER] untuk kembali ...")
        menu()

    elif jawabMenu == "2":
        pesanMenu()
    else:
        print("Menu yang Anda masukan salah!")
        time.sleep(1)
        menu()

menu()