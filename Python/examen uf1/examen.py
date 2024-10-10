import os
import csv
import json
import random
import string
import platform

def clearScreen():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def afegeixPrompt(frase):
    prompt.append(frase)
    if len(prompt) > 15:
        prompt.pop(0)

def escriuPrompt():
    for cnt in range(0, len(prompt)):
        print(prompt[cnt])

prompt = []

# Nom, Cognoms i DNI
# Denis Fernández Varariu 47956998C

# Exercici UF1 --------- --------- --------- ---------

# Diccionari de mascotes
pets = {}

# Funció que crea un codi aleatori
def createCode():
    lletres = string.ascii_uppercase  # Todas las letras mayúsculas
    code = ''.join([str(random.randint(0, 9)) for _ in range(3)])  # Tres números
    code += ''.join(random.choices(lletres, k=3))  # Tres letras
    code += "-" + str(random.randint(1, 15))  # Año entre 1 y 15
    return code

# Funció que crea un nom aleatori entre 10 noms
def createName():
    noms = ["Max", "Bella", "Luna", "Charlie", "Lucy", "Cooper", "Bailey", "Daisy", "Sadie", "Oliver"]
    nom = random.choice(noms)
    return nom

# Funció que crea una edat aleatòria entre 1 i 15 anys
def createAge():
    edat = random.randint(1, 15)
    return edat

# Funció que crea un tipus de mascota aleatori
def createType():
    tipus = ["gos", "gat", "conill", "hamster", "ocell"]
    return random.choice(tipus)

# Funció que crea una llista d'activitats aleatòria entre 2 i 5 activitats (no repetides)
def createActivities():
    acts = ["Correr", "Saltar", "Nedar", "Caçar", "Jugar a la pilota", "Dormir"]
    return random.sample(acts, random.randint(2, 5))

# Funció que afegeix 'number' mascotes al diccionari 'pets'
def addPets(number):
    codis = []
    for _ in range(number):
        while True:
            codi = createCode()
            if codi not in pets:  # Asegurarse de que no existe ya ese código
                break
        pet = {
            "name": createName(),
            "age": createAge(),
            "type": createType(),
            "activities": createActivities()
        }
        pets[codi] = pet
        codis.append(codi)
    afegeixPrompt(f"(addPets) {number} pets added")
    return codis

# Funció que permet buscar mascotes a partir d'un paràmetre
def searchPets(param, value):
    codis = []
    for key, pet in pets.items():
        if param in pet and pet[param] == value:
            codis.append(key)
    if codis:
        afegeixPrompt(f"(searchPets) Found {len(codis)}: {codis}")
    else:
        afegeixPrompt("No s'han trobat mascotes amb aquests criteris.")
    return codis

# Funció que permet modificar mascotes a partir del seu codi
def modifyPets(code, param, value):
    if code in pets:
        pets[code][param] = value
        afegeixPrompt(f"(modifyPets) Pet {code} modified")
    else:
        afegeixPrompt(f"(modifyPets) Pet {code} not found")
    return

# Funció que permet borrar mascotes a partir del seu codi
def deletePets(codes):
    esborrats = []
    for code in codes:
        if code in pets:
            del pets[code]
            esborrats.append(code)
    afegeixPrompt(f"(deletePets) Pets deleted: {esborrats}")
    return esborrats

# Funció que llista totes les mascotes
def listPets():
    if pets:
        afegeixPrompt("Llista de mascotes:")
        for pet_code, pet_info in pets.items():
            afegeixPrompt(f"{pet_code}: {pet_info}")
    else:
        afegeixPrompt("No hi ha mascotes disponibles.")

# Funció del menú principal
def menu():
    error = ""
    while True:
        clearScreen()
        print(
"""Gestió de mascotes:
1) Llista
2) Afegir
3) Modificar
4) Esborrar
5) Buscar""")
        if error != "":
            print(error)
            error = ""
        print("""0) Sortir
Escull una opció [0-5]:  """)                   

        escriuPrompt()
        opcio = input(" ")
        
        if opcio == "1":
            listPets()
        elif opcio == "2":
            num = int(input("Quantes mascotes vols afegir? "))
            addPets(num)
        elif opcio == "3":
            code = input("Introdueix el codi de la mascota a modificar: ")
            param = input("Introdueix el paràmetre a modificar (name, age, type, activities): ")
            if param == "activities":
                acts = input("Introdueix les noves activitats (separades per comes): ")
                value = acts.split(",")
            elif param == "age":
                value = int(input("Introdueix el nou valor: "))
            else:
                value = input("Introdueix el nou valor: ")
            modifyPets(code, param, value)
        elif opcio == "4":
            code = input("Introdueix el codi de la mascota a esborrar (separa per comes si són més d'una): ")
            codel = code.split(",")
            deletePets(codel)
        elif opcio == "5":
            param = input("Introdueix el paràmetre per buscar (name, age, type, activities): ")
            value = input("Introdueix el valor de cerca: ")
            result = searchPets(param, value)
            if not result:
                afegeixPrompt("No s'han trobat mascotes amb aquests criteris.")
        elif opcio == "0":
            return
        else:
            error = "ERROR: Opció no vàlida"

# Inici del programa
menu()




#print(pets)
# Exercici UF2 --------- --------- --------- ---------

# Retorna el resultat de les operacions lògiques 'AND' i 'XOR' per les entrades A i B
def simple_logic_gate(a, b, operation):
    return False

# Mostra una taula amb els valors de les operacions lògiques 'AND' i 'XOR'
def table_logic_gate():
    pass

# Mostra les mitjanes de dues llistes numèriques d'igual longitud
def calculate_average(list1, list2):
    pass

# Calcula recursivament les particions d'un número
def particions(n, max_number=None):
    return 0

# Genera una excepció de valor si l'entrada és un text i de valor si l'entrada és un número
def exceptionGenerate(input):
    pass

# Crida a la funció anterior i mostra un error segons si és de tipus 'ValueError' o 'IndexError'
def exceptionHandle(func):
    pass

# Exercici UF3 --------- --------- --------- ---------

# Mostra els contingus d'un arxiu .csv entre les linies 'begin' i 'end'
def list_csv(file, begin, end):
    return []

# Retorna el valor d'un arxiu .csv a la posició row/column
def read_csv(file, row, column):
    return ""

# Modifica les dades d'un .csv a la posició 'row' / 'column'
def modify_csv(file, row, column, value):
    pass

# Genera un nom aleatòri de números i lletres que comença amb una lletra
def generate_random_name():
    return ''

# Canvia el nom dels arxius de la ruta 'path' i guarda les equivalències a 'files.json'
def fun_files(path):
    pass

# Reestableix els noms d'arxius segons la informació de 'files.json'
def undo_fun_files(path):
    pass