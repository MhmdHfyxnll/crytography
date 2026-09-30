# Columnar Transposition Cipher

Aplikasi GUI sederhana untuk melakukan **enkripsi dan dekripsi menggunakan Columnar Transposition Cipher**.

Project ini dibuat sebagai implementasi cipher klasik berdasarkan materi **Ragam Cipher Klasik (Bagian 1)**.

## Fitur

- Enkripsi menggunakan Columnar Transposition Cipher
- Dekripsi ciphertext
- Kunci berupa kata
- Validasi agar setiap huruf pada kunci berbeda
- GUI menggunakan Python Tkinter
- Dapat dijalankan di Linux Mint

## Konsep Columnar Transposition

Columnar Transposition Cipher termasuk **cipher transposisi**.

Pada cipher transposisi, posisi huruf pada plaintext diubah sehingga menghasilkan susunan ciphertext yang berbeda.

Materi menjelaskan bahwa plaintext dapat disusun ke dalam tabel berdasarkan panjang kunci, kemudian ciphertext diperoleh dengan membaca kolom secara vertikal.

Contoh dari materi:

```text
Plaintext:
SISTEM DAN TEKNOLOGI INFORMASI ITB

Kunci:
TOMBAK
```

Setelah spasi dibuang dan plaintext disusun berdasarkan panjang kunci, hasil dibaca secara vertikal sesuai urutan huruf pada kunci.

Urutan alfabet kunci `TOMBAK` digunakan untuk menentukan urutan pembacaan kolom.

## Contoh Sederhana

Plaintext:

```text
SISTEMDANTEKNOLOGIINFORMASIITB
```

Kunci:

```text
TOMBAK
```

Program menyusun plaintext ke dalam tabel dengan jumlah kolom sesuai panjang kunci, kemudian membaca kolom berdasarkan urutan alfabet karakter kunci.

## Catatan

Untuk mempermudah proses dan mengikuti contoh pada materi, aplikasi ini menggunakan kunci dengan **huruf yang berbeda**.

Contoh valid:

```text
TOMBAK
KUNCI
RAHASIA
```

Namun `KUNCI` memiliki huruf I yang hanya sekali dan valid; sedangkan kunci yang memiliki karakter berulang seperti `BANANA` ditolak oleh aplikasi.

Spasi plaintext dihapus selama proses enkripsi/dekripsi.

## Persyaratan

- Python 3
- Tkinter

Pada Linux Mint, jika Tkinter belum tersedia:

```bash
sudo apt update
sudo apt install python3-tk
```

## Cara Menjalankan

Masuk ke folder:

```bash
cd columnar-transposition-cipher
```

Jalankan:

```bash
python3 app.py
```

## Struktur Project

```text
columnar-transposition-cipher/
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Upload ke GitHub

Buat repository baru di GitHub dengan nama:

```text
columnar-transposition-cipher
```

Kemudian jalankan:

```bash
cd columnar-transposition-cipher

git init
git add .
git commit -m "Initial commit - Columnar Transposition Cipher GUI"
git branch -M main
git remote add origin https://github.com/USERNAME/columnar-transposition-cipher.git
git push -u origin main
```

Ganti `USERNAME` dengan username GitHub kamu.

## Referensi Materi

Implementasi ini mengacu pada bagian **Cipher Transposisi**, khususnya **Columnar Transposition Cipher** pada materi Ragam Cipher Klasik.
