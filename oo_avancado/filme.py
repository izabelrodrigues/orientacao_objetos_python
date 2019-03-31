from oo_avancado.programa import Programa
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

print(f'Nome: {vingadores.nome} - Likes: {vingadores.likes}')
