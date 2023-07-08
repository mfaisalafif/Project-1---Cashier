#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###   module1_cashier.py
###   Panjat --> Panduan Belanja Termurah

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
    

