# kwargs singkatan dari keyword arguments

def record(**identitas):
    for i in identitas.items():
        print(i)

record(nama='windi', umur=17, alamat="jakarta", no_hp='0740192741092') # hanya dengan menambah ** pada parameter di atas kita bisa mengirim banyak keyword argument ke fungsi
print('-'*30)
record(nama='rilda', umur=18, alamat="bandung", no_hp='0934709137402')

