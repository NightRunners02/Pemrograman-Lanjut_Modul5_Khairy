
def baca_data(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return lines
        
    except FileNotFoundError:
        print("File tidak ditemukan. Membuat file baru...")
        return []


def tulis_data(file_path, data):
    with open(file_path, 'w') as file:
        file.writelines(data)


def hapus_duplikat(data):
    unique_data = []
    seen = set()
    for line in data:
        if line not in seen:
            unique_data.append(line)
            seen.add(line)
    return unique_data


def main():
    file_path = 'data_mahasiswa.txt'

    
    data = baca_data(file_path)

    
    while True:
        nama = input("Masukkan Nama: ")
        if not nama:
            break
        nim = input("Masukkan NIM: ")
        semester = input("Masukkan Semester: ")
        data.append(f"{nama} {nim} {semester}\n")

    
    data = hapus_duplikat(data)

   
    tulis_data(file_path, data)

    print("Data telah disimpan dan duplikat dihapus.")

if __name__ == "__main__":
    main()

