from datetime import datetime

class Turno:
    def __init__(self, paciente, medico, fecha_hora):
        if not isinstance(fecha_hora, datetime):
            raise ValueError("fecha_hora debe ser un datetime válido.")
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__fecha_hora__ = fecha_hora

    def obtener_fecha_hora(self):
        return self.__fecha_hora__

    def __str__(self):
        fecha_str = self.__fecha_hora__.strftime("%d/%m/%Y %H:%M")
        return f"Turno el {fecha_str} - {self.__paciente__} con {self.__medico__}"
