from datetime import datetime

class Receta:
    def __init__(self, paciente, medico, medicamentos):
        self._paciente = paciente
        self._medico = medico
        self._medicamentos = medicamentos[:]  # copia de la lista
        self._fecha = datetime.now()

    def __str__(self):
        lista = ', '.join(self._medicamentos)
        fecha_str = self._fecha.strftime("%d/%m/%Y")
        return f"Receta del {fecha_str} - {self._paciente} con {self._medico}: {lista}"
