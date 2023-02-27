import random

lista = []
for _ in range(1,51):
    lista.append(_)

def randomquestion(ls):
    rq = random.choice(ls)
    ls.remove(rq)
    return  rq

answers = {
    1:"a", 2:"a", 3:"", 4:"", 5:"", 6:"", 7:"", 8:"", 9:"", 10:"",
    11:"c", 12:"b", 13:"d", 14:"d", 15:"a", 16:"a", 17:"c", 18:"d", 19:"c", 20:"a",
    21:"a", 22:"c", 23:"c", 24:"a", 25:"b", 26:"a", 27:"", 28:"", 29:"", 30:"",
    31:"b", 32:"b", 33:"a", 34:"c", 35:"b", 36:"a", 37:"d", 38:"a", 39:"a", 40:"a",
    41:"b", 42:"b", 43:"b", 44:"a", 45:"b", 46:"c", 47:"b", 48:"a", 49:"a", 50:"d"
    }

for _ in range(1,4):
    q = randomquestion(lista)
    
