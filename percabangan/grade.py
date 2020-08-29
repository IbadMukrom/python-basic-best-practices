#contoh program percabangan grade nilai

nilai = int(input('inputkan nilai anda: '))

if nilai > 100:
    print('nilai anda di luar batas bro')
elif nilai >= 90:
    print('grade anda A')
elif nilai >=80:
    print('grade anda B')
elif nilai >=70:
    print('grade anda C')
elif nilai >= 60:
    print('grade anda D')
else:
    print('anda tidak lulus')
