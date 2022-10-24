# 6.6 PRAKTIKUM (hanya bisa kerjakan 2-7)
# bayu fajrin 19.01.013.077 

# 2. buatlah program yang menampilkan deret geometri dengan masukan nilai awal,
#    banyaknya suku, dan rasio antara satu suku dan suku sebelumnya
#    rumus suku ke-n deret geometri adalah Un  = arn-1
a = float(input('Nilai Awal : '))
un = int(input('Suku akhir : '))
u = int(input('banyaknya suku :'))
r = float(input("Rasio : "))
for n in range(u, un+1):
    suku = a*(r**(n-1))
    print(suku)



# 3. buatlah program yang menginput sejumlah N(input) bilangan, kemudian keluaranya
#    berupa nilai total dan rata-rata dari bilangan yang telah di input tersebut
data_n = input('\nMasukan nilai N, pisahkan dengan tanda koma. contoh: 1,2,3,dst : ')
list_angka = data_n.split(',')
daftar_baru = [int(x) for x in list_angka]
jumlah = 0
for angka in daftar_baru:
    jumlah += angka
rata_rata = jumlah / len(daftar_baru)
print('\nJumlah  total: {}'.format(jumlah))
print(f'Nilai rata-rata: {int(rata_rata)}')



# 4. buatlah program menghitung X^y dengan x bilangan real dan y bilangan bulat positif
print(('\nAPLIKASI PERHITUNGAN BERPANGKAT DENGAN POSISI X^y'))
x = int(input('Masukan nilai x : '))
y = int(input('Masukan nilai y : '))
hasil = x ** y
print(f'\nHasil = {hasil}')



# 5. buatlah program menghitung N! dengan N sebagai masukan
#       contoh 5! = 5 * 4 * 3 * 2 * 1 maka 5! = 120
x = int(input('Masukkan nilai n: '))
faktorial = 1
for i in range(1, x + 1):
  faktorial *= i
print(f'{x}! = {faktorial}')



# 6. Buatlah program tebak angka dimana pengguna menginput suatu bilangan integer antara 0-10 yang telah diacak komputer. Jika
#    angka yang ditebak lebih besar dari angka sesungguhnya, maka ditampilkan keterangan bahwa angka nilacak lebih besar...
import random
nilacak = random.randint(0, 10)
print('Coba tebak angka saya, dari 0-10')
print('=' *50)
while True:
  tebakan = int(input('\nMasukkan angka: '))
  if tebakan == nilacak:
    print('Tebakanmu benar!')
    break # berhenti paksa
  else:
    print(
      'Angka tebakan lebih',
      'kecil' if tebakan < nilacak else 'besar')



# 7. buatlah program untuk menampilkan dan menjumlahkan semua bilangan antara nilai X dan Y 
print('Masukan angka X dan Y untuk menghitung jumlah angka dari X sampai Y')
print('=' *50)
x= int(input('Masukan nilai X   : '))
y= int(input('Masukan nilai Y   : '))
print('Deret    : ')
for antara in range(x,y+1):
    print(antara, end=' ')
jumlah= sum(range(x,y+1))
print(f'\nJumlah : {jumlah}')


