import random
from hangman import game_ui, game_logic

# Нужно ли выводить загаданное слово
DEBUG = True

random_line = random.choice(open("words.txt").readlines()).rstrip('\n')

# Создаём игру и передаём в виде параметра классу UI
game = game_logic.Logic(random_line)
ui = game_ui.UI(game)

while True:
    ui.show()
    if DEBUG:
        print(random_line)

    if ui.check():
        break

    answer = input('Введите следующую букву: ').strip().lower()
    if len(answer) != 1:
        print('Вводите только одну букву!')
        continue

    game.guess(answer)
