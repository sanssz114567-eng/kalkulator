# Fungsi untuk penjumlahan
def tambah(x, y):
    return x + y

# Fungsi untuk pengurangan
def kurang(x, y):
    return x - y

# Fungsi untuk perkalian
def kali(x, y):
    return x * y

# Fungsi untuk pembagian
def bagi(x, y):
    if y == 0:
        return "Error! Pembagian dengan nol tidak bisa."
    return x / y

# Menu utama
print("=== KALKULATOR SEDERHANA ===")
print("Pilih Operasi:")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (*)")
print("4. Pembagian (/)")

# Meminta input dari pengguna
pilihan = input("Masukkan pilihan (1/2/3/4): ")

# Memastikan input pilihan valid
if pilihan in ('1', '2', '3', '4'):
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if pilihan == '1':
        print(f"Hasil: {angka1} + {angka2} = {tambah(angka1, angka2)}")
    elif pilihan == '2':
        print(f"Hasil: {angka1} - {angka2} = {kurang(angka1, angka2)}")
    elif pilihan == '3':
        print(f"Hasil: {angka1} * {angka2} = {kali(angka1, angka2)}")
    elif pilihan == '4':
        print(f"Hasil: {angka1} / {angka2} = {bagi(angka1, angka2)}")
else:
    print("Pilihan tidak valid!")