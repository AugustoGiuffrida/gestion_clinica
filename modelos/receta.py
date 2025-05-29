from datetime import datetime

class Receta:
    def __init__(self, paciente, medico, medicamentos):
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__medicamentos__ = medicamentos[:]
        self.__fecha__ = datetime.now()

    def __str__(self):
        lista = ', '.join(self.__medicamentos__)
        fecha_str = self.__fecha__.strftime("%d/%m/%Y")
        return f"Receta del {fecha_str} - {self.__paciente__} con {self.__medico__}: {lista}"
