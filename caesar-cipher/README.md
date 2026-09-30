# Caesar Cipher

Aplikasi GUI sederhana untuk melakukan **enkripsi dan dekripsi menggunakan Caesar Cipher**.

Project ini dibuat sebagai tugas implementasi sistem cipher klasik berdasarkan materi kuliah **Ragam Cipher Klasik**.

## Fitur

- Enkripsi teks menggunakan Caesar Cipher
- Dekripsi ciphertext menggunakan Caesar Cipher
- Kunci/pergeseran 0-25
- Mempertahankan spasi, angka, dan tanda baca
- GUI menggunakan Python Tkinter
- Dapat dijalankan langsung di Linux Mint

## Konsep Caesar Cipher

Caesar Cipher merupakan cipher substitusi. Setiap huruf alfabet digeser sebanyak nilai kunci tertentu.

Untuk kunci `k`:

```text
Enkripsi : C = (P + k) mod 26
Dekripsi : P = (C - k) mod 26
```

Keterangan:

- `P` = plaintext
- `C` = ciphertext
- `k` = kunci/pergeseran

Contoh dengan `k = 3`:

```text
A → D
B → E
C → F
...
X → A
Y → B
Z → C
```

## Contoh Penggunaan

Plaintext:

```text
HALO DUNIA
```

Kunci:

```text
3
```

Hasil enkripsi:

```text
K DOR GXQLD
```

Untuk mendapatkan plaintext kembali, masukkan ciphertext dan gunakan tombol **Dekripsi** dengan kunci yang sama.

> Catatan: aplikasi ini memproses huruf alfabet dan mempertahankan karakter non-alfabet seperti spasi, angka, dan tanda baca.

## Persyaratan

- Python 3
- Tkinter

Pada Linux Mint, jika Tkinter belum tersedia:

```bash
sudo apt update
sudo apt install python3-tk
```

## Cara Menjalankan

Masuk ke folder project:

```bash
cd caesar-cipher
```

Jalankan:

```bash
python3 app.py
```

GUI Caesar Cipher akan terbuka.

## Struktur Project

```text
caesar-cipher/
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Upload ke GitHub

Buat repository baru di GitHub dengan nama:

```text
caesar-cipher
```

Kemudian jalankan:

```bash
cd caesar-cipher

git init
git add .
git commit -m "Initial commit - Caesar Cipher GUI"
git branch -M main
git remote add origin https://github.com/USERNAME/caesar-cipher.git
git push -u origin main
```

Ganti `USERNAME` dengan username GitHub kamu.

## Referensi Materi

Implementasi ini mengacu pada materi kuliah **02 – Ragam Cipher Klasik (Bagian 1)**, khususnya bagian Caesar Cipher.
