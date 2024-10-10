"""

Nom i Cognoms: Denis Fernández Varariu
DNI: 47956998C
URL vídeo: https://drive.google.com/file/d/1m39Y0VKJj2LdmoF7L29yoLn9u7MeaXVg/view?usp=sharing




Casal d'estiu
Cal fer un gestor per organitzar les dades d'un casal d'estiu, 
tal i com s'indica a continuació.
Es farà servir aquest tipus de diccionaris:

Diccionari d'estudiant:
Conté un nom, l'edat, l'antiguitat que és un valor entre 0 i 10 inclossos, 
i una llista de jocs que li agraden.

La llista de jocs, ha de contenir entre 2 i 5 jocs de manera aleatòria entre els següents:
["Tennis", "Ping-Pong", "Indoor Hockey", "Football", "Chess", "Swimming", "Basketball", "Volleyball", "Handball"]

student0 = {
    'dni': '12345678A',
    'name' : 'Joan' ,  
    'age' :  25 ,  
    'antiquitey' : 0,
    "games": ["Tennis", "Ping-Pong", "Indoor Hockey"]
}

Diccionari d'estudiants:
Guarda les dades de diversos estudiants, 
identificats a partir d'un codi de 8 caràcters que:

- Tres primers números són aleatòris entre 0 i 9 inclosos
- Treslletres aleatòries entre A i Z incloses (sense ñ)
- Un guió
- Dos números que és l'any de naixement de l'estudiant

students = {
    '534LTH-25': student0
}

"""
import random
import os
import platform

def clear_screen():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')
#Prompt
prompt = []

def promptAfegir(text):
    global prompt
    prompt.append(text)
    if len(prompt) >= 4:
        prompt.pop(0)

def promptEsborrar():
    global prompt
    for cnt in range(0, len(prompt)):
        promptAfegir("")

def promptDibuixar():
    global prompt
    for cnt  in range(0, len(prompt)):
        print(prompt[cnt])

"""
Exercici 0

Fes una funció addStudents(number) que crei afegeixi 'number' estudiants al diccionari 'students'

És a dir, si number és 5, crea 5 estudiants amb dades aleatòries.
És a dir, si number és 8, crea 8 estudiants amb dades aleatòries.

Afegeix els nous estudiants al diccionari, i retorna la llista amb els codis dels estudiants creats.
La funció escriu al prompt: "(createDatabase) 8 students added"

Et caldrà fer les següents funcions:
createCode() que retorna un codi aleatori
createName() que retorna un nom aleatori entre 10 noms
createAge() que retorna una edat aleatoria entre 5 i 15
createAntiquitey() que retorna una antiguitat aleatoria entre 0 i 10
createGames() que retorna una llista de jocs aleatoria entre 2 i 5 jocs

"""

# Fes aquí el codi de l'exercici 0

students = {

}

def createDNI():
    array_lletres = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
    primer_num = random.randint(0,5)
    numero_darrers = ""
    for cnt in range(0,7):
        num = random.randint(0, 9)
        numero_darrers = numero_darrers + str(num)
    numeros = str(primer_num) + str(numero_darrers)
    resto = int(numeros) % 23
    dni = numeros + "-" + array_lletres[resto]
    return dni

def createCode():
    lletres = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","W","X","Y","Z"]
    primernum = random.randint(0,9)
    segonnum = random.randint(0,9)
    tercernum = random.randint(0,9)
    primersnums = str(primernum) + str(segonnum) + str(tercernum) 
    primeralletra = random.choice(lletres)
    segonalletra = random.choice(lletres)
    terceralletra = random.choice(lletres)
    primereslletres = primeralletra + segonalletra + terceralletra
    anyun = random.randint(0,9)
    anydos = random.randint(0,9)
    anynaix = str(anyun) + str(anydos)
    code = primersnums + primereslletres + anynaix
    return code

def createName():
    noms = ["Denis","Adri","David","Marc","Pablo","Marta","Maria","Javier","Albert","Daniel"]
    nom = random.choice(noms)
    return nom

def createAge():
    edad = random.randint(5,15)
    return edad

def createAntiquitey():
    antiguetat = random.randint(0,10)
    return antiguetat

def createGames():
    jocs = []
    games = ["Tennis", "Ping-Pong", "Indoor Hockey", "Football", "Chess", "Swimming", "Basketball", "Volleyball", "Handball"]
    for i in games:
        game = random.choice(games)
        if game not in jocs:
            jocs.append(game)
    return jocs

def createStudent():  
    dic = {
        'dni': createDNI(),
        'name' : createName() ,  
        'age' :  createAge() ,  
        'antiquitey' : createAntiquitey(),
        "games": createGames()
}
    return dic


def addStudents(number):
    global students 
    ar = []
    for x in range(number):
        student = createStudent()
        ar.append(student)
        students[createCode()] = student
    promptAfegir(f"(createDatabase) {number} students added")
    return ar
    
    

"""
Exercici 1

Fes una funció que permeti buscar usuaris a partir d'un paràmetre. searchStudents(param, value)

La funció ha de retornar una llista amb els usuaris trobats. 
Si no troba cap usuari, retorna una llista buida.
La funció escriu al prompt: "(searchStudents) Found 1: ['534LTH-25']"

Per exemple:
La cerca no ha de tenir en compte les majúscules ni minúscules.
La funció escriu al prompt: "(searchStudents) Found 1: ['534LTH-25']" 
i després una linia amb les dades de cada estudiant trobat.

searchStudents(age, 25) ha de tornar ['534LTH-25']
searchStudents(games, "Tenis") ha de tornar ['534LTH-25']
searchStudents(games, "tenis") ha de tornar ['534LTH-25']

"""

# Fes aquí el codi de l'exercici 1

def searchStudents(param, value):
    usus = []
    for code, student in students.items():
        if value in student[param]:
            usus.append(code)
    promptAfegir(f"(searchStudents) Found {len(usus)}: {usus}")
    return usus

"""
Exercici 2

Fes una funció que permeti modificar usuaris a partir del seu codi. modifyStudents(code, param, value)

La funció ha de retornar si true o false segons si s'ha pogut modificar o no.
La funció escriu al prompt: "(modifyStudents) Student 534LTH-25 modified"
La funció escriu al prompt: "(modifyStudents) Student 534LTH-25 not found"

En el cas dels jocs, el value serà una llista.

"""

# Fes aquí el codi de l'exercici 2



def modifyStudents(code, param, value):
    global students
    if code in students:
        students[code][param] = value
        promptAfegir(f"(modifyStudents) Student {code} modified")
    else:
        promptAfegir(f"(modifyStudents) Student {code} not found")
    return
"""
Exercici 3

Fes una funció que permeti borrar usuaris a partir del seu codi. deleteStudents(list)

La funció sempre retorna la llista d'estudiants que s'han esborrat.
Si no ha esborrat cap estudiant retorna una llista buida.
La funció escriu al prompt: "(deleteStudents) Students deleted: ['534LTH-25']"

"""

# Fes aquí el codi de l'exercici 3


def deleteStudents(list):
    esborrats = []
    for cnt in range(0, len(list)):
        student = list[cnt]
        del students[student]
        esborrats.append(student)
    promptAfegir(f"(deleteStudents) Students deleted: {esborrats}")
    return esborrats

    
"""
Exercici 4

Fes el següent menú, i un prompt de 15 linies per gestionar les dades anteriors:

Et caldrà fer una funció 'listStudents(param)' que mostrarà al prompt una linia amb les dades de cada estudiant,
si són més de 15, el prompt simplement s'encarregarà de mostrar les 15 últimes. 
Haurà d'ordenar la llista segons el paràmetre, en cas de la llista segons el primer element de la llista

Options:                   Examples:
Add students to database - add 9 students
Search students          - search age 25
Modify students          - modify '534LTH-25' age 25
Delete students          - delete 534LTH-25,641ARC-20
List students            - list students by age
Exit                     - exit
Prompt 0
...
Prompt 14
What do you want to do?

A cada interacció es neteja la pantalla i es mostra el menú, el prompt i la pregunta.
"""

# Fes aquí el codi de l'exercici 4
def listStudents(param):
    llista = []
    for key in students.keys():
        llista.append(students[key])
    llista_ordenada = sorted(llista, key=lambda x: x[param])
    for cnt in range(0, len(llista_ordenada)):
        promptAfegir(llista_ordenada[cnt])

def menu():
    while True:
        print("""
Options:                   Examples:
Add students to database - add 9 students
Search students          - search age 25
Modify students          - modify '534LTH-25' age 25
Delete students          - delete 534LTH-25,641ARC-20
List students            - list students by age
Exit                     - exit
""")
        promptDibuixar()
        opcio = input("What do you want to do? ")
        comanda = opcio.split(" ")
        if comanda[0] == "add" and comanda[1].isalnum():
            addStudents(int(comanda[1]))
        elif comanda[0] == "search":
            if comanda[2].isalpha():
                searchStudents(comanda[1], comanda[2])
            else:
                searchStudents(comanda[1], int(comanda[2]))
        elif comanda[0] == "modify":
            code = comanda[1].replace("'", "")
            modifyStudents(code, comanda[2], comanda[3])
        elif comanda[0] == "delete":
            codes = comanda[1].split(",")
            deleteStudents(codes)
        elif comanda[0] == "list" and len(comanda) == 4:
            listStudents(comanda[3])
        elif comanda[0] == "exit":
            return
        clear_screen()
menu()
"""
Exercici Extra

Aquest exercici és voluntari, està fora de l'exàmen, però:

- T'ajuda amb la nota si has fallat alguna de les preguntes anteriors
- T'ajuda amb la nota de la UF si l'altre exàmen no et va anar massa bé
- T'ajuda a no anar al grup de repàs si ets un dels candidats
- T'ajuda a aprendre que un programador cobra per pensar.

En un organisme tenim bacteris B1 i cèl·lules CA.

Les quantitats no estan predeterminades, és a dir s'han de generar aleatòriament
entre 0 i 1000 per les cèl·lules CA i entre 0 i 20 per els bacteris B1.

Per aquest ordre passarà el següent:

- Cada segon, cada Bacteri B1 es menjarà 3 cèl·lules CA i es duplicarà. 
- Els Bacteris B1 que no disposin de 3 cèl·lules CA per menjar, es moriran sense menjar una sola cèl·lula. 
- Les que s'hagin menjat 3 cèl·lules CA, tal com hem mencionat abans, es duplicaran.
- Cada 3 Segons, cada 10 cèl·lules CA eliminaran una cèl·lula B1.
- Cada 4 segons, les cèl·lules CA es quadruplicaran
- Crea un algorisme que simuli l'evolució de les cèl·lules CA i els bacteris B1 cada segon, mostrant les taules d'exemple següents:

Exemple amb B1 = 15, CA = 1000

Starts with 15 bacteria and 1000 cells
Seconds       Bacteria B1       Cells CA
1             30                955
2             60                865
3             52                685
4             104               2116
5             208               1804
6             298               1180
7             596               286
8             190               4
9             2                 1
10            0                 1

Exemple amb B1 = 10, CA = 1200

Starts with 10 bacteria and 1200 cells
Seconds       Bacteria B1       Cells CA
1             20                1170
2             40                1110
3             0                 990

"""

# Fes aquí el codi de l'exercici Extra