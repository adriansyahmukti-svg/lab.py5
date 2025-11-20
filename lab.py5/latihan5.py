daftar_kontak = {
    'Ari': '081267888',
    'Dina': '087677776'
}
print("--- Daftar Kontak Awal ---")
print(daftar_kontak)
print("-" * 30)

print("Nomor Telepon Ari:", daftar_kontak['Ari'])
print("-" * 30)


daftar_kontak['Riko'] = '087654544'
print("Kontak setelah Riko ditambahkan:")
print(daftar_kontak)
print("-" * 30)



daftar_kontak['Dina'] = '088999776'
print("Kontak setelah Dina diubah:")
print(daftar_kontak)
print("-" * 30)


print("Semua Nama (Keys):")
for nama in daftar_kontak.keys():
    print(f"- {nama}")
print("-" * 30)


print("Semua Nomor (Values):")
for nomor in daftar_kontak.values():
    print(f"- {nomor}")
print("-" * 30)

print("Daftar Nama dan Nomornya (Items):")
for nama, nomor in daftar_kontak.items():
    print(f"Nama: {nama} | Nomor: {nomor}")
print("-" * 30)

del daftar_kontak['Dina']
print("Kontak setelah Dina dihapus:")
print(daftar_kontak)
print("-" * 30)