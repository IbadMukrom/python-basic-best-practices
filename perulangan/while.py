

# perulangan dengan while

i = 0
while i < 10:
    print(i)
    i+=1
print("==="*20)

i = 0
while i < 10:
    i = i + 1
    if i == 8:
        break  # break di gunakan untuk mengentikan perulangan di tengah program walaupun kondisi masih tetap True
    print(i)

print("==="*20)

i = 0 
while i < 10:
    i += 1
    if i == 8: # continue di gunakan untuk menghentikan perulangan, kemudian melanjutkan ke perulangan selanjutnya
        continue
    print(i)