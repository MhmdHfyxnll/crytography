import tkinter as tk
from tkinter import ttk, messagebox


def validate_key(key):
    key = key.strip().replace(" ", "")

    if not key:
        raise ValueError("Kunci harus diisi.")

    if not key.isalpha() or not key.isascii():
        raise ValueError("Kunci hanya boleh berisi huruf A-Z.")

    # Columnar Transposition klasik lebih mudah dipahami
    # jika setiap huruf kunci berbeda.
    if len(set(key.upper())) != len(key):
        raise ValueError(
            "Setiap huruf pada kunci harus berbeda.\n"
            "Contoh: TOMBAK"
        )

    return key.upper()


def get_column_order(key):
    """Return column numbers sorted alphabetically by key character."""
    return sorted(range(len(key)), key=lambda index: key[index])


def encrypt(text, key):
    key = validate_key(key)

    # Sesuai konsep materi: spasi dibuang sebelum penyusunan tabel.
    plaintext = "".join(text.split())

    if not plaintext:
        raise ValueError("Plaintext tidak boleh kosong.")

    columns = len(key)
    rows = (len(plaintext) + columns - 1) // columns

    # Isi tabel dari kiri ke kanan, baris demi baris.
    grid = []
    position = 0

    for _ in range(rows):
        row = []
        for _ in range(columns):
            if position < len(plaintext):
                row.append(plaintext[position])
                position += 1
            else:
                row.append("")
        grid.append(row)

    # Baca kolom berdasarkan urutan alfabet kunci.
    order = get_column_order(key)
    ciphertext = []

    for column in order:
        for row in grid:
            if row[column]:
                ciphertext.append(row[column])

    return "".join(ciphertext)


def decrypt(ciphertext, key):
    key = validate_key(key)

    ciphertext = "".join(ciphertext.split())

    if not ciphertext:
        raise ValueError("Ciphertext tidak boleh kosong.")

    columns = len(key)
    length = len(ciphertext)

    rows = (length + columns - 1) // columns
    remainder = length % columns

    # Pada tabel terakhir, kolom yang lebih awal mendapat karakter tambahan.
    column_lengths = []
    for column in range(columns):
        if remainder == 0:
            column_lengths.append(rows)
        elif column < remainder:
            column_lengths.append(rows)
        else:
            column_lengths.append(rows - 1)

    order = get_column_order(key)

    # Tempatkan ciphertext kembali ke kolom sesuai urutan kunci.
    columns_data = [""] * columns
    position = 0

    for column in order:
        length_for_column = column_lengths[column]
        columns_data[column] = ciphertext[
            position:position + length_for_column
        ]
        position += length_for_column

    # Baca kembali tabel secara horizontal.
    plaintext = []
    for row in range(rows):
        for column in range(columns):
            if row < len(columns_data[column]):
                plaintext.append(columns_data[column][row])

    return "".join(plaintext)


class ColumnarTranspositionApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Columnar Transposition Cipher")
        self.geometry("760x610")
        self.minsize(650, 540)

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
            text="Columnar Transposition Cipher",
            style="Title.TLabel"
        ).pack(anchor="w")

        ttk.Label(
            header,
            text="Enkripsi dan dekripsi dengan teknik transposisi kolom",
            style="Subtitle.TLabel"
        ).pack(anchor="w", pady=(4, 0))

        key_frame = ttk.Frame(self)
        key_frame.pack(fill="x", pady=(0, 12))

        ttk.Label(
            key_frame,
            text="Kunci:",
            style="Section.TLabel"
        ).pack(side="left")

        self.key_var = tk.StringVar(value="TOMBAK")

        self.key_entry = ttk.Entry(
            key_frame,
            textvariable=self.key_var,
            width=20
        )
        self.key_entry.pack(side="left", padx=(10, 10))

        ttk.Label(
            key_frame,
            text="Contoh: TOMBAK (huruf kunci harus berbeda)"
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
                "Spasi dihapus saat proses transposisi, sesuai contoh pada materi."
            ),
            style="Subtitle.TLabel"
        ).pack(anchor="w", pady=(8, 0))

    def get_input_and_key(self):
        text = self.input_text.get("1.0", "end-1c")
        key = validate_key(self.key_var.get())

        if not text:
            raise ValueError("Masukkan teks terlebih dahulu.")

        return text, key

    def show_result(self, result):
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", result)

    def encrypt(self):
        try:
            text, key = self.get_input_and_key()
            result = encrypt(text, key)
            self.show_result(result)
        except ValueError as error:
            messagebox.showerror("Input Tidak Valid", str(error))

    def decrypt(self):
        try:
            text, key = self.get_input_and_key()
            result = decrypt(text, key)
            self.show_result(result)
        except ValueError as error:
            messagebox.showerror("Input Tidak Valid", str(error))

    def clear(self):
        self.input_text.delete("1.0", "end")
        self.output_text.delete("1.0", "end")
        self.key_var.set("TOMBAK")
        self.input_text.focus_set()


if __name__ == "__main__":
    app = ColumnarTranspositionApp()
    app.mainloop()
