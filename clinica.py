from datetime import datetime
from modelos.paciente import Paciente
from modelos.medico import Medico
from modelos.turno import Turno
from modelos.receta import Receta
from modelos.historia_clinica import HistoriaClinica
from excepciones.excepciones import (
    PacienteNoExisteError,
    MedicoNoExisteError,
    TurnoDuplicadoError,
)

class Clinica:
    def __init__(self):
        self._pacientes = {}
        self._medicos = {}
        self._turnos = []
        self._historias_clinicas = {}

    def agregar_paciente(self, paciente):
        dni = paciente.obtener_dni()
        self._pacientes[dni] = paciente
        self._historias_clinicas[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico):
        mat = medico.obtener_matricula()
        self._medicos[mat] = medico

    def agendar_turno(self, dni, matricula, fecha_hora):
        if dni not in self._pacientes:
            raise PacienteNoExisteError(f"No existe paciente DNI {dni}.")
        if matricula not in self._medicos:
            raise MedicoNoExisteError(f"No existe médico Matrícula {matricula}.")
        # validar duplicado
        for t in self._turnos:
            if (t.obtener_fecha_hora() == fecha_hora
                and t._medico.obtener_matricula() == matricula):
                raise TurnoDuplicadoError("Turno duplicado para ese médico/hora.")
        paciente = self._pacientes[dni]
        medico = self._medicos[matricula]
        nuevo = Turno(paciente, medico, fecha_hora)
        self._turnos.append(nuevo)
        self._historias_clinicas[dni].agregar_turno(nuevo)

    def emitir_receta(self, dni, matricula, medicamentos):
        if dni not in self._pacientes:
            raise PacienteNoExisteError(f"No existe paciente DNI {dni}.")
        if matricula not in self._medicos:
            raise MedicoNoExisteError(f"No existe médico Matrícula {matricula}.")
        paciente = self._pacientes[dni]
        medico = self._medicos[matricula]
        receta = Receta(paciente, medico, medicamentos)
        self._historias_clinicas[dni].agregar_receta(receta)

    def obtener_historia_clinica(self, dni):
        if dni not in self._historias_clinicas:
            raise PacienteNoExisteError(f"No hay historia clínica para DNI {dni}.")
        return self._historias_clinicas[dni]

    def obtener_turnos(self):
        return list(self._turnos)
