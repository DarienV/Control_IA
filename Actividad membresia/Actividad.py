import csv

rangos = []
min = []
max = []

with open("C:\\Users\\didie\\Documents\\BUAP_Prim23\\Control_IA\\Actividad membresia\\Edades.csv", "r") as f:
    data = f.readlines()

for line in data:
    rangos.append(line.split(','))
del rangos[0]

for i in rangos:
    i[2] = i[2].strip('\n')
    min.append(i[1])
    max.append(i[2])


maxval = max[0]    
for x in max: 
    if x > maxval:
        maxval = x
minval = min[0]
for x in min: 
    if x < minval:
        minval = x
        
lista = []
for _ in range(int(minval), int(maxval)+1):
    lista.append(_)

membership = []
total = []
for _ in lista:
    count = 0
    for i in range(0,len(rangos)):
        if _ in range(int(min[i]), int(max[i])+1):
            count += 1
    total.append(count)

maxval = total[0]    
for x in total: 
    if x > maxval:
        maxval = x

for _ in range(0, len(lista)):
    prom = total[_]/maxval
    membership.append(prom)
    
    
outfile = open("Membership.csv","w")
outfile.write("Edad,Frecuencia,Grado de pertenencia")
outfile.write("\n")

for _ in range(0,len(lista)):
    newrow = ""
    newrow = ("{},{},{}".format(lista[_],total[_],membership[_]))
    outfile.write(newrow)
    outfile.write("\n")
outfile.close()

age = 27
numper = []
degree = []
freq = []  
count = 0

for i in range(0,len(rangos)):
    if age in range(int(min[i]), int(max[i])+1):
        count += 1
    if (i%10 == 0) and (i > 0):
        numper.append(i)
        degree.append(count)
        freq.append(count/i)



outfile = open("Membership2.csv","w")
outfile.write("# de personas,Membership degree,Membership frequency")
outfile.write("\n")

for _ in range(0,len(numper)):
    newrow = ""
    newrow = ("{},{},{}".format(numper[_],degree[_],freq[_]))
    outfile.write(newrow)
    outfile.write("\n")
outfile.close()
