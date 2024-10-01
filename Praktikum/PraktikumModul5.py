import os

def baca_data(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        return []

def tulis_data(file_path, data):
    with open(file_path, 'w') as file:
        file.writelines(data)

def tambah_data():
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    matkul = input("Masukkan Mata Kuliah: ")
    semester = input("Masukkan Semester: ")
    return f"{nama} {nim} {matkul} {semester}\n"

def tampilkan_data(data):
    if not data:
        print("Tidak ada data.")
    else:
        for i, line in enumerate(data, 1):
            print(f"Menampilkan Data ke-{i}:")
            print(line)

def update_data(data, nim):
    for i, line in enumerate(data):
        if nim in line:
            nama_baru = input("Masukkan Nama Baru: ")
            nim_baru = input("Masukkan NIM Baru: ")
            matkul_baru = input("Masukkan Matkul Baru: ")
            semester_baru = input("Masukkan Semester Baru: ")
            data[i] = f"{nama_baru} {nim_baru} {matkul_baru} {semester_baru}\n"
            print("Data berhasil diupdate.")
            return data
    print("Data tidak ditemukan.")
    return data

def delete_data(data, nim):
    for i, line in enumerate(data):
        if nim in line:
            del data[i]
            print("Data berhasil didelete.")
            return data
    print("Data tidak ditemukan.")
    return data

def search_data(data, nim):
    for line in data:
        if nim in line:
            print(line)

def main():
    file_path = 'data_mahasiswa.txt'

    while True:
        print("=====APLIKASI KELOLA DATA MAHASISWA=====")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Search Data")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        data = baca_data(file_path)

        if pilihan == '1':
            data.append(tambah_data())
            tulis_data(file_path, data)
            print("Data mahasiswa berhasil ditambahkan.")
        elif pilihan == '2':
            tampilkan_data(data)
        elif pilihan == '3':
            nim_update = input("Masukkan NIM dari data yang ingin diubah: ")
            data = update_data(data, nim_update)
            tulis_data(file_path, data)
        elif pilihan == '4':
         nim_delete = input("Masukkan NIM data yang ingin dihapus: ")
         if nim_delete:
             data = delete_data(data, nim_delete)
             tulis_data(file_path, data)
         else:
              print("NIM tidak boleh kosong. Silakan masukkan NIM yang valid.")

        elif pilihan == '5':
            nim_search = input("Masukkan NIM dari data yang ingin dicari: ")
            search_data(data, nim_search)
        elif pilihan == '6':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()