import tkinter as tk
from tkinter import ttk, messagebox

ALPHABET_SIZE = 26


def validate_key(key):
    key = key.strip()

    if not key:
        raise ValueError("Kunci harus diisi.")

    if not key.isalpha() or not key.isascii():
        raise ValueError("Kunci hanya boleh berisi huruf A-Z.")

    return key.upper()


def vigenere_cipher(text, key, decrypt=False):
    key = validate_key(key)
    result = []
    key_index = 0

    for char in text:
        if char.isalpha() and char.isascii():
            base = ord("A") if char.isupper() else ord("a")

            text_value = ord(char.upper()) - ord("A")
            key_value = ord(key[key_index % len(key)]) - ord("A")

            if decrypt:
                shifted = (text_value - key_value) % ALPHABET_SIZE
            else:
                shifted = (text_value + key_value) % ALPHABET_SIZE

            result.append(chr(base + shifted))
            key_index += 1
        else:
            # Spasi, angka, tanda baca, dan karakter non-alfabet
            # tidak menggeser posisi kunci.
            result.append(char)

    return "".join(result)


class VigenereCipherApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Vigenère Cipher")
        self.geometry("720x590")
        self.minsize(620, 520)

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
        style.configure(
            "Action.TButton",
            font=("Sans", 10, "bold"),
            padding=8
        )

    def create_widgets(self):
        header = ttk.Frame(self)
        header.pack(fill="x", pady=(0, 15))

        ttk.Label(
            header,
            text="Vigenère Cipher",
            style="Title.TLabel"
        ).pack(anchor="w")

        ttk.Label(
            header,
            text="Enkripsi dan dekripsi teks menggunakan cipher abjad-majemuk",
            style="Subtitle.TLabel"
        ).pack(anchor="w", pady=(4, 0))

        key_frame = ttk.Frame(self)
        key_frame.pack(fill="x", pady=(0, 15))

        ttk.Label(
            key_frame,
            text="Kunci:",
            style="Section.TLabel"
        ).pack(side="left")

        self.key_var = tk.StringVar(value="KEY")

        self.key_entry = ttk.Entry(
            key_frame,
            textvariable=self.key_var,
            width=20
        )
        self.key_entry.pack(side="left", padx=(10, 10))

        ttk.Label(
            key_frame,
            text="Contoh: KEY, LAMPION, RAHASIA"
        ).pack(side="left")

        input_frame = ttk.LabelFrame(
            self,
            text="Plaintext / Ciphertext"
        )
        input_frame.pack(
            fill="both",
            expand=True,
            pady=(0, 12)
        )

        self.input_text = tk.Text(
            input_frame,
            height=8,
            wrap="word",
            font=("Sans", 11),
            padx=10,
            pady=10
        )
        self.input_text.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=8
        )

        button_frame = ttk.Frame(self)
        button_frame.pack(fill="x", pady=(0, 12))

        ttk.Button(
            button_frame,
            text="🔒 Enkripsi",
            style="Action.TButton",
            command=self.encrypt
        ).pack(
            side="left",
            expand=True,
            fill="x",
            padx=(0, 5)
        )

        ttk.Button(
            button_frame,
            text="🔓 Dekripsi",
            style="Action.TButton",
            command=self.decrypt
        ).pack(
            side="left",
            expand=True,
            fill="x",
            padx=5
        )

        ttk.Button(
            button_frame,
            text="🗑 Bersihkan",
            style="Action.TButton",
            command=self.clear
        ).pack(
            side="left",
            expand=True,
            fill="x",
            padx=(5, 0)
        )

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
        self.output_text.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=8
        )

        ttk.Label(
            self,
            text=(
                "Kunci diulang sepanjang teks. "
                "Spasi, angka, dan tanda baca tidak menggunakan karakter kunci."
            ),
            style="Subtitle.TLabel"
        ).pack(anchor="w", pady=(8, 0))

    def get_input_and_key(self):
        text = self.input_text.get("1.0", "end-1c")
        key = self.key_var.get()

        if not text:
            raise ValueError("Masukkan teks terlebih dahulu.")

        key = validate_key(key)

        return text, key

    def show_result(self, result):
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", result)

    def encrypt(self):
        try:
            text, key = self.get_input_and_key()
            result = vigenere_cipher(text, key, decrypt=False)
            self.show_result(result)
        except ValueError as error:
            messagebox.showerror("Input Tidak Valid", str(error))

    def decrypt(self):
        try:
            text, key = self.get_input_and_key()
            result = vigenere_cipher(text, key, decrypt=True)
            self.show_result(result)
        except ValueError as error:
            messagebox.showerror("Input Tidak Valid", str(error))

    def clear(self):
        self.input_text.delete("1.0", "end")
        self.output_text.delete("1.0", "end")
        self.key_var.set("KEY")
        self.input_text.focus_set()


if __name__ == "__main__":
    app = VigenereCipherApp()
    app.mainloop()
