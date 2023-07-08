#!/usr/bin/env python
# coding: utf-8

# In[1]:


### main_cashier.py

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

