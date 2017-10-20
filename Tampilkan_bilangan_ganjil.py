#!/usr/local/bin/python3
print ("Tampilkan NIM Ganjil For")

nim=int(input("Masukkan NIM Anda Tanpa Di Dahului Dengan Angka 0: "))
loop=int(input("Masukkan Range Yang Diinginkan: "))
for i in range (nim,nim+loop):
	if (i%2)==1:
		print (i)
