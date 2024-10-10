import os
import platform
import random

# Aquesta funció neteja la pantalla, no la modifiquis
def clear_screen():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')

"""
-------------------------------------------------------------------------------
Exercici 0
-------------------------------------------------------------------------------

Fes una funció "generate_cards" que retorna un array amb 13 cartes de Poker

* Les cartes de poker van del 2 al 10 (inclòssos) i després J, Q, K, A
* No hi ha pals (no hi ha diamants, cors, piques ni trèbols)
"""

# Fes aquí el codi de l'exercici 0
def generate_cards():
    return ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


"""
-------------------------------------------------------------------------------
Exercici 1
-------------------------------------------------------------------------------

Fes una funció "set_name" que retorna un nom escrit per l'usuari i que:

* Cada vegada que l'usuari fa un intent d'escriure el nom:

  - El primer cop, apareix: 
    "Set your name: "
  - Si l'usuari escriu un nom no valid, apareix el missatge: 
    "Invalid name (only letters and spaces allowed), set your name again: "
  - Cal netejar la pantalla a cada petició

* Ho ha de demanar fins que el nom sigui vàlid
* Només s'accepten lletres i espais
* Quan s'ha escollit un nom vàlid, la funció retorna el nom
    
Perquè quedi clar:

* "Albert Johanson" és un nom vàlid
* "[Albert!" no és un nom vàlid
* "Albert33" no és un nom vàlid
"""

# Fes aquí el codi de l'exercici 1
def set_name():
    while True:
        clear_screen()
        name = input("Set your name: ")
        if all(part.isalpha() for part in name.split()):
            return name
        print("Invalid name (only letters and spaces allowed), set your name again: ")



""  
"""
-------------------------------------------------------------------------------
Exercici 2
-------------------------------------------------------------------------------

Fes una funció "select_opponent" que retorna un oponent seleccionat per l'usuari:

* Quan l'usuari escull un oponent, s'esborra la pantalla i es mostra el següent menú.

Select Opponent -----------------------
1) Hal 9000
2) Skynet
3) Agent Smith
4) The Borg
Select your opponent:

* Les opcions s'han de mostrar a partir d'una llista d'oponents

* Si s'escull una opció incorrecta, s'esborra la pantalla i es mostra el menú anterior amb el missatge:
  "Invalid option, select your opponent again: "

* Si s'escull una opció correcta, la funció retorna el nom de l'oponent seleccionat

"""

# Fes aquí el codi de l'exercici 2
def select_opponent():
    opponents = ["Hal 9000", "Skynet", "Agent Smith", "The Borg"]
    while True:
        clear_screen()
        print("Select Opponent -----------------------")
        
        # Contador manual para mostrar el índice de cada oponente
        index = 1
        for opponent in opponents:
            print(f"{index}) {opponent}")
            index += 1

        choice = input("Select your opponent: ")
        
        # Comprobar si la opción es un número válido dentro del rango de opciones
        if choice.isdigit() and 1 <= int(choice) <= len(opponents):
            return opponents[int(choice) - 1]
        else:
            print("Invalid option, select your opponent again: ")

"""
-------------------------------------------------------------------------------
Exercici 3
-------------------------------------------------------------------------------

Fes una funció "game_round" que: 

* A partir d'una baralla de cartes barrejada
* Cada jugador treu tres cartes i es sumen els punts
* Primer treu les cartes l'usuari i després l'oponent (l'ordinador)
* Guanya la ronda el jugador que té més punts
* Si empaten en punts, la ronda no compta
* Els valors numèrics sumen la seva puntuació
  - Les lletres sumen: J, Q, K = 11 i A = 12
  - Per cada ronda es neteja la pantalla i s'han descriure missatges tipus:

" > 'Albert Johanson' got ['3', 'A', '5'] : 20"
" > 'Hall 9000' got ['7', 'J', '2'] : 20"

* A cada ronda s'ha d'escriure, segons correspongui:
  
  > Player 'nom del jugador' X points, cards: ['carta1', 'carta2', 'carta3']
  > Opponent 'nom de l'oponent' Y points, cards: ['carta1', 'carta2', 'carta3']
  > Round winner: 'nom del jugador' o 'nom de l'oponent' o 'draw'

* Finalment, retorna el jugador que ha guanyat la ronda o "draw" si hi ha hagut empat

"""

# Fes aquí el codi de l'exercici 3
def game_round(player_name, opponent_name):
    cards = generate_cards()
    random.shuffle(cards)

    # Función interna para calcular el valor de las cartas
    def card_value(card):
        if card in ['J', 'Q', 'K']:
            return 11
        elif card == 'A':
            return 12
        else:
            return int(card)

    # Selección de cartas y cálculo de puntaje para el jugador
    player_cards = [cards.pop() for _ in range(3)]
    player_points = sum(card_value(card) for card in player_cards)
    
    # Selección de cartas y cálculo de puntaje para el oponente
    opponent_cards = [cards.pop() for _ in range(3)]
    opponent_points = sum(card_value(card) for card in opponent_cards)

    # Mostrar los resultados de la ronda
    clear_screen()
    print(f"> {player_name} got {player_cards} : {player_points}")
    print(f"> {opponent_name} got {opponent_cards} : {opponent_points}")

    if player_points > opponent_points:
        print(f"Round winner: {player_name}")
        return player_name
    elif opponent_points > player_points:
        print(f"Round winner: {opponent_name}")
        return opponent_name
    else:
        print("Round winner: draw")
        return "draw"

    


"""------------------------------------------------------------------------------
Exercici 4
-------------------------------------------------------------------------------

Fes la funció "game_of_cards" que juga la partida:

* Es jugen rondes fins que un jugador guanya tres rondes

* A cada ronda es mostra el següent missatge:

  - Round X, 'player_name' has won Y rounds, 'opponent_name' has won Z rounds

* Quan s'acaba la ronda, es mostra el següent missatge:
"Keep playing? (yes, no): "

  - Si l'usuari escriu "y" o "yes", es juga una altra ronda
  - Si l'usuari escriu "n" o "no", es torna al menú de joc
  - Si l'usuari escriu una altra cosa, es torna a preguntar.

* Finalment, quan un jugador guanya tres rondes, es mostre un d'aquests missatges:

" > Player 'Albert Johanson' has won the game!"
" > Opponent 'Hal 9000' has won the game!"

I es dóna l'opció de tornar a jugar o tornar al menú de joc:

"Play again? (yes, no): "

  - Si l'usuari escriu "y" o "yes", s'esborra la pantalla i es juga una altra ronda.
  - Si l'usuari escriu "n" o "no", es torna al menú de joc
  - Si l'usuari escriu una altra cosa, es torna a preguntar.

"""

# Fes aquí el codi de l'exercici 4
def game_of_cards(player_name, opponent_name):
    player_wins = 0
    opponent_wins = 0
    round_number = 1

    while player_wins < 3 and opponent_wins < 3:
        print(f"Round {round_number}, {player_name} has won {player_wins} rounds, {opponent_name} has won {opponent_wins} rounds")
        winner = game_round(player_name, opponent_name)
        
        if winner == player_name:
            player_wins += 1
        elif winner == opponent_name:
            opponent_wins += 1
        
        round_number += 1

        if player_wins < 3 and opponent_wins < 3:
            keep_playing = input("Keep playing? (yes, no): ").strip().lower()
            if keep_playing in ['n', 'no']:
                break

    if player_wins == 3:
        print(f"> Player {player_name} has won the game!")
    else:
        print(f"> Opponent {opponent_name} has won the game!")

    play_again = input("Play again? (yes, no): ").strip().lower()
    if play_again in ['y', 'yes']:
        clear_screen()
        game_of_cards(player_name, opponent_name)

"""
-------------------------------------------------------------------------------
Exercici 5
-------------------------------------------------------------------------------

Fes una funció "show_menu" que mostra el menú:

Si no s'ha escollit nom d'usuari:

  Game Of Cards -------------------------
  1) Set your name
  2) Select the opponent  (not available) 
  3) Play                 (not available)
  4) Mostrar menú
  0) Sortir
  Set your option:

Si no s'ha escollit oponent:

  Game Of Cards -------------------------
  1) Set your name        (Albert Johanson)
  2) Select the opponent
  3) Play                 (not available)
  4) Mostrar menú
  0) Sortir
  Set your option:

Quan ja s'ha escollit nom d'usuari i oponent:

  Game Of Cards -------------------------
  1) Set your name        (Albert Johanson)
  2) Select the opponent  (Skynet)
  3) Play
  4) Mostrar menú
  0) Sortir
  Set your option:

Les opcions (not available) no estàn disponibles, i el seu funcionament és aquest:

* Abans de jugar l'usuari ha d'escriure el seu nom
* Un cop ha introduit el seu nom, ha de seleccionar un oponent
* Un cop ha seleccionat un oponent, pot jugar

Per tant:

* Si ha escrit el seu nom, el (not available) desapareix de l'opció 2
* Si ha seleccionat un oponent, el (not available) desapareix de l'opció 3
* Si escullen una opció no vàlida o no sisponible: 

    S'esborra la pantalla
    Es dibuixa el menú (segons correspongui)
    Es torna a demanar una opció amb el text: "Invalid option, set your option again: "

Redibuix del menú:

* El menú ha de fer servir la funció "clear_screen" per netejar la pantalla
* La pantalla del menú s'esborra cada vegada que l'usuari escull una opció

Opcions:

* La opció 0 surt del programa
* La opció 1 crida la funció "set_name"
* La opció 2 crida la funció "select_opponent"
* La opció 3 crida la funció "joc_de_cartes"

"""

# Fes aquí el codi de l'exercici 5
def show_menu():
    player_name = None
    opponent_name = None

    while True:
        clear_screen()
        print("Game Of Cards -------------------------")
        print(f"1) Set your name        {f'({player_name})' if player_name else ''}")
        print(f"2) Select the opponent  {f'({opponent_name})' if opponent_name else '(not available)'}")
        print(f"3) Play                 {'(not available)' if not (player_name and opponent_name) else ''}")
        print("4) Mostrar menú")
        print("0) Sortir")
        
        option = input("Set your option: ").strip()

        if option == "0":
            break
        elif option == "1":
            player_name = set_name()
        elif option == "2":
            if player_name:
                opponent_name = select_opponent()
            else:
                print("Invalid option, set your option again: ")
        elif option == "3":
            if player_name and opponent_name:
                game_of_cards(player_name, opponent_name)
            else:
                print("Invalid option, set your option again: ")
        elif option == "4":
            continue
        else:
            print("Invalid option, set your option again: ")

