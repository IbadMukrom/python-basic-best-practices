# list adalah tipe data sequence (berurutan) yang bisa menampung banyak tipe data sekaligus
# list bersifat mutable (bisa dirubah nilainya)  

mylist = ['laptop', 'hp', 'tv', 1000, 60.78]
print (mylist)


mylist[0] = ('laptop gaming') #mengubah value index ke 0
mylist[3] = (10) #mengubah value index 4 dengan nilai 10
print(f'nilai setelah di rubah {mylist}')


mylist.append(100000) #method untuk menambahkan nilai baru di akhir index
print(f'nilai setelah di rubah {mylist}')

mylist.pop(0) # method untuk menghapus nilai berdasarkan index
print(f'nilai setelah di rubah {mylist}')

mylist.insert(0, 'dani')# menambah value berdasarkan index yang kita tentukan
print(f'nilai setelah di rubah {mylist}')

print('hp' in mylist) #cek apakah value tersebut ada pada list tersebut









