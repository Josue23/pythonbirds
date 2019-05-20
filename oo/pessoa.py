class Pessoa:
    def cumprimentar(self):
        return f'Olá id(self): {id(self)}'


if __name__ == '__main__':
    maria = Pessoa()
    print(maria.cumprimentar())
    print(f'id(maria): {id(maria)}')
