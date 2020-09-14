
# perulangan di python menggunakan keyword for

list = ['hello','world', 'apa', "kabar", 123, False] # perulangan list 
for i in list:
    print(i)
 
print("---" * 20)

tuple = ('hello', 'world', 'how', 'are you', 123, True) # perulangan tuple
for j in tuple:
    print(j)

print("---" * 20)

testing = {'hallo', 'bro', 'keep', 'coding'} # perulangan set
for z in testing:
    print(z)

print("---" * 20)

dict = {'nama':'dani', 'umur':32, 'alamat':'kopang'} # perulangan dictionary
for d in dict.items():
    print(d)

print("---" * 20)

numbers = [7, 5, 9, 8, 4, 2, 6, 4, 1]

# variablel untuk menyimpan jumlah
sum = 0

# iterasi untuk menjumlahkan total angka pada list 
for each in numbers:
    sum +=  each
print("Jumlah semuanya:", sum)