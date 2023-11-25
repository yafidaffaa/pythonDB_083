import tkinter as tk
from tkinter import messagebox
import sqlite3

top = tk.Tk()
top.title("Pemrogramman Kelas B")
top.geometry("400x400")
top.resizable(False,False)

def simpan_data_ke_sqlite(nama_siswa, Biologi, Fisika, Inggris, prediksi_fakultas):
    """Membuka atau membuat database SQLite"""
    conn = sqlite3.connect("Prediksi_Fakultas.db")
    cursor = conn.cursor()

    """Membuat tabel jika belum ada"""
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa
    ( 
    nama_siswa TEXT,
    Biologi INTEGER,
    Fisika INTEGER,
    Inggris INTEGER,                
    Prediksi_fakultas TEXT)''')
    
    """Memasukkan data mata pelajaran ke dalam tabel"""
    cursor.execute("INSERT INTO nilai_siswa (nama_siswa, Biologi, Fisika, Inggris, Prediksi_fakultas) VALUES (?, ?, ?, ?, ?)",
    (nama_siswa, Biologi, Fisika, Inggris, prediksi_fakultas))
    """ Melakukan commit dan menutup koneksi"""
    conn.commit()
    conn.close()

#Membuat label untuk judul
var = tk.Label(text="Aplikasi Prediksi Prodi Pilihan")
var.pack(side=tk.TOP)

inputFame = tk.LabelFrame(top)
inputFame.pack(padx=10, pady= 10, fill="x", expand=True)

#Membuat Input 1
Input1 = tk.Label(inputFame,text= "Masukan Nama Siswa: ")
Input1.pack(padx=10, pady=5, fill="x", expand=True)

E1 = tk.Entry(inputFame)
E1.pack(padx=10, pady= 5, fill="x", expand=True)

#Membuat Input 2
Input2 = tk.Label(inputFame,text= "Masukan Nilai Biologi: ")
Input2.pack(padx=10, pady=5, fill="x", expand=True)

E2 = tk.Entry(inputFame)
E2.pack(padx=10, pady= 5, fill="x", expand=True)

#Membuat Input 3
Input3 = tk.Label(inputFame,text= "Masukan Nilai Fisika: ")
Input3.pack(padx=10, pady=5, fill="x", expand=True)

E3 = tk.Entry(inputFame)
E3.pack(padx=10, pady= 5, fill="x", expand=True)

#Membuat Input 4
Input4 = tk.Label(inputFame,text= "Masukan Nilai Inggris: ")
Input4.pack(padx=10, pady=5, fill="x", expand=True)

E4 = tk.Entry(inputFame)
E4.pack(padx=10, pady= 5, fill="x", expand=True)

def prediksi():
    biologi = float(E2.get())
    fisika = float(E3.get())
    inggris = float(E4.get())

    if biologi > fisika and inggris :
        return "Kedokteran"
    elif fisika > biologi and inggris :
        return "Teknik"
    elif inggris > biologi and fisika :
        return "Bahasa"
    else :
        return "Anda lebih baik langsung kerja!!"


#Membuat function mengambil inputan(get)
def onClickButton():
    namaSiswa = E1.get()
    biologi = float(E2.get())
    fisika = float(E3.get())
    inggris = float(E4.get())

    prediksi_prodi = prediksi()
    


    print("Data Berhasil disimpan")
    simpan_data_ke_sqlite(nama_siswa= namaSiswa, Biologi= biologi, Fisika= fisika, Inggris= inggris, prediksi_fakultas= prediksi_prodi)

    messagebox.showinfo("Keterangan", f"Nama: {namaSiswa}\nPrediksi Fakultas: {prediksi_prodi}" )


#Membuat tombol submit
tombol =tk.Button(text="Submit", command=onClickButton)
tombol.pack(padx=10, pady= 5, fill="x", expand=True)


top.mainloop()

