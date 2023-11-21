import tkinter as tk
import sqlite3

def hasil_prediksi():
    # Mengambil nilai dari input pengguna
    nilai_biologi = float(input_nilai[0].get())
    nilai_fisika = float(input_nilai[1].get())
    nilai_inggris = float(input_nilai[2].get())
    nama_siswa = input_nama_siswa.get()

    # Menentukan prodi pilihan berdasarkan nilai tertinggi
    if nilai_biologi > nilai_fisika and nilai_biologi > nilai_inggris:
        prodi_pilihan = "Kedokteran"
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
        prodi_pilihan = "Teknik"
    elif nilai_inggris > nilai_biologi and nilai_inggris > nilai_fisika:
        prodi_pilihan = "Bahasa"
    else:
        prodi_pilihan = "Prodi Pilihan Tidak Dapat Diprediksi"

    # Menampilkan hasil prediksi
    output_label.config(text=f"Prodi Pilihan: {prodi_pilihan}")

    # Menyimpan data ke database SQLite
    simpan_data_ke_sqlite(nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prodi_pilihan)

def simpan_data_ke_sqlite(nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prodi_terpilih):
    # Membuka atau membuat database SQLite
    conn = sqlite3.connect("tkinterdata.db")
    cursor = conn.cursor()

    # Membuat tabel jika belum ada
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       nama_siswa TEXT,
                       biologi REAL,
                       fisika REAL,
                       inggris REAL,
                       prediksi_fakultas TEXT)''')

    # Memasukkan data nilai siswa ke dalam tabel
    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prodi_terpilih))

    # Melakukan commit dan menutup koneksi
    conn.commit()
    conn.close()

# Membuat GUI menggunakan Tkinter
uiApp = tk.Tk()
uiApp.configure(background='black')
uiApp.geometry("800x600")  # Ubah ukuran jendela utama
uiApp.resizable(False, False)
uiApp.title('Aplikasi Prediksi Prodi Pilihan')

# Membuat frame
inputFrame = tk.Frame(uiApp)
inputFrame.pack(padx=10, fill="x", expand=True)

# Label Judul dengan ukuran font lebih besar
judul_label = tk.Label(inputFrame, text="Aplikasi Prediksi Prodi Pilihan")
judul_label.pack(pady=10)

# Entry Nama Siswa
input_nama_siswa_label = tk.Label(inputFrame, text="Nama Siswa:")
input_nama_siswa_label.pack()
input_nama_siswa = tk.Entry(inputFrame)
input_nama_siswa.pack()

# 10 Input Nilai Mata Pelajaran
input_label = tk.Label(inputFrame, text="Masukkan Nilai Mata Pelajaran")
input_label.pack(pady=5)

mata_pelajaran = ["Biologi", "Fisika", "Inggris"]
input_nilai = []
for i, pelajaran in enumerate(mata_pelajaran):
    nilai_label = tk.Label(inputFrame, text=f"{pelajaran}:")
    nilai_label.pack()
    nilai_entry = tk.Entry(inputFrame)
    nilai_entry.pack()
    input_nilai.append(nilai_entry)

# Button Hasil Prediksi
button_prediksi = tk.Button(inputFrame, text="Hasil Prediksi", command=hasil_prediksi)
button_prediksi.pack(pady=5)

# Label Luaran Hasil Prediksi
output_label = tk.Label(inputFrame, text="")
output_label.config(wraplength=600)
output_label.pack()

uiApp.mainloop()
