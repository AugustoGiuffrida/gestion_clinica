class Medico:
    def __init__(self, nombre, matricula, especialidad):
        self._nombre = nombre
        self._matricula = matricula
        self._especialidad = especialidad

    def obtener_matricula(self):
        return self._matricula

    def __str__(self):
        return f"Dr. {self._nombre} (Matrícula: {self._matricula}, Especialidad: {self._especialidad})"
