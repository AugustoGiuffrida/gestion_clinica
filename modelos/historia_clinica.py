class HistoriaClinica:
    def __init__(self, paciente):
        self.__paciente__ = paciente
        self.__turnos__ = []
        self.__recetas__ = []

    def agregar_turno(self, turno):
        self.__turnos__.append(turno)

    def agregar_receta(self, receta):
        self.__recetas__.append(receta)

    def obtener_turnos(self):
        return list(self.__turnos__)

    def obtener_recetas(self):
        return list(self.__recetas__)

    def __str__(self):
        out = [f"--- Historia Clínica de {self.__paciente__} ---", "Turnos:"]
        for t in self.__turnos__:
            out.append(f"  • {t}")
        out.append("Recetas:")
        for r in self.__recetas__:

            out.append(f"  • {r}")
        return "\n".join(out)
