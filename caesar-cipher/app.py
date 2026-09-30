import tkinter as tk
from tkinter import ttk, messagebox


ALPHABET_SIZE = 26


def caesar_cipher(text, key, decrypt=False):
    """Encrypt or decrypt alphabetic characters using Caesar Cipher."""
    try:
        key = int(key)
    except ValueError:
        raise ValueError("Kunci harus berupa angka 0-25.")

    if not 0 <= key <= 25:
        raise ValueError("Kunci harus berada di antara 0 dan 25.")

    if decrypt:
        key = -key

    result = []

    for char in text:
        if char.isalpha() and char.isascii():
            base = ord("A") if char.isupper() else ord("a")
            shifted = (ord(char) - base + key) % ALPHABET_SIZE
            result.append(chr(base + shifted))
        else:
            # Spasi, angka, tanda baca, dan karakter non-alfabet dipertahankan.
            result.append(char)

    return "".join(result)


class CaesarCipherApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Caesar Cipher")
        self.geometry("720x560")
        self.minsize(620, 500)

        self.configure(padx=20, pady=20)

        self.create_styles()
        self.create_widgets()

    def create_styles(self):
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure("Title.TLabel", font=("Sans", 22, "bold"))
        style.configure("Subtitle.TLabel", font=("Sans", 10))
        style.configure("Section.TLabel", font=("Sans", 11, "bold"))
        style.configure("Action.TButton", font=("Sans", 10, "bold"), padding=8)

    def create_widgets(self):
        header = ttk.Frame(self)
        header.pack(fill="x", pady=(0, 15))

        ttk.Label(
            header,
            text="Caesar Cipher",
            style="Title.TLabel"
        ).pack(anchor="w")

        ttk.Label(
            header,
            text="Enkripsi dan dekripsi teks menggunakan metode Caesar Cipher",
            style="Subtitle.TLabel"
        ).pack(anchor="w", pady=(4, 0))

        key_frame = ttk.Frame(self)
        key_frame.pack(fill="x", pady=(0, 15))

        ttk.Label(
            key_frame,
            text="Kunci / Pergeseran (0-25):",
            style="Section.TLabel"
        ).pack(side="left")

        self.key_var = tk.StringVar(value="3")
        self.key_entry = ttk.Entry(
            key_frame,
            textvariable=self.key_var,
            width=8,
            justify="center"
        )
        self.key_entry.pack(side="left", padx=(10, 0))

        ttk.Label(
            key_frame,
            text="Contoh: 3 berarti setiap huruf digeser 3 posisi ke kanan.",
        ).pack(side="left", padx=(10, 0))

        input_frame = ttk.LabelFrame(self, text="Plaintext / Ciphertext")
        input_frame.pack(fill="both", expand=True, pady=(0, 12))

        self.input_text = tk.Text(
            input_frame,
            height=8,
            wrap="word",
            font=("Sans", 11),
            padx=10,
            pady=10
        )
        self.input_text.pack(fill="both", expand=True, padx=8, pady=8)

        button_frame = ttk.Frame(self)
        button_frame.pack(fill="x", pady=(0, 12))

        ttk.Button(
            button_frame,
            text="🔒 Enkripsi",
            style="Action.TButton",
            command=self.encrypt
        ).pack(side="left", expand=True, fill="x", padx=(0, 5))

        ttk.Button(
            button_frame,
            text="🔓 Dekripsi",
            style="Action.TButton",
            command=self.decrypt
        ).pack(side="left", expand=True, fill="x", padx=5)

        ttk.Button(
            button_frame,
            text="🗑 Bersihkan",
            style="Action.TButton",
            command=self.clear
        ).pack(side="left", expand=True, fill="x", padx=(5, 0))

        output_frame = ttk.LabelFrame(self, text="Hasil")
        output_frame.pack(fill="both", expand=True)

        self.output_text = tk.Text(
            output_frame,
            height=8,
            wrap="word",
            font=("Sans", 11),
            padx=10,
            pady=10
        )
        self.output_text.pack(fill="both", expand=True, padx=8, pady=8)

        info = ttk.Label(
            self,
            text="Karakter non-alfabet seperti spasi, angka, dan tanda baca tetap dipertahankan.",
            style="Subtitle.TLabel"
        )
        info.pack(anchor="w", pady=(8, 0))

    def get_input_and_key(self):
        text = self.input_text.get("1.0", "end-1c")

        if not text:
            raise ValueError("Masukkan teks terlebih dahulu.")

        key = self.key_var.get().strip()

        if not key:
            raise ValueError("Masukkan kunci/pergeseran.")

        return text, key

    def show_result(self, result):
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", result)

    def encrypt(self):
        try:
            text, key = self.get_input_and_key()
            result = caesar_cipher(text, key, decrypt=False)
            self.show_result(result)
        except ValueError as error:
            messagebox.showerror("Input Tidak Valid", str(error))

    def decrypt(self):
        try:
            text, key = self.get_input_and_key()
            result = caesar_cipher(text, key, decrypt=True)
            self.show_result(result)
        except ValueError as error:
            messagebox.showerror("Input Tidak Valid", str(error))

    def clear(self):
        self.input_text.delete("1.0", "end")
        self.output_text.delete("1.0", "end")
        self.key_var.set("3")
        self.input_text.focus_set()


if __name__ == "__main__":
    app = CaesarCipherApp()
    app.mainloop()
