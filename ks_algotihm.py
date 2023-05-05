import time
# çalışma süresini bulmak için başlatık
start_time = time.time()

with open('ks_10000_0', 'r') as f:
    # İlk satırı okuma ve atlama
    line = f.readline()
    # diğer  satırları oku
    lines = f.readlines()

# okunan verilerin eklenmesi için boş liste
matrix = []
# okunan veriler boş listeye eklenmesi
for i in lines:
    if i.strip():  # boş bir satır değilse devam et
        x, y = map(int, i.strip().split())
        matrix.append([x, y])


# atlanan ilk satırın ilk sütunu matrixin uzunluğu ve
# ikinci sütunu maximum taşınan ağırlığı değişkene atıyoruz
matrix_len, max_weight = line.split()

# kullanım kolaylığından dolayı değişkenleri int e çevirdik
matrix_len = int(matrix_len)
max_weight = int(max_weight)

# 1 ağırlıktaki eşyaların değerini boş listeye ekledik
a = []

for i in range(matrix_len):
    x = matrix[i][0]/matrix[i][1]
    a.append(x)

# oluşturduğumuz a listesini 3. sütun olarak matrixe ekledik
# indexleri de ekledik ki tekrar bu matrix sırasına dönelim
for i in range(matrix_len):
    matrix[i].append(a[i])
    matrix[i].append(i)

# matrixi bulduğum birim değere göre büyükten küçüğe sıraladık
matrix = sorted(matrix, key=lambda x: x[2], reverse=True)

top = 0
result = 0

for i in range(matrix_len):
    if top+matrix[i][1] < max_weight:
        top += matrix[i][1]
        matrix[i][1] = 1
        result += matrix[i][0]

    else:
        matrix[i][1] = 0

matrix = sorted(matrix, key=lambda x: x[3])
result2 = ' '.join([str(row[1]) for row in matrix])

print(result)
print(result2)

print("--- %s saniye ---" % (time.time() - start_time))
