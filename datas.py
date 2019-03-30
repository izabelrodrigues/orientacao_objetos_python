class Data:
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def exibe_data_formatada(self):
        print(self.__dia, self.__mes, self.__ano, sep='/')
