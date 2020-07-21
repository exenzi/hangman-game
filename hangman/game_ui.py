import os, os.path

class UI():
    # Выводит всю нужную информацию на экран
    def __init__(self, game):
        self.game = game
        # Принимаем в качестве параметра доступ к инстанции игры

    def show(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'\nСлово: {self.game.get_word()}')

        # Открываем картинку в соответствии с количествой ошибок
        errors = self.game.get_errors()
        error_count = len(errors)
        filename = os.path.join(os.path.dirname(__file__), f'figures/{error_count}.txt')
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')

        if errors:
            print(f'Ошибки ({error_count}):', ', '.join(errors))

        print('У вас осталось ошибок:', 7 - error_count)

    def check(self):
        if self.game.is_won():
            print('Игра пройдена!')
            return True
        if self.game.is_lost():
            print('Было загадано слово', self.game.get_actual_word())
            print('Игра проиграна')
            return True
        return False
