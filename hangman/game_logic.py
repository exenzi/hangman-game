class Logic():
    def __init__(self, word):
        self.word = []
        self.errors = set()

        # Буквы хранятся в словаре:
        # ключи - сами буквы
        # значения - открыты ли они

        for char in word:
            self.word.append({'char': char, 'opened': False})

    def guess(self, char):
        # Если хотя бы одна буква открылась, то флаг right станет True,
        # иначе запишет букву в ошибку

        right = False
        for letter in self.word:
            if char == letter['char']:
                letter['opened'] = True
                right = True

        # Буквы й, и, а так же е ё должны считаться как одна ошибка ~Андрей
        if not right:
            if (char == 'ё' and 'е' in self.errors) \
            or (char == 'е' and 'ё' in self.errors) \
            or (char == 'и' and 'й' in self.errors) \
            or (char == 'й' and 'и' in self.errors):
                return -1
            self.errors.add(char)

    def is_won(self):
        # Возвращает, выиграл ли пользователь
        for letter in self.word:
            if not letter['opened']:
                return False
        return True

    def is_lost(self):
        # Возвращает, проиграл ли пользователь
        if len(self.errors) == 7:
            return True
        return False

    def get_word(self):
        # Возвращает готовое слово со всеми нужными пропусками и пробелами
        result = []
        for letter in self.word:
            if letter['opened']:
                result.append(letter['char'])
            else:
                result.append('__')
        return ' '.join(result)

    def get_errors(self):
        # Возвращает буквы, которые пользователь угадал неправильно
        return self.errors

    def __str__(self):
        return str(self.word)
