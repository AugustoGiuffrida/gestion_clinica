#from especialidad import Especialidad

class Medico:
    def __init__(self, nombre, matricula):
        self.__nombre__ = nombre
        self.__matricula__ = matricula
        self.__especialidades__ = []

    def agregar_especialidad(self, especialidad):
        self.__especialidades__.append(especialidad)

    def obtener_matricula(self):
        return self.__matricula__

    def obtener_especialidad_para_dia(self, dia):
        for especialidad in self.__especialidades__:
            if especialidad.verificar_dia(dia):
                return especialidad.obtener_especialidad()
        return None

    def __str__(self):
        especialidades_str = ', '.join(str(esp) for esp in self.__especialidades__)
        return f"{self.__nombre__} (Matrícula: {self.__matricula__}) - Especialidades: {especialidades_str}"
