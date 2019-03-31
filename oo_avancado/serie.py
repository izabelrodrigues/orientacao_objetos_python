from oo_avancado.programa import Programa
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()
atlanta.dar_likes()
print(f'Nome: {atlanta.nome} - Likes: {atlanta.likes}')