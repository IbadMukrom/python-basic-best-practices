# dictionary adalah tipe data yang anggotanya terdiri dari kuncy(key) dan nilai(value)

dct = {'name:':'bonjovi',
        'age:':20,
        'address:': 'america'
    }
print(dct)

for i in dct.keys(): # menggunakan perulangan untuk mengakses key saja
    print(i)

for j in dct.values(): # menggunakan perulangan untuk mengakses value saja
    print(j)

for k in dct.items(): # menggunakan perulangan untuk mengakses keduanya
    print(k)