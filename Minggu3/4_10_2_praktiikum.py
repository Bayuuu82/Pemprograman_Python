print(('PROGRAM MENGHITUNG PEMBELIAN').center(100))
print('{:^100}'.format('-'*60))

harga=int(input(('Harga Satuan     : Rp ').center(70)))
jum=int(input(('Jumlah Pembelian :   ').center(70)))

harbarang= harga * jum
hargadiskon= harbarang * (10/100)
hargatotal= harbarang - hargadiskon
print('{:^80}'.format(f'Diskon           : Rp.      {int(hargadiskon)} ').center(70))
print('{:^80}'.format(f'Harga Total      : Rp.      {int(hargatotal)}').center(70))
