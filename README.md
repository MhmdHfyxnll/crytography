## NAMA : MUHAMMAD HAFIYAINUL YAKIN WAHID
## NIM  : 312410164



# Sistem Cipher Klasik

Project ini dibuat untuk memenuhi tugas mata kuliah yang membahas tentang **cipher klasik**.

Pada project ini terdapat 3 aplikasi sederhana untuk melakukan proses enkripsi dan dekripsi, yaitu:

* Caesar Cipher
* Vigenère Cipher
* Columnar Transposition Cipher

Semua aplikasi dibuat menggunakan **Python dan Tkinter** sehingga bisa dijalankan dengan tampilan GUI.

## 1. Caesar Cipher

Caesar Cipher adalah metode enkripsi dengan cara menggeser setiap huruf berdasarkan jumlah pergeseran yang diberikan.

Contohnya jika menggunakan kunci `3`:

```text
A → D
B → E
C → F
```

Jadi jika plaintext:

```text
HALO
```

dengan kunci `3`, hasil enkripsinya:

```text
KDOR
```

Aplikasi ini memiliki fitur:

* Enkripsi
* Dekripsi
* Input kunci 0–25
* Tampilan GUI

## 2. Vigenère Cipher

Vigenère Cipher menggunakan sebuah kata sebagai kunci. Setiap huruf pada kunci digunakan untuk menentukan pergeseran huruf pada plaintext.

Contoh:

```text
Plaintext : HELLO
Kunci     : KEY
```

Kunci akan digunakan berulang jika panjang plaintext lebih panjang dari kunci.

Aplikasi ini memiliki fitur:

* Enkripsi
* Dekripsi
* Input kunci berupa huruf
* Tampilan GUI

## 3. Columnar Transposition Cipher

Columnar Transposition Cipher merupakan metode yang mengubah posisi huruf dengan cara menyusun plaintext ke dalam tabel, kemudian membaca kolom berdasarkan urutan kunci.

Contoh kunci:

```text
TOMBAK
```

Plaintext disusun ke dalam beberapa kolom sesuai panjang kunci, kemudian kolom dibaca berdasarkan urutan huruf pada kunci.

Aplikasi ini memiliki fitur:

* Enkripsi
* Dekripsi
* Input kunci
* Tampilan GUI

## Teknologi

* Python 3
* Tkinter
* Git
* GitHub

## Cara Menjalankan

Pastikan Python dan Tkinter sudah terinstall.

Jika Tkinter belum ada di Linux Mint:

```bash
sudo apt install python3-tk
```

Kemudian masuk ke folder aplikasi dan jalankan:

### Caesar Cipher

```bash
cd caesar-cipher
python3 app.py
```

### Vigenère Cipher

```bash
cd vigenere-cipher
python3 app.py
```

### Columnar Transposition Cipher

```bash
cd columnar-transposition-cipher
python3 app.py
```

## Struktur Folder

```text
caesar-cipher/
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE

vigenere-cipher/
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE

columnar-transposition-cipher/
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Tujuan

Project ini dibuat untuk memahami cara kerja beberapa metode cipher klasik dan mencoba menerapkannya dalam bentuk aplikasi sederhana yang dapat digunakan untuk melakukan enkripsi dan dekripsi teks.
