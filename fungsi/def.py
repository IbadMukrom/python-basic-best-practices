# fungsi di python menggunakan keyword def

def kalimat():
    print('hallo saya adalah puisi')

kalimat() # pemanggilan fungsi


def penjumlahan(angka_pertama, angka_kedua): #fungsi dengan parameter
    hasil = angka_pertama + angka_kedua
    print(f'hasilnya adalah {hasil}')

penjumlahan(10,20) #pemanggilan fungsi



def perkalian(f1, f2):
    hasil = f1 * f2
    print(f'hasilnya adalah {hasil}')
    return hasil # return untuk mengembalikan nilai dari fungs


ini_return = perkalian(5,10) # sehingga kita bisa membuat objek/instance baru dari hasil return di atas


