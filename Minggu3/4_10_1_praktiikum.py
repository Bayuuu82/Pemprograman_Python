print(('DATA KECEPATAN MOBIL').center(100))
print('{:^100}'.format('-'*60))

kecepatan=int(input(('Kecepatan rata-rata(km/jam):').center(70)))
waktu=int(input    (('Waktu Tempuh(Jam)          :').center(70)))
jar = kecepatan * waktu
print((f'Jarak tempuh               :      {kecepatan} * {waktu} = {jar}').center(85))
print('{:^100}'.format('-'*60))
