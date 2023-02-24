import random

lista = []
for _ in range(1,51):
    lista.append(_)

def randomquestion(ls):
    rq = random.choice(ls)
    ls.remove(rq)
    return  rq

q1 = randomquestion(lista)
q2 = randomquestion(lista)
q3 = randomquestion(lista)

print(q1,q2,q3)
print(lista)