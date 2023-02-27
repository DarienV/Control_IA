import random
import csv

def randomquestion(ls):
    rq = random.choice(ls)
    ls.remove(rq)
    return  rq

correct_answers = {
    1:"a",   2:"a",  3:"d",  4:"c",  5:"c",  6:"b",  7:"b",  8:"d",  9:"d", 10:"d",
    11:"c", 12:"b", 13:"d", 14:"d", 15:"a", 16:"a", 17:"c", 18:"d", 19:"c", 20:"a",
    21:"a", 22:"c", 23:"c", 24:"a", 25:"b", 26:"a", 27:"a", 28:"a", 29:"d", 30:"b",
    31:"b", 32:"b", 33:"a", 34:"c", 35:"b", 36:"a", 37:"d", 38:"a", 39:"a", 40:"a",
    41:"b", 42:"b", 43:"b", 44:"a", 45:"b", 46:"c", 47:"b", 48:"a", 49:"a", 50:"d"
    }

lista = []
for _ in range(1,51):
    lista.append(_)

with open("Preguntas.txt", "r", encoding="utf8") as q:
    questions = q.readlines()

with open("Respuestas.csv", "r", encoding="utf8") as a:
    answers = a.readlines()

score = 0

for i in range(1,4):
    q = randomquestion(lista)
    print(questions[q])
    aux = answers[q].split(",")
    for j in aux:
        print(j)
    
    user_answer = input("La respuesta es: ")
    if user_answer.lower() == correct_answers[q+1]:
        print("Correcto!\n")
        score += 1
    else:
        print("Incorrecto :(\n")

print("\n\nObtuvo " + str(score) + "/3 de calificacion.")