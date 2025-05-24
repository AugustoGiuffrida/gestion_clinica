class Paciente:
    def __init__(self, nombre, dni, fecha_nacimiento):
        self._nombre = nombre
        self._dni = dni
        self._fecha_nacimiento = fecha_nacimiento

    def obtener_dni(self):
        return self._dni

    def __str__(self):
        return f"{self._nombre} (DNI: {self._dni})"
