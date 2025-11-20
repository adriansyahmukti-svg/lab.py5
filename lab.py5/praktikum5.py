import os
DATA_NILAI = {
    '23455': {
        'Nama': 'mukti adriansyah', 
        'Tugas': 99, 
        'UTS': 68, 
        'UAS': 88, 
        'Akhir': 84.30 
    },
    '23456': {
        'Nama': 'Budi', 
        'Tugas': 70, 
        'UTS': 80, 
        'UAS': 75, 
        'Akhir': 75.25
    },
    '23457': {
        'Nama': 'Cindy', 
        'Tugas': 85, 
        'UTS': 90, 
        'UAS': 95, 
        'Akhir': 90.50
    }
}

def hitung_akhir(t, u, a):
    """Menghitung Nilai Akhir (30% Tugas, 35% UTS, 35% UAS)"""
    return round((t * 0.30) + (u * 0.35) + (a * 0.35), 2)

def tambah_data():
    """T (Tambah Data) - Tetap berfungsi jika ingin menambah data lain"""
    print("\n--- TAMBAH DATA ---")
    nim = input("NIM: ").strip()
    if nim in DATA_NILAI:
        print(f"ERROR: NIM {nim} sudah ada.")
        return
    
    try:
        nama = input("Nama: ").strip()
        tugas = int(input("Nilai Tugas (30%): "))
        uts = int(input("Nilai UTS (35%): "))
        uas = int(input("Nilai UAS (35%): "))
        
        akhir = hitung_akhir(tugas, uts, uas)
        
        DATA_NILAI[nim] = {
            'Nama': nama,
            'Tugas': tugas,
            'UTS': uts,
            'UAS': uas,
            'Akhir': akhir
        }
        print(f"\n Data {nama} berhasil ditambahkan. Nilai Akhir: {akhir}")
    except ValueError:
        print("ERROR: Input nilai harus angka.")

def tampilkan_data():
    """L (Lihat/Tampilkan Data)"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" + "="*70)
    print("DAFTAR NILAI MAHASISWA".center(70))
    print("="*70)

    if not DATA_NILAI:
        print("TIDAK ADA DATA".center(70))
        return

    print("| NO | NIM | NAMA | TUGAS | UTS | UAS | AKHIR |")
    print("-" * 70)
    
    no = 1
    for nim, data in DATA_NILAI.items():
        print(f"| {no:<2} | {nim:<3} | {data['Nama']:<12} | {data['Tugas']:<5} | {data['UTS']:<3} | {data['UAS']:<3} | {data['Akhir']:<5.2f} |")
        no += 1
    print("-" * 70)

def ubah_data():
    """U (Ubah Data)"""
    print("\n--- UBAH DATA ---")
    nim = input("NIM yang akan diubah: ").strip()
    if nim not in DATA_NILAI:
        print(f"ERROR: NIM {nim} tidak ditemukan.")
        return

    data = DATA_NILAI[nim]
    print(f"Mengubah data {data['Nama']} (NIM: {nim})")
    print("Kosongkan input jika tidak ingin mengubah nilai.")
    
    try:
        data['Nama'] = input(f"Nama Baru (lama: {data['Nama']}): ") or data['Nama']
        
        t_str = input(f"Tugas Baru (lama: {data['Tugas']}): ").strip()
        u_str = input(f"UTS Baru (lama: {data['UTS']}): ").strip()
        a_str = input(f"UAS Baru (lama: {data['UAS']}): ").strip()

        if t_str: data['Tugas'] = int(t_str)
        if u_str: data['UTS'] = int(u_str)
        if a_str: data['UAS'] = int(a_str)

        data['Akhir'] = hitung_akhir(data['Tugas'], data['UTS'], data['UAS'])
        print(f"\n Data NIM {nim} berhasil diubah. Akhir Baru: {data['Akhir']}")
        
    except ValueError:
        print("ERROR: Input nilai harus angka.")

def hapus_data():
    """H (Hapus Data)"""
    print("\n--- HAPUS DATA ---")
    nim = input("NIM yang akan dihapus: ").strip()
    
    if nim in DATA_NILAI:
        nama = DATA_NILAI[nim]['Nama']
        del DATA_NILAI[nim]
        print(f"\n Data {nama} (NIM: {nim}) berhasil dihapus.")
    else:
        print(f"ERROR: NIM {nim} tidak ditemukan.")

def cari_data():
    """C (Cari Data)"""
    print("\n--- CARI DATA ---")
    nim = input("Masukkan NIM yang dicari: ").strip()
    
    if nim in DATA_NILAI:
        data = DATA_NILAI[nim]
        print("\n--- HASIL PENCARIAN ---")
        print(f"NIM   : {nim}")
        print(f"Nama  : {data['Nama']}")
        print(f"Tugas : {data['Tugas']}")
        print(f"UTS   : {data['UTS']}")
        print(f"UAS   : {data['UAS']}")
        print(f"AKHIR : {data['Akhir']}")
    else:
        print(f" NIM {nim} tidak ditemukan.")


def menu_utama():
    """Loop utama program."""
    while True:
        print("\n" + "-"*40)
        pilihan = input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]: ").upper()
        
        if pilihan == 'L':
            tampilkan_data()
        elif pilihan == 'T':
            tambah_data()
        elif pilihan == 'U':
            ubah_data()
        elif pilihan == 'H':
            hapus_data()
        elif pilihan == 'C':
            cari_data()
        elif pilihan == 'K':
            print("\n👋 Program Selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu_utama()