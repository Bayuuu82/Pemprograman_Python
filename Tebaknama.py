import os
from random import choice
# masukan nama dalam variabel 
guest_nama = choice(['Septi', 'Bayu', 'Budi', 'Tono', 'Dika', 'Danu', 'Anto', 'Elga', 'Safi', 'Anto'])

print('Coba tebak nama siapa yang saya pilih')
print('Septi, Bayu, Budi, Tono, Dika, Danu, Anto, Elga, Safi, Anto')


# buat perulangannya 
while True:
    # player1 = int(input('\nPlayer 1 memilih:'))
    player2 = input('\nTebakan Player 2:')
    if player2 == guest_nama:
        print('Tebakan mu benar!!')
        break
    elif player2 != guest_nama:
        print('Tebakanmu salah!')
        break


batas_percobaan = 3

for percobaan in range(batas_percobaan):
    player2 = int(input(f'\n [sisa {batas_percobaan - 1} kali menebak] \nTebak lagi: '))
    if player2 == guest_nama:
        print('Tebakan mu benar!!')
        break
    else:
        print('Tebakanmu salah!')
else:
  print(f'\nSayang sekali, kamu sudah salah menebak sebanyak {batas_percobaan}x!')