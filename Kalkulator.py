from tkinter import *
import datetime
now=datetime.datetime.now()

class Kalkulator:

    def __init__(self, master):
        # menginisiasikan master gui kalkulator
        self.master = master
        master.title("Kalkulator Python Sederhana")
        self.master.config(bg="#D3D3D3")
        # Membuat kotak inputan kalkulator
        self.persamaan=Entry(master, width=50)
        self.persamaan.grid(row=0, column=0, columnspan=10, padx=20, pady=20)
        self.buatbutton()
        

        # Panggil Konversi Suhu
        kotakentrysuhu=KonversiRupiah(master)
        kotakentrysuhu.kotakkonversirupiah()
        kotakentrysuhu.buatbutton()
        # Tampil Nama Username
        hello=Data(tampungusername[0]).tampil()
        t = Label(root,text='Hello: '+hello)
        t.grid(row=300, column=2, sticky='SW', columnspan=4)

        # Memposisikan text dibawah kalkulator
        date_time = now.strftime("%d-%m-%Y")
        t1 = Label(root,text='Sekarang Tanggal: '+date_time)
        t1.grid(row=350, column=2, sticky='SW', columnspan=4)      

 
 


    def buatbutton(self):
        angka0 = self.Button(0)
        angka1 = self.Button(1)
        angka2 = self.Button(2)
        angka3 = self.Button(3)
        angka4 = self.Button(4)
        angka5 = self.Button(5)
        angka6 = self.Button(6)
        angka7 = self.Button(7)
        angka8 = self.Button(8)
        angka9 =  self.Button(9)
        buttontambah = self.Button('+')
        buttonkurang = self.Button('-')
        buttonkali = self.Button('*')
        buttonbagi = self.Button('/')
        buttonbersihkan = self.Button('C')
        buttonsamadengan = self.Button('=')
        buttonModulus = self.Button('%')
        buttonPangkat = self.Button('K')
        
        # menampung  tampilan tombol tombol
        row1=[buttonbersihkan,angka0,buttonsamadengan,buttonkali]
        row2=[angka7,angka8,angka9,buttonbagi]
        row3=[angka4,angka5,angka6,buttontambah]
        row4=[angka1,angka2,angka3,buttonkurang]
        row5 = [buttonModulus, buttonPangkat]

        # menampilkan tombol dan tertata secara rapi menggunakan looping for
        tampildiguibuttonsemua=1
        for row in [row1, row2, row3, row4,row5]:
            indendasikolom=2
            for buttn in row:
                buttn.grid(row=tampildiguibuttonsemua, column=indendasikolom, columnspan=1)
                indendasikolom+=1
            tampildiguibuttonsemua+=1


    
    def clickButton(self, value):

        #dapatkan dari user input
        current_persamaan=str(self.persamaan.get())
        
        if  value=='C':
            self.persamaan.delete(-1, END)

        if value == 'K':
            answer = int(current_persamaan) * int(current_persamaan)
            self.persamaan.delete(-1, END)
            self.persamaan.insert(0,answer)
        #Menanmpilkan hasil
        elif value == '=':
            answer = str(eval(current_persamaan))
            self.persamaan.delete(-1, END)
            self.persamaan.insert(0, answer)
        
        # elif value == 'M':
        #     answer = str(current_persamaan)
        #     x=answer % answer
        #     self.persamaan.delete(-1,END)
        #     self.persamaan.insert()

        #Agar tombol bisa diklik
        else:
            self.persamaan.delete(0, END)
            self.persamaan.insert(-1, current_persamaan+value)
    def Button(self,value):
        # mengembalikan master,warna dan value angka
        return Button(self.master, text=value, width=9,bg='#B6D0D4',fg='#000000', command = lambda: self.clickButton(str(value)))

class KonversiRupiah(Kalkulator):
    def __init__(self, masterrupiah):
        self.masterrupiah=masterrupiah
        # self.persamaanrupiah=Entry(masterrupiah, width=50)
        # self.persamaanrupiah.grid(row=0, column=0, columnspan=10, padx=20, pady=20)

    def kotakkonversirupiah(self):
        self.kotakkonversirupiah1 = Entry(self.masterrupiah, width=50)
        self.kotakkonversirupiah1.grid(row=50, column=0, columnspan=10, padx=20, pady=20,sticky="S")

    def buatbutton(self):
        angka0 = self.Button("USD")
        buttonkali = self.Button('EURO')
        buttonbersihkan = self.Button('GBP')
        buttonsamadengan = self.Button('C')

        # menampung  tampilan tombol tombol
        row1=[buttonbersihkan,angka0,buttonsamadengan,buttonkali]

    
        # menampilkan tombol dan tertata secara rapi menggunakan looping for

        for row in [row1]:
            indendasikolom=2
            for buttn in row:
                buttn.grid(row=400, column=indendasikolom, columnspan=1,sticky="SW")
                indendasikolom+=1



    
    def clickButton(self, value):

        #dapatkan dari user input
        current_persamaan1=float(self.kotakkonversirupiah1.get())
        
        if  value=='C':
            self.kotakkonversirupiah1.delete(-1, END)
        elif value=='GBP':
            answer=float(current_persamaan1/17987)
            self.kotakkonversirupiah1.delete(-1,END)
            self.kotakkonversirupiah1.insert(0, answer)
        elif value=='EURO':
            answer=float(current_persamaan1/15270)
            self.kotakkonversirupiah1.delete(-1,END)
            self.kotakkonversirupiah1.insert(0, answer)

        elif value=='USD':
            answer=float(current_persamaan1/14665)
            self.kotakkonversirupiah1.delete(-1,END)
            self.kotakkonversirupiah1.insert(0, answer)


          #Agar biar multiple fungsi Matematika
        else:
            self.kotakkonversirupiah1.delete(0, END)
            self.kotakkonversirupiah1.insert(-1, current_persamaan1)
        
    def Button(self,value):
        # mengembalikan master,warna dan value angka
        return Button(self.masterrupiah, text=value, width=9,bg='#B6D0D4',fg='#000000', command = lambda: self.clickButton(str(value)))




class Data():
    def __init__(self, nama):
        self.nama=nama
    def tampil(self):
        return self.nama




if __name__=='__main__':
    username=input("Masukan Nama Anda: ")
    cocokanusername=Data(username).tampil()
    tampungusername=[]
    tampungusername.append(cocokanusername)
    if username:
        root = Tk()
        gui=Kalkulator(root)
        root.resizable(False, False) #Mematikan Maximize
        root.mainloop()
    else:
        print("Anda wajib memasukan username")
        


