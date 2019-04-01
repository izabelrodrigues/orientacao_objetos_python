from oo_avancado.filme import Filme
from oo_avancado.serie import Serie


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()
atlanta.dar_likes()

playlist = [vingadores, atlanta]
for programa in playlist:
    print(programa)

