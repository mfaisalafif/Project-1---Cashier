# Project 01 : Cashier
# Background
**Panjat (Panduan Belanja Termurah)** merupakan sistem _self checkout_ yang bertujuan untuk memudahkan customer melakukan pemesanan ke supermarket. Customer dapat melakukan input nama barang, jumlah barang dan harga barang ke dalam keranjang belanja. Jika customer melakukan kesalahan input maka customer dapat melakukan update nama, jumlah ataupun harga barang tersebut. Customer juga dapat membatalkan pemesanan barang dengan cara menghapus beberapa barang yang ingin dibatalkan ataupun dengan melakukan _reset_ (menghapus seluruh barang dari keranjang belanja). Setelah pemesanan selesai, customer dapat melihat isi keranjang belanja, mengecek apakah total belanja mendapatkan diskon sesuai ketentuan yang berlaku, dan melihat total harga yang perlu dibayar.


![Poster1](https://github.com/mfaisalafif/Project01_Cashier/blob/main/Panjat.jpg)

# Requirements
1. Customer melakukan input nama dan nomor ID   
2. Customer melakukan input nama barang, jumlah barang dan harga barang ke dalam keranjang
3. Customer mengupdate nama, jumlah dan harga barang jika ada kesalahan input
4. Customer membatalkan pemesanan barang:
   - Menghapus barang dari keranjang
   - Melakukan _reset_ keranjang
5. Customer dapat melihat isi keranjang belanja sementara
6. Customer dapat melihat isi keranjang belanja dalam bentuk tabel dan total harga sementara
7. Customer dapat melakukan pengecekan total belanja akhir dan juga apakah customer mendapatkan diskon sesuai dengan ketentuan berikut:
   - Jika total belanja kurang dari atau sama dengan Rp200.000 maka tidak akan mendapatkan diskon
   - Jika total belanja lebih dari Rp200.000 dan kurang dari atau sama dengan Rp300.000 maka akan mendapatkan diskon 5%
   - Jika total belanja lebih dari Rp300.000 dan kurang dari atau sama dengan Rp500.000 maka akan mendapatkan diskon 8%
   - Jika total belanja lebih dari Rp500.000 maka akan mendapatkan diskon 10%
8. Customer dapat melihat total harga akhir yang perlu dibayar

# Flowchart
Berikut ini merupakan flowchart untuk menggunakan sistem Panjat (Panduan Belanja Termurah)


![Flow](https://github.com/mfaisalafif/Project01_Cashier/blob/main/Flowchart%20Cashier.png)

# Code Explanation

## 1. main_cashier.py
Berikut ini merupakan code main_cashier di mana proses utama (running code) akan dijalankan, di bagian ini juga akan diimport class Panjat dan class BelanjaPanjat dari masing-masing module. Lalu di bagian ini akan terjadi proses input data nama dan nomor ID customer.
          
      from module1_cashier import Panjat
      """Melakukan import class Panjat dari file module1_cashier.py"""

      from module2_cashier import BelanjaPanjat
      """Melakukan import class BelanjaPanjat dari file module2_cashier.py"""
      
      def nama_dan_id():
          """
          Fungsi ini bertujuan untuk melakukan input nama dan id 
          ------------------------------------------------------
          
          Parameters
          ----------
          nama1 = str
              Nama customer yang akan diinput oleh customer
          id_tr1 = str
              ID yang akan diinput oleh customer
          nama_2 = str
              Nama customer yang distandardkan ke dalam string
          id_tr2 = int
              ID customer yang distandardkan ke dalam integer
          transaction2 = class --> Panjat
              Membuat object transaction2
          transaction2.selamat_datang() = method in class --> Panjat
              Memanggil method pesan selamat datang di modul class Panjat
          """
          ## Looping untuk melakukan pengisian nama jika belum diisi dengan benar
          nama1 = ""
          while len(nama1) == 0:
              nama1 = str(input("Silahkan input nama anda: "))
              if len(nama1) == 0:
                  print("Nama tidak boleh kosong.")
          
          ## Looping untuk melakukan pengisian nomor ID jika belum diisi dengan benar
          while True:
              id_tr1 = input("Silahkan input No ID customer anda: ")
              if id_tr1.isdigit():
                  break
              else:
                  print("No ID customer tidak valid.")
          
          nama2 = str(nama1)
          id_tr2 = int(id_tr1)
          transaction2 = Panjat(nama2, id_tr2)
          return(transaction2.selamat_datang())

      nama_dan_id()

## 2. module1_cashier.py
Berikut ini merupakan code module1_cashier di mana terdapat 'class Panjat', class ini bertujuan untuk memberikan pesan selamat datang kepada customer. Method yang terdapat dalam kelas ini yaitu : Panjat.selamat_datang().

      class Panjat: 
          """
          Membuat class Panjat untuk memberi pesan selamat datang kepada customer
          -----------------------------------------------------------------------
              
          Attributes
          ----------
          nama = str
              Nama customer
          id_tr = int
              No ID customer
          
          Method
          ------
          selamat_datang()
              Memberi pesan selamat datang sesuai dengan nama dan no ID customer
          
          """
          def __init__(self, nama, id_tr):
              """
              Constructor untuk class Panjat
      
              Parameters
              ----------
              Tidak terdapat parameter pada Constructor
      
              Attributes
              ----------
              nama = str
                  Nama customer
              id_tr = int
                  No ID customer
              """
      
              self.nama = nama
              self.id_tr = id_tr 
          
          def selamat_datang(self):
              """
              Method untuk memberi pesan selamat datang sesuai dengan nama dan no ID customer
             
              """
              self.selamat = f"{self.nama} dengan No customer ID {self.id_tr}, Selamat datang di PANJAT (Panduan Belanja Termurah)"
              print()
              print('=' * len(self.selamat))
              print(self.selamat)
              print('=' * len(self.selamat))
              return


# Test case

# Kesimpulan

