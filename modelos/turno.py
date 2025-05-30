from datetime import datetime

class Turno:
    def __init__(self, paciente, medico, fecha_hora, especialidad):
        if not isinstance(fecha_hora, datetime):
            raise ValueError("fecha_hora debe ser un datetime válido.")
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__fecha_hora__ = fecha_hora
        self.__especialidad__ = especialidad        

    def obtener_medico(self):
        return self._medico


    def obtener_fecha_hora(self):
        return self.__fecha_hora__

    def __str__(self):
        fecha_str = self.__fecha_hora__.strftime("%d/%m/%Y %H:%M")
        return f"Turno: {self.__paciente__} con {self.__medico__} ({self.__especialidad__}) el {fecha_str}"

