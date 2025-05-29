class Medico:
    def __init__(self, nombre, matricula, especialidad):
        self.__nombre__ = nombre
        self.__matricula__ = matricula
        self.__especialidad__ = especialidad

    def obtener_matricula(self):
        return self.__matricula__

    def __str__(self):
        return f"Dr. {self.__nombre__} (Matrícula: {self.__matricula__}, Especialidad: {self.__especialidad__})"
