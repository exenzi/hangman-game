import random
from hangman import game_ui, game_logic

DEBUG = True

random_line = random.choice(open("words.txt").readlines()).rstrip('\n')
game = game_logic.Logic(random_line)
ui = game_ui.UI(game)

while True:
    ui.show()
    if DEBUG:
        print(game.word)
    answer = input('Введите следующую букву: ').strip().lower()
    if len(answer) != 1:
        print('Вводите только одну букву!')
        continue

    game.guess(answer)

    if game.is_won():
        print('Игра пройдена!')
        break
    if game.is_lost():
        print('Игра проиграна')
        break
