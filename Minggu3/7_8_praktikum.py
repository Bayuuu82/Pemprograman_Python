print('=' *35)
mahasiswa = {}
for i in range(5):
    no = i+1
    nama = input('\nMasukkan Nama : ')
    nilai = int(input('Masukkan Nilai : '))
    mahasiswa[no] = nama, nilai
print('-' *35)
print ("{:<8} {:<15} {:<10}".format('No','Nama','Nilai'))
print('-' *35)
for n, d in mahasiswa.items():
    nama, nilai = d
    print ("{:<8} {:<15} {:<10}".format(n, nama, nilai))
print('-' *35)

#   belum fix di nilai rata ratanya
# for key, value1, value2 in mahasiswa.items():
#     print(f'Jumlah mahasiswa : {i+1}')
#     rata_rata = sum(value2) / len(mahasiswa)
#     print (rata_rata)
