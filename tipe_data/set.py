# set adalah tipe data yang bisa menampungn banyak jenis tipe data
# set bersifat immutable dan unordered ('tidak berurutan')
# set tidak mendukung data yang double/duplikat


myset = {'hello', 'world', 'python', 1000, 10.1 , True, 'hello' }

myset.update('java') #method add untuk menambah data
print(myset)

i = {1,2,3}
j = {4,5,6}
k = {7,7,8}
i.update(j,k) #method update untuk menggabungkan 2 set, atau lebih
print(i)

set1 = {1,2,3,14,23}
set2 = {1,2,3,14,21}
r = set2.difference(set1) #method difference untuk melihat perbedaan element dari 2 set atau lebih
print(r)









