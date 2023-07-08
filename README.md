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
Berikut ini merupakan code main_cashier di mana proses utama (_running code_) akan dijalankan, di bagian ini juga akan diimport _class Panjat_ dan _class BelanjaPanjat_ dari masing-masing module. Lalu di bagian ini akan terjadi proses input data nama dan nomor ID customer.
          
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
Berikut ini merupakan code module1_cashier di mana terdapat _class Panjat_, class ini bertujuan untuk memberikan pesan selamat datang kepada customer. Attributes yang terdapat dalam class ini adalah: _nama_ dan _id_tr_. Method yang terdapat dalam kelas ini yaitu : _Panjat.selamat_datang()_ --> untuk memeberi pesan selamat datang.

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

## 3. module2_cashier.py
Berikut ini merupakan code module2_cashier di mana terdapat _class BelanjaPanjat_, class ini bertujuan untuk menjalankan proses transaksi. Attributes yang terdapat dalam class ini adalah: _keranjang_, yang berupa dictionary untuk menyimpan nama, jumlah dan harga barang.

      import pandas as pd
      """Melakukan import pandas untuk menampilkan data dalam bentuk tabel"""
      
      class BelanjaPanjat:
          """
          Membuat class BelanjaPanjat untuk transaksi self-checkout
          ---------------------------------------------------------
              
          Attribute
          ---------
          keranjang = dict
              Di awal berisi dictionary kosong yang kemudian dictionary tersebut akan diisi nama, jumlah dan harga barang oleh customer
              
          Methods
          -------
          tambah_barang()
              Menambahkan barang ke dalam keranjang belanja dengan menginput nama, jumlah dan harga barang
          lihat_keranjang()
              Melihat isi keranjang belanja
          update_barang()
              Megupdate nama, jumlah atau harga barang
          hapus_barang()
              Menghapus suatu barang dari keranjang belanja
          kosongkan_keranjang()
              Melakukan reset keranjang belanja atau menghapus semua barang dari keranjang belanja
          total_belanja()
              Melihat isi keranjang belanja dalam bentuk tabel dan total harga sementara
          total_belanja_akhir()
              Melakukan pengecekan apakah customer mendapatkan diskon sesuai dengan ketentuan dan melihat total harga akhir yang perlu dibayar   
          """
          
          def __init__(self):
              """
              Constructor untuk class BelanjaPanjat
              -------------------------------------
      
              Parameters
              ----------
              Tidak terdapat parameter pada Constructor
      
              Attribute
              ---------
              keranjang = dict
                  Di awal berisi dictionary kosong yang kemudian dictionary tersebut akan diisi nama, jumlah dan harga barang oleh customer
              """
              self.keranjang = {}

### 3.1 method tambah_barang() 
Method ini befungsi untuk menambahkan barang ke dalam keranjang belanja dengan menginput nama, jumlah dan harga barang.

      def tambah_barang(self):
           """
           Method untuk menambahkan barang ke dalam keranjang belanja dengan menginput nama, jumlah dan harga barang
           ---------------------------------------------------------------------------------------------------------
           
           Attribute
           ---------
           keranjang = dict
               Di awal berisi dictionary kosong yang kemudian dictionary tersebut akan diisi nama, jumlah dan harga barang oleh customer
          
           Parameters
           ----------
           Tidak terdapat parameter pada method ini
   
           Variables
           ----------
           item = str
               Nama barang
           quantity = int
               Jumlah barang
           price = int
               Harga barang
           """
           ## Looping untuk melakukan pengisian nama, jumlah dan harga barang
           while True:
               item = input("Silahkan input barang yang ingin anda beli (atau ketik 'cukup' jika sudah selesai): ")
               if item.lower() == "cukup":
                   break
               while item.strip() == "":
                   print("Nama barang tidak boleh kosong. Silahkan diisi nama barang yang ingin dibeli.")
                   item = input("Silahkan input barang yang ingin anda beli (atau ketik 'cukup' jika sudah selesai): ")
                   if item.lower() == "cukup":
                       break
               
               if item.lower() == "cukup":
                   break
               
               quantity = None
               while quantity is None:
                   try:
                       quantity = int(input("Silahkan input jumlah barang tersebut: "))
                   except ValueError:
                       print("Jumlah barang tidak valid. Silahkan input jumlah barang (bilangan bulat).")
               
               price = None
               while price is None:
                   try:
                       price = int(input("Silahkan input harga barang tersebut: "))
                   except ValueError:
                       print("Harga barang tidak valid. Silahkan input harga barang (bilangan bulat).")
                       
               if item in self.keranjang:
                   # Jika barang sudah ada di dalam keranjang maka akan menambahkan jumlah dan mengupdate harga barang
                   self.keranjang[item][0] += quantity
                   self.keranjang[item][1] = price
               else:
                   # Jika barang tidak ada di dalam keranjang belanja maka akan menambahkan barang, jumlah dan harta baru
                   self.keranjang[item] = [quantity, price]

### 3.2 method lihat_keranjang()
Method ini befungsi untuk melihat isi keranjang belanja.

    def lihat_keranjang(self):
        """
        Method untuk melihat isi keranjang belanja
        ------------------------------------------
        
        Attribute
        ---------
        keranjang = dict
            Di awal berisi dictionary kosong yang kemudian dictionary tersebut akan diisi nama, jumlah dan harga barang oleh customer
       
        Parameters
        ----------
        Tidak terdapat parameter pada method ini

        Variables
        ----------
        index = int
            No urut barang yang dibeli
        item = str
            Nama barang
        quantity = int
            Jumlah barang
        price = int
            Harga barang
        details = list
            List jumlah dan harga dari setiap barang
        items = list
            List nama, jumlah dan harga dari setiap barang
        """
        if not self.keranjang:
            print("Keranjang belanja kosong.")
        else:
            print("Keranjang belanja anda:")
            print("------------------")
            index = 1
            for item, details in self.keranjang.items():
                quantity, price = details
                print(f"Barang {index}: {item}")
                print(f"Jumlah barang: {quantity}")
                print(f"Harga: {price}")
                print("------------------")  
                index += 1

### 3.3 method update_barang()
Method ini befungsi untuk mengupdate nama, jumlah atau harga barang.

    def update_barang(self):
        """
        Method untuk mengupdate nama, jumlah atau harga barang
        ------------------------------------------------------
        
        Attribute
        ---------
        keranjang = dict
            Di awal berisi dictionary kosong yang kemudian dictionary tersebut akan diisi nama, jumlah dan harga barang oleh customer
       
        Parameters
        ----------
        Tidak terdapat parameter pada method ini

        Variables
        ----------
        item = str
            Nama barang yang ingin diganti
        new_item = str
            Nama barang yang baru sebagai pengganti
        quantity = int
            Jumlah barang
        price = int
            Harga barang
        """
        item = input("Silahkan input barang yang ingin anda update: ")
        if item in self.keranjang:
            new_item = input("Input nama barang yang baru (atau kosongkan jika hanya ingin mengganti jumlah atau harga): ")
            
            quantity = None
            while quantity is None:
                try:
                    quantity = int(input("Input jumlah barang yang baru: "))
                except ValueError:
                    print("Jumlah barang tidak valid. Silahkan input harga barang (bilangan bulat).")
            
            price = None
            while price is None:
                try:
                    price = int(input("Input harga barang yang baru: "))
                except ValueError:
                    print("Harga barang tidak valid. Silahkan input harga barang (bilangan bulat).")
            
            ## Mengupdate nama barang yang ingin diganti dengan nama barang baru jika input tidak kosong
            if new_item.strip() != '':
                self.keranjang[new_item] = self.keranjang.pop(item)
                item = new_item
            
            ## Mengupdate jumlah barang dan harga barang
            self.keranjang[item][0] = quantity
            self.keranjang[item][1] = price
        else:
            print(f"{item} tidak ada di dalam keranjang belanja.")

### 3.4 method hapus_barang()
Method ini befungsi untuk menghapus suatu barang dari keranjang belanja.

    def hapus_barang(self):
        """
        Method untuk menghapus suatu barang dari keranjang belanja
        ----------------------------------------------------------
        
        Attribute
        ---------
        keranjang = dict
            Di awal berisi dictionary kosong yang kemudian dictionary tersebut akan diisi nama, jumlah dan harga barang oleh customer
       
        Parameters
        ----------
        Tidak terdapat parameter pada method ini

        Variables
        ---------
        item = str
            Nama barang yang ingin diganti
        """
        item = input("Silahkan input barang yang ingin anda hapus: ")
        
        if item in self.keranjang:
            del self.keranjang[item]
            print(f"{item} sudah dihapus dari keranjang belanja.")
        else:
            print(f"{item} tidak ada di dalam keranjang belanja.")

### 3.5 method kosongkan_keranjang()
Method ini befungsi untuk melakukan reset keranjang belanja atau menghapus semua barang dari keranjang belanja.

    def kosongkan_keranjang(self):
        """
        Method untuk melakukan reset keranjang belanja atau menghapus semua barang dari keranjang belanja
        -------------------------------------------------------------------------------------------------
        
        Attribute
        ---------
        keranjang = dict
            Di awal berisi dictionary kosong yang kemudian dictionary tersebut akan diisi nama, jumlah dan harga barang oleh customer
       
        Parameters
        ----------
        Tidak terdapat parameter pada method ini

        Variables
        ---------
        Tidak terdapat variable pada method ini
        """
        self.keranjang = {}
        print("Keranjang belanja berhasil dikosongkan (reset).")

### 3.6 method total_belanja()
Method ini befungsi untuk melihat isi keranjang belanja dalam bentuk tabel dan total harga sementara.

    def total_belanja(self):
        """
        Method untuk melihat isi keranjang belanja dalam bentuk tabel dan total harga sementara
        ---------------------------------------------------------------------------------------
        
        Attribute
        ---------
        keranjang = dict
            Di awal berisi dictionary kosong yang kemudian dictionary tersebut akan diisi nama, jumlah dan harga barang oleh customer
       
        Parameters
        ----------
        subtotal_harga = int
            Perkalian antara jumlah dengan harga masing-masing barang 
        total_payment = int
            Total harga seluruh barang sebelum diskon
            
        Variables
        ---------
        item = str
            Nama barang
        details = list
            List jumlah dan harga dari setiap barang
        items = list
            List nama, jumlah dan harga dari setiap barang           
        quantity = int
            Jumlah barang
        price = int
            Harga barang
        quantities = list
            List jumlah dari setiap barang
        prices = list
            List harga dari setiap barang
        subtotal_costs = list
            List subtotal harga dari setiap barang
        data = dict
            Dictionary untuk menyimpan daftar nama, jumlah, harga dan subtotal dari seluruh barang di keranjang
        pd.DataFrame = class in pandas
            Memanggil class DataFrame untuk membuat data structure 
        df = convert dict into dataframe
            Bentuk tabel dari data
        df.index = method dari dataframe
            Memanggil index dari tabel/dataframe --> ditambah 1 agar outcome dimulai dari angka 1 
        """
        for item, details in self.keranjang.items():
            quantity, price = details
            if quantity == 0 or price == 0:
                print(f"Terdapat kesalahan input data, harga atau jumlah barang belum diinput untuk barang berikut: {item}")
                return
        
        items = []
        quantities = []
        prices = []
        subtotal_costs = []
        total_payment = 0
        
        for item, details in self.keranjang.items():
            quantity, price = details
            subtotal_harga = quantity * price
            
            items.append(item)
            quantities.append(quantity)
            prices.append(price)
            subtotal_costs.append(subtotal_harga)
            
            total_payment += subtotal_harga
        
        data = {'Barang': items,'Jumlah barang': quantities,'Harga per unit': prices,'Subtotal harga': subtotal_costs}
        
        df = pd.DataFrame(data)
        df.index = df.index + 1 
        
        print("Isi keranjang belanja anda sebagai berikut: ")
        print(df)
        print(f"Total harga belanja anda adalah : {total_payment}")
        print("Semua barang belanja anda bisa di-check out. Silahkan untuk melakukan pembayaran atau cek diskon terlebih dulu.")
        

### 3.7 method total_belanja_akhir()
Method ini befungsi untuk mengecek apakah customer mendapatkan diskon sesuai dengan ketentuan dan melihat total harga akhir yang perlu dibayar.

    def total_belanja_akhir(self):
        """
        Method untuk mengecek apakah customer mendapatkan diskon sesuai dengan ketentuan dan melihat total harga akhir yang perlu dibayar
        ---------------------------------------------------------------------------------------------------------------------------------
        
        Attribute
        ---------
        keranjang = dict
            Di awal berisi dictionary kosong yang kemudian dictionary tersebut akan diisi nama, jumlah dan harga barang oleh customer
       
        Parameters
        ----------
        subtotal_harga = int
            Perkalian antara jumlah dengan harga masing-masing barang 
        total_payment = int
            Total harga seluruh barang sebelum diskon
        total_belanja_akhir = float
            Total harga akhir yang diperoleh dari harga awal dikurangi dengan total diskon (harga awal yang dikali dengan besar diskon)
        
        Variables
        ---------
        item = str
            Nama barang
        details = list
            List jumlah dan harga dari setiap barang
        items = list
            List nama, jumlah dan harga dari setiap barang           
        quantity = int
            Jumlah barang
        price = int
            Harga barang
        
        Constant
        --------
        discount = int
            Besaran diskon sesuai dengan ketentuan berikut:
            1. jika total belanja < atau = Rp200.000 maka discount = 0%
            2. jika total belanja > Rp200.000 dan < atau = Rp300.000 maka discount = 5%
            3. jika total belanja > Rp300.000 dan < atau = Rp500.000 maka discount = 8%
            4. jika total belanja > Rp500.000 maka discount = 10%
        """
        total_payment = 0
        for item, details in self.keranjang.items():
            quantity, price = details
            if quantity == 0 or price == 0:
                print(f"Terdapat kesalahan input data, harga atau jumlah barang belum diinput untuk barang berikut: {item}")
                return
            else:
                subtotal_harga = quantity * price
                total_payment += subtotal_harga
        
        if total_payment > 500_000:
            discount = 0.1
        elif total_payment >300_000:
            discount = 0.08
        elif total_payment > 200_000:
            discount = 0.05
        else:
            discount = 0
    
        total_belanja_akhir = total_payment - total_payment * discount
        print(f"Total harga belanja anda sebelum mendapatkan diskon : {total_payment}")
        print(f"Total harga belanja anda setelah mendapatkan diskon {discount*100:.0f}% menjadi : {total_belanja_akhir}")
        print(f"Silahkan untuk melakukan pembayaran")      
        return
    
# Test case
## Pre-Test
Customer ingin menginput nama dan nomor ID dengan menggunakan fungsi _nama_dan_id()_.

![Pre_Test](https://github.com/mfaisalafif/Project01_Cashier/blob/main/Images/Nama%20dan%20ID.jpg)

## Test 1
Customer ingin menambahkan dua item baru menggunakan method _tambah_barang()_. item yang ditambahkan adalah sebagai berikut:
   - Nama item: Ayam Goreng, Qty: 2 dan harga per item: 20000
   - Nama item: Pasta Gigi, Qty: 3 dan harga per item: 15000

![Test_1](https://github.com/mfaisalafif/Project01_Cashier/blob/main/Images/Test%201.jpg)

## Test 2
Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka customer menggunakan method _hapus_barang()_ untuk menghapus item. Item yang ingin dihapus adalah Pasta Gigi.

![Test_2](https://github.com/mfaisalafif/Project01_Cashier/blob/main/Images/Test%202.jpg)

## Test 3
Customer salah memasukkan item yang ingin dibelanjakan. Daripada menghapusnya satu-satu, maka customer cukup menggunakan method _kosongkan_keranjang()_ untuk menghapus semua item yang sudah ditambahkan.

![Test_3](https://github.com/mfaisalafif/Project01_Cashier/blob/main/Images/Test%203.jpg)

## Test 4
Customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan method _total_belanja()_ dan _total_belanja_akhir()_. Sebelum mengeluarkan output total belanja akan menampilkan item-item yang dibeli.

![Test_4](https://github.com/mfaisalafif/Project01_Cashier/blob/main/Images/Test%204.jpg)


# Suggestion and Conclusion
Sistem _self checkout_ **Panjat (Panduan Belanja Termurah)** dapat berfungsi sesuai dengan semua requirements yang diperlukan dan dapat memudahkan customer melakukan pemesanan ke supermarket tanpa harus datang ke supermarket secara langsung. Beberapa improvement yang perlu diimplementasikan dalam sistem _self checkout_ **Panjat** antara lain.
   1.	Daftar barang terlaris & daftar barang dengan potongan harga ditampilkan di menu awal
   2.	Sistem dapat menampilkan stock barang, harga, dan expired date (_product catalogue_)
   3.	Sistem dapat mengelompokkan barang sesuai dengan kategori (makanan, minuman, sayur, buah, alat rumah tangga, dst)
