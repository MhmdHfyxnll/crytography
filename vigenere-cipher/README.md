# Vigenère Cipher

Aplikasi GUI sederhana untuk melakukan **enkripsi dan dekripsi menggunakan Vigenère Cipher**.

Project ini dibuat sebagai implementasi cipher klasik berdasarkan materi **Ragam Cipher Klasik (Bagian 1)**.

## Fitur

- Enkripsi plaintext menggunakan Vigenère Cipher
- Dekripsi ciphertext menggunakan Vigenère Cipher
- Kunci berupa kata/huruf A-Z
- Kunci diulang sepanjang plaintext
- Spasi, angka, dan tanda baca dipertahankan
- GUI menggunakan Python Tkinter
- Dapat dijalankan di Linux Mint

## Konsep Vigenère Cipher

Vigenère Cipher termasuk **cipher abjad-majemuk (polyalphabetic substitution cipher)**.

Pada cipher abjad-majemuk, setiap huruf dapat menggunakan kunci yang berbeda. Cipher ini dapat dipandang sebagai gabungan beberapa cipher abjad-tunggal dengan kunci yang berbeda.

Contoh konsep dari materi:

```text
Plaintext : KRIPTOGRAFIKLASIK...
Kunci     : LAMPIONLAMPION...
```

Kunci akan diulang sampai panjangnya sesuai dengan teks yang diproses.

Untuk setiap huruf:

```text
Enkripsi : C = (P + K) mod 26
Dekripsi : P = (C - K) mod 26
```

Dengan pemetaan:

```text
A = 0
B = 1
C = 2
...
Z = 25
```

## Contoh Penggunaan

Plaintext:

```text
HELLO WORLD
```

Kunci:

```text
KEY
```

Program akan mengulang kunci:

```text
KEYKEYKEY
```

Kemudian setiap huruf alfabet diproses berdasarkan huruf kunci yang bersesuaian.

Untuk mengembalikan plaintext, masukkan ciphertext dan gunakan tombol **Dekripsi** dengan kunci yang sama.

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
cd vigenere-cipher
```

Jalankan:

```bash
python3 app.py
```

## Struktur Project

```text
vigenere-cipher/
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Upload ke GitHub

Buat repository GitHub baru dengan nama:

```text
vigenere-cipher
```

Kemudian:

```bash
cd vigenere-cipher

git init
git add .
git commit -m "Initial commit - Vigenere Cipher GUI"
git branch -M main
git remote add origin https://github.com/USERNAME/vigenere-cipher.git
git push -u origin main
```

Ganti `USERNAME` dengan username GitHub kamu.

## Referensi Materi

Implementasi ini mengikuti bagian **Cipher Abjad-Majemuk (Polyalpabetic Substitution Cipher)** pada materi kuliah Ragam Cipher Klasik.
