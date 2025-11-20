- Menampilkan daftar kontak awal
- Menambahkan kontak baru
- Mengubah nomor kontak
- Menampilkan semua nama, nomor, dan daftar lengkap kontak
- Menghapus kontak

1. Inisialisasi Kontak
   - Membuat dictionary `daftar_kontak` dengan nama dan nomor telepon.
   
2. Menampilkan Daftar Kontak Awal
   - Menampilkan seluruh kontak yang ada pada dictionary.

3. Mengakses Nomor Kontak Tertentu
   - Contoh: Menampilkan nomor telepon Ari.

4. Menambahkan Kontak Baru
   - Menambahkan pasangan key-value baru ke dictionary.

5. Mengubah Nomor Kontak
   - Memperbarui nomor telepon untuk key yang sudah ada.

6. Menampilkan Semua Nama dan Nomor
   - Menggunakan `keys()`, `values()`, dan `items()` untuk menampilkan data.

7. Menghapus Kontak
   - Menghapus kontak tertentu menggunakan `del`

1. Pastikan Python terinstall (versi 3.x direkomendasikan)
2. Simpan script Python ini sebagai `daftar_kontak.py`
3. Jalankan menggunakan terminal:
   ```bash
   python daftar_kontak.py

## Flowchart Program Manajemen Nilai Mahasiswa

```
         ┌─────────────────────┐
         │   Mulai Program     │
         └─────────┬──────────┘
                   │
                   ▼
       ┌─────────────────────┐
       │  Inisialisasi daftar│
       │  kontak (dictionary)│
       └─────────┬──────────┘
                   │
                   ▼
       ┌─────────────────────┐
       │ Tampilkan daftar    │
       │ kontak awal         │
       └─────────┬──────────┘
                   │
                   ▼
       ┌─────────────────────┐
       │ Tampilkan nomor Ari │
       └─────────┬──────────┘
                   │
                   ▼
       ┌─────────────────────┐
       │ Tambahkan Riko ke   │
       │ daftar kontak       │
       └─────────┬──────────┘
                   │
                   ▼
       ┌─────────────────────┐
       │ Ubah nomor Dina     │
       └─────────┬──────────┘
                   │
                   ▼
       ┌─────────────────────┐
       │ Tampilkan semua     │
       │ nama (keys)         │
       └─────────┬──────────┘
                   │
                   ▼
       ┌─────────────────────┐
       │ Tampilkan semua     │
       │ nomor (values)      │
       └─────────┬──────────┘
                   │
                   ▼
       ┌─────────────────────┐
       │ Tampilkan daftar    │
       │ nama dan nomor      │
       │ (items)             │
       └─────────┬──────────┘
                   │
                   ▼
       ┌─────────────────────┐
       │ Hapus Dina dari     │
       │ daftar kontak       │
       └─────────┬──────────┘
                   │
                   ▼
         ┌─────────────────┐
         │  Tampilkan daftar│
         │  kontak akhir    │
         └─────────┬───────┘
                   │
                   ▼
              ┌─────────┐
              │   Selesai│
              └─────────┘







1. Tentukan Struktur Data
   Gunakan dictionary untuk menyimpan data mahasiswa:
   Key utama: NIM
   Value: dictionary dengan nama dan nilai

2. Buat Fungsi Menghitung Nilai Akhir
3. Buat Fungsi Tambah Data
4. Buat Fungsi Tampilkan Data
   Langkah-langkah:
   Periksa apakah dictionary kosong
   Jika ada data, tampilkan semua NIM, Nama, Nilai Tugas, UTS, UAS, dan Nilai Akhir dalam tabel
   Ini adalah bagian Read dalam CRUD
   Buat Fungsi Hapus Data
5. Buat Fungsi Cari Data
   Langkah-langkah:
   Minta input NIM yang dicari
   Periksa apakah NIM ada
   Jika ada, tampilkan detail data mahasiswa
   Jika tidak ada, beri pesan "tidak ditemukan"
6. Buat Menu Utama
   Langkah-langkah:
   Buat loop while True
   Tampilkan pilihan menu: Lihat, Tambah, Ubah, Hapus, Cari, Keluar
   Jalankan fungsi sesuai pilihan pengguna
   Jika memilih Keluar, hentikan loop
Flowchart Program Daftar Kontak

```
```
+-------------------------+
|          Mulai          |
+-------------------------+
            |
            v
+-------------------------+
|   Tampilkan Menu Utama  |
| [L/T/U/H/C/K]           |
+-------------------------+
            |
            v
+-------------------------+
|       Pilih Opsi        |
+-------------------------+
    |     |     |     |     |     |
    L     T     U     H     C     K
    |     |     |     |     |     |
    v     v     v     v     v     v
+--------+--------+--------+--------+--------+ 
| Lihat  | Tambah | Ubah   | Hapus | Cari   | Keluar
| Data   | Data   | Data   | Data  | Data   | Program
+--------+--------+--------+--------+--------+
    |       |       |       |       |
    v       v       v       v       v
+---------------------------------------------+
| Setelah operasi selesai → kembali ke menu  |
+---------------------------------------------+
            |
            v
+-------------------------+
|         Selesai         |
+-------------------------+
```

