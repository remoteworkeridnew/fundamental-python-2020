# KONTRUKSI DASAR PYTHON
# SEQUENTIAL: Eksekusi berurutan
print('hello world!')
print('by Eko')
print('tanggal 10 Juni 2020')
print("-" * 10)

# Percabangan: Eksekusi terpilih
ingin_cepat = False
if ingin_cepat:
    print('Jalan lurus aja ya!')
else:
    print('Jalan lain')

# PERULANGAN
jumlah_anak = 4

for index_anak in range(1, jumlah_anak+1): #jumlah perulangan= 5 -1 = 4
        print(f'Halo anak #{index_anak}')
