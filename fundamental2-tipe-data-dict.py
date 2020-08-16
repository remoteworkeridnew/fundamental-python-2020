"""
Tipe data dictionary sekedar menghubunkan antara KEY an VALUE
KVP = Key Value Pair
dictionary = kamus
"""

kamus_ind_eng = {'anak': 'son', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}

print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])

print('\ndata ini dikirimkan oleh server gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2020-06-10',
    'driver_list': [{'nama': 'eko', 'jarak': 10},
                    {'nama': 'dwi', 'jarak': 30},
                    {'nama': 'tri', 'jarak': 100},
                    {'nama': 'catur', 'jarak': 1000}
    ]
}
print(data_dari_server_gojek)
print(f"\nDriver sekitar sini{data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #4 {data_dari_server_gojek['driver_list'][3]}")
print(f"Driver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")
