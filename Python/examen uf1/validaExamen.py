import importlib.util
import sys
import string
import random

results = {
    "ex0": 1,
    "ex0insercio": 1,
    "ex0id": 1,
    "ex0dades": 1,
    "ex1": 1,
    "ex2": 1,
    "ex2dni": 1,
    "ex2name": 1,
    "ex2age": 1,
    "ex2antiquity": 1,
    "ex2games": 1,
    "ex3": 1
}

def load_file(filename):
    spec = importlib.util.spec_from_file_location(filename, f'./{filename}.py')
    module = importlib.util.module_from_spec(spec)
    sys.modules[filename] = module
    spec.loader.exec_module(module)
    return module


if len(sys.argv) != 2:
    print("Usage: python validaExamen.py <nom_alumne>")
    sys.exit(1)

alumne = sys.argv[1]
examen = load_file(alumne)

def validate_student_id_format(student_id):
    # Comprovar el format: 3 números, 3 lletres, guió, 2 números
    parts = student_id.split("-")
    if len(parts) != 2 or len(parts[0]) != 6 or len(parts[1]) != 2:
        return False

    if not parts[0][:3].isdigit() or not parts[0][3:6].isalpha() or not parts[1].isdigit():
        return False

    return True

def validate_student_data(student):
    # Validar el DNI
    if not (student['dni'][:-1].isdigit() and student['dni'][-1].isalpha() and int(student['dni'][:-1]) < 60000000):
        print(f"    Ha fallat el format del DNI: {student['dni']}")
        return False

    # Validar l'edat
    if not (5 <= student['age'] <= 15):
        print(f"    Ha fallat l'edat de l'estudiant: {student['age']}")
        return False

    # Validar l'antiguitat
    if not (0 <= student['antiquitey'] <= 10):
        print(f"    Ha fallat el valor de l'antiguitat: {student['antiquitey']}")
        return False

    # Validar els jocs
    valid_games = ["Tennis", "Ping-Pong", "Indoor Hockey", "Football", "Chess", "Swimming", "Basketball", "Volleyball", "Handball"]
    if not (2 <= len(student["games"]) <= 5 and all(game in valid_games for game in student["games"]) and len(set(student["games"])) == len(student["games"])):
        print(f"    Ha fallat el valor de la llista 'games': {student['games']}")
        return False
    return True

# Funció per validar la funció addStudents
def validate_exercici_0():
    global examen
    global results

    for cntTest in range(0, 25):

        print(f"Test Exercici 0: {cntTest}")

        # Validar número d'usuaris inserits és correcte
        original_count = len(examen.students)
        number_to_add = random.randint(2,5)
        generated_ids = examen.addStudents(number_to_add)
        if len(examen.students) != original_count + number_to_add:
            results["ex0insercio"] = 0
            print("  Ha fallat el número d'estudiants insertat")

        if generated_ids is None:
            results["ex0insercio"] = 0
            generated_ids = list(examen.students.keys())[-number_to_add:]
            print("  La funció 'addStudents' no retorna res")

        # Comprovar la validesa de cada estudiant afegit
        for student_id in generated_ids:
            # Comprovar el format de l'identificador
            if not validate_student_id_format(student_id):
                results["ex0id"] = 0
                print(f"  Ha fallat el format de l'id: ${student_id}")

            # Comprovar les dades de l'estudiant
            student = examen.students[student_id]
            if not validate_student_data(student):
                results["ex0dades"] = 0
                print(f"  Ha fallat les dades de l'estudiant")

def searchStudents(param, value):
    # Convertir el valor a minúscules per a la cerca insensible a majúscules
    value = str(value).lower()
    found_students = []

    # Iterar sobre els estudiants i buscar coincidències
    for student_id, student_data in examen.students.items():
        if param in student_data:
            # Per a les llistes, com 'games', necessitem un tractament especial
            if isinstance(student_data[param], list):
                if any(value in str(game).lower() for game in student_data[param]):
                    found_students.append(student_id)
            # Per a altres tipus de dades
            elif value in str(student_data[param]).lower():
                found_students.append(student_id)

    # Imprimir el resultat de la cerca
    # print(f"(searchStudents) Found {len(found_students)}: {found_students}")
    return found_students

def validate_exercici_1():
    global examen
    test_cases = []

    # Generar test_cases
    for student_id, student_data in examen.students.items():
        test_cases.append(('dni', student_data['dni']))
        test_cases.append(('name', student_data['name']))
        test_cases.append(('age', student_data['age']))
        test_cases.append(('antiquitey', student_data['antiquitey']))

        cntGame = 0
        for game in student_data['games']:
            if (cntGame % 3 == 0):
                test_cases.append(('games', game))
            elif (cntGame % 3 == 1):
                test_cases.append(('games', game.lower()))
            else:
                test_cases.append(('games', game.upper()))

    if len(test_cases) > 100:
        test_cases = random.sample(test_cases, 100)

    # Validar
    cntTest = 0
    for param, value in test_cases:
        print(f"Test Exercici 1: {cntTest}")
        cntTest = cntTest + 1
        found_students_examen = examen.searchStudents(param, value)
        found_students_reference = searchStudents(param, value)

        if not isinstance(found_students_examen, list):
            results["ex1"] = 0
            print(f"  La cerca amb {param}={value} no retorna una llista")
        else:
            if set(found_students_examen) != set(found_students_reference):
                results["ex1"] = 0
                reference_str = str(found_students_reference)[:100]
                found_str = str(found_students_examen)[:100]
                print(f"  La cerca amb {param}={value} retorna resultats incorrectes:")
                print(f"  > esperat {reference_str}")
                print(f"  > obtingut {found_str}")

def validate_exercici_2():
    global examen
    numTests = 5
    lenKeys = len(examen.students.keys())
    if (lenKeys < 5):
        numTests = lenKeys
    cntTest = 0
    for student_id in list(examen.students.keys())[:numTests]:  # Utilitzar només alguns estudiants per la prova
        print(f"Test Exercici 2: {cntTest}")
        cntTest = cntTest + 1
        rstDni = examen.modifyStudents(student_id, 'dni', 'dni Modificat')
        if rstDni is False:
            print(f"  Error al modificar el dni, no ha retornat True")
            results["ex2dni"] = 0
        if rstDni is None:
            print(f"  Error al modificar el dni, no s'ha rebut ni True ni False")
            results["ex2dni"] = 0
        rstName = examen.modifyStudents(student_id, 'name', 'Nom Modificat')
        if rstName is False:
            print(f"  Error al modificar el name, no ha retornat True")
            results["ex2name"] = 0
        if rstName is None:
            print(f"  Error al modificar el name, no s'ha rebut ni True ni False")
            results["ex2name"] = 0
        rstAge = examen.modifyStudents(student_id, 'age', 99)
        if rstAge is False:
            print(f"  Error al modificar age, no ha retornat True")
            results["ex2name"] = 0
        if rstAge is None:
            print(f"  Error al modificar age, no s'ha rebut ni True ni False")
            results["ex2name"] = 0
        rstAnt = examen.modifyStudents(student_id, 'antiquitey', 99)
        if rstAnt is False:
            print(f"  Error al modificar antiquitey, no ha retornat True")
            results["ex2antiquity"] = 0
        if rstAnt is None:
            print(f"  Error al modificar antiquitey, no s'ha rebut ni True ni False")
            results["ex2antiquity"] = 0
        rstGames = examen.modifyStudents(student_id, 'games', ['Game1', 'Game2'])
        if rstAnt is False:
            print(f"  Error al modificar games, no ha retornat True")
            results["ex2games"] = 0
        if rstAnt is None:
            print(f"  Error al modificar games, no s'ha rebut ni True ni False")
            results["ex2games"] = 0
        
        # Comprovar les modificacions
        if examen.students[student_id]['dni'] != 'dni Modificat' or \
           examen.students[student_id]['name'] != 'Nom Modificat' or \
           examen.students[student_id]['age'] != 99 or \
           examen.students[student_id]['antiquitey'] != 99 or \
           examen.students[student_id]['games'] != ['Game1', 'Game2']:
            print(f"  Alguna dada no s'ha modificat correctament")
            results["ex2"] = 0

    # Intentar modificar un usuari no existent
    rstWrong = examen.modifyStudents('00000000', 'name', 'Nom Fals')
    if rstWrong is True:
        print(f"  Error al modificar un usuari inexsistent, no ha retornat False")
        results["ex2"] = 0
    if rstWrong is None:
        print(f"  Error al modificar un usuari inexsistent, no s'ha rebut ni True ni False")
        results["ex2"] = 0

def validate_exercici_3():
    global examen

    print(f"Test Exercici 3:")
    student_ids_to_delete = random.sample(list(examen.students.keys()), random.randint(2, 3))
    deleted_students = examen.deleteStudents(student_ids_to_delete)
    for student_id in student_ids_to_delete:
        if student_id in examen.students:
            print(f"  Error, l'estudiant {student_id} no ha estat esborrat")
            results["ex3"] = 0

    # Comprovar si la llista retornada conté els identificadors correctes
    if set(deleted_students) != set(student_ids_to_delete):
        print(f"  La llista d'estudiants esborrats no és correcta:")
        print(f"  > esperat {student_ids_to_delete}")
        print(f"  > obtingut {deleted_students}")
        results["ex3"] = 0

def get_exam_grade():
    grade = 0

    # Exercici 0
    ex0 = 0
    if all(results[key] == 1 for key in ['ex0', 'ex0insercio', 'ex0id', 'ex0dades']):
        ex0 = 2
    elif any(results[key] == 1 for key in ['ex0', 'ex0insercio', 'ex0id', 'ex0dades']):
        ex0 = 1
    else:
        ex0 = 0

    # Exercici 1
    ex1 = 2 if results['ex1'] == 1 else 0

    # Exercici 2
    ex2 = 0
    if all(results[key] == 1 for key in ['ex2', 'ex2dni', 'ex2name', 'ex2age', 'ex2antiquity', 'ex2games']):
        ex2 = 2
    elif any(results[key] == 1 for key in ['ex2', 'ex2dni', 'ex2name', 'ex2age', 'ex2antiquity', 'ex2games']):
        ex2 = 1
    else:
        ex2 = 0

    # Exercici 3
    ex3 = 2 if results['ex3'] == 1 else 0

    print(f"Exercici 0: {ex0}")
    print(f"Exercici 1: {ex1}")
    print(f"Exercici 2: {ex2}")
    print(f"Exercici 3: {ex3}")
    return ex0 + ex1 + ex2 + ex3


# Executar la validació
validate_exercici_0()
print("")
validate_exercici_1()
print("")
validate_exercici_2()
print("")
validate_exercici_3()

print("Resultat testos:")
print(results)
nota = get_exam_grade()
print(f"Nota '{alumne}' (sense comptar l'exercici 4): {nota}")
