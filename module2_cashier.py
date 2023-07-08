#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###   module2_cashier.py
###   Panjat --> Panduan Belanja Termurah
###   BelanjaPanjat --> Keranjang untuk Belanja di Panduan Belanja Termurah


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

