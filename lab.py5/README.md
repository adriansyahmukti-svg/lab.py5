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




1. Tentukan Struktur Data

Gunakan dictionary untuk menyimpan data mahasiswa:
Key utama: NIM
Value: dictionary dengan nama dan nilai

2. Buat Fungsi Menghitung Nilai Akhir
3. Buat Fungsi Tambah Data
Langkah-langkah:
Minta input NIM, Nama, Tugas, UTS, UAS
Periksa apakah NIM sudah ada
Hitung nilai akhir menggunakan fungsi sebelumnya
Simpan data ke dictionary
Ini adalah bagian Create dalam CRUD.
4. Buat Fungsi Tampilkan Data
Langkah-langkah:
Periksa apakah dictionary kosong
Jika ada data, tampilkan semua NIM, Nama, Nilai Tugas, UTS, UAS, dan Nilai Akhir dalam tabel
Ini adalah bagian Read dalam CRUD
Buat Fungsi Hapus Data

Langkah-langkah:
Minta input NIM yang ingin dihapus
Periksa apakah NIM ada
Hapus data dari dictionary
Ini adalah bagian Delete dalam CRUD.
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
## Flowchart Program Daftar Kontak

```## Flowchart Program Daftar Kontak

```
+-------------------------+
|          Mulai          |
+-------------------------+
            |
            v
+-------------------------+
|   Tampilkan Daftar      |
|     Kontak Awal         |
+-------------------------+
            |
            v
+-------------------------+
| Tampilkan Nomor Ari     |
+-------------------------+
            |
            v
+-------------------------+
| Tambahkan Kontak Riko   |
+-------------------------+
            |
            v
+-------------------------+
| Ubah Nomor Dina         |
+-------------------------+
            |
            v
+-------------------------+
| Tampilkan Semua Nama    |
|       (Keys)            |
+-------------------------+
            |
            v
+-------------------------+
| Tampilkan Semua Nomor   |
|       (Values)          |
+-------------------------+
            |
            v
+-------------------------+
| Tampilkan Nama & Nomor  |
|       (Items)           |
+-------------------------+
            |
            v
+-------------------------+
| Hapus Kontak Dina       |
+-------------------------+
            |
            v
+-------------------------+
| Tampilkan Kontak Akhir  |
+-------------------------+
            |
            v
+-------------------------+
|          Selesai        |
+-------------------------+
```

|

