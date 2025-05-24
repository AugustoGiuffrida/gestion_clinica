from datetime import datetime

class Turno:
    def __init__(self, paciente, medico, fecha_hora):
        if not isinstance(fecha_hora, datetime):
            raise ValueError("fecha_hora debe ser un datetime válido.")
        self._paciente = paciente
        self._medico = medico
        self._fecha_hora = fecha_hora

    def obtener_fecha_hora(self):
        return self._fecha_hora

    def __str__(self):
        fecha_str = self._fecha_hora.strftime("%d/%m/%Y %H:%M")
        return f"Turno el {fecha_str} - {self._paciente} con {self._medico}"
