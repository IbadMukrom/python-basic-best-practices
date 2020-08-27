# tuple di python sedikit mirip dengan list, tuple bisa menyimpan banyak jenis tipe data
# perbedaan nya dengan list adalah tuple bersifat immutable (tidak bisa di rubah)

mytuple = ('hello ', 'world', 'python', 'world', 2000, True, 10.1)

x = mytuple.index('world') #method index untuk mengecek value tersebut berada di index ke berapa
print(x)

print(mytuple.count('world')) # method count untuk menghitung berapa 


