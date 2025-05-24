class HistoriaClinica:
    def __init__(self, paciente):
        self._paciente = paciente
        self._turnos = []
        self._recetas = []

    def agregar_turno(self, turno):
        self._turnos.append(turno)

    def agregar_receta(self, receta):
        self._recetas.append(receta)

    def __str__(self):
        out = [f"--- Historia Clínica de {self._paciente} ---", "Turnos:"]
        for t in self._turnos:
            out.append(f"  • {t}")
        out.append("Recetas:")
        for r in self._recetas:
            out.append(f"  • {r}")
        return "\n".join(out)
