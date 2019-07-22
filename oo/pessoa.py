class Pessoa:
    # atributos de instancia
    def __init__(self, nome=None, idade=35):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):  # atributo da classe
        return f'Olá {id(self)}'


if __name__ == "__main__":
    p = Pessoa(nome='Joana')
    print(p.cumprimentar())
    print(id(p))
    print(f'p.nome: {p.nome}')
    p.nome = 'Maria'
    print(f'p.nome: {p.nome}')
    print(f'p.idade: {p.idade}')
