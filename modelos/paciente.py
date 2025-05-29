class Paciente:
    def __init__(self, nombre, dni, fecha_nacimiento):
        self.__nombre__ = nombre
        self.__dni__ = dni
        self.__fecha_naciemiento__ = fecha_nacimiento

    def obtener_dni(self):
        return self.__dni__

    def __str__(self):
        return f"{self.__nombre__} (DNI: {self.__dni__})"
