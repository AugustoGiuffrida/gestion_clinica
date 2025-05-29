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
        """
        Inicializa la clínica con estructuras vacías para:
         - pacientes: mapea DNI → Paciente
         - médicos:  mapea matrícula → Medico
         - turnos:   lista de Turno
         - historias_clinicas: mapea DNI → HistoriaClinica
        """
        self.__pacientes__ = {}
        self.__medicos__ = {}
        self.__turnos__ = []
        self.__historias_clinicas__ = {}

    def agregar_paciente(self, paciente):
        """
        Registra un nuevo paciente en la clínica.

        Parámetros:
            paciente (Paciente): instancia de Paciente a agregar.

        Efecto:
            - Añade el objeto Paciente al diccionario _pacientes por su DNI.
            - Crea una nueva HistoriaClinica vacía asociada a ese DNI.
        """
        dni = paciente.obtener_dni()
        # Guardamos el paciente bajo su DNI
        self.__pacientes__[dni] = paciente
        # Creamos la historia clínica vacía para este paciente
        self.__historias_clinicas__[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico):
        """
        Registra un nuevo médico en la clínica.

        Parámetros:
            medico (Medico): instancia de Medico a agregar.

        Efecto:
            - Añade el objeto Medico al diccionario _medicos por su matrícula.
        """
        mat = medico.obtener_matricula()
        self.__medicos__[mat] = medico

    def agendar_turno(self, dni, matricula, fecha_hora):
        """
        Agenda un turno para un paciente con un médico en una fecha y hora específicas.

        Parámetros:
            dni (str): DNI del paciente.
            matricula (str): Matrícula del médico.
            fecha_hora (datetime): Objeto datetime del turno.

        Excepciones:
            PacienteNoExisteError: si el DNI no está registrado.
            MedicoNoExisteError: si la matrícula no está registrada.
            TurnoDuplicadoError: si ya existe un turno para ese médico en esa fecha y hora.
        """
        # Validar existencia de paciente
        if dni not in self.__pacientes__:
            raise PacienteNoExisteError(f"No existe paciente DNI {dni}.")
        # Validar existencia de médico
        if matricula not in self.__medicos__:
            raise MedicoNoExisteError(f"No existe médico Matrícula {matricula}.")

        # Validar que no haya duplicado: mismo médico y misma fecha_hora
        for t in self.__turnos__:
            # obtener_fecha_hora() compara fecha y hora exactos
            if (t.obtener_fecha_hora() == fecha_hora
                and t.__medico__.obtener_matricula() == matricula):
                raise TurnoDuplicadoError("Turno duplicado para ese médico/hora.")

        # Recuperar objetos
        paciente = self.__pacientes__[dni]
        medico    = self.__medicos__[matricula]
        # Crear y almacenar el nuevo turno
        nuevo = Turno(paciente, medico, fecha_hora)
        self.__turnos__.append(nuevo)
        # Añadir el turno a la historia clínica del paciente
        self.__historias_clinicas__[dni].agregar_turno(nuevo)

    def emitir_receta(self, dni, matricula, medicamentos):
        """
        Emite una receta médica para un paciente.

        Parámetros:
            dni (str): DNI del paciente.
            matricula (str): Matrícula del médico.
            medicamentos (list[str]): Lista de nombres de medicamentos.

        Excepciones:
            PacienteNoExisteError: si el DNI no está registrado.
            MedicoNoExisteError: si la matrícula no está registrada.
        """
        # Verificar que paciente exista
        if dni not in self.__pacientes__:
            raise PacienteNoExisteError(f"No existe paciente DNI {dni}.")
        # Verificar que médico exista
        if matricula not in self.__medicos__:
            raise MedicoNoExisteError(f"No existe médico Matrícula {matricula}.")

        paciente = self.__pacientes__[dni]
        medico    = self.__medicos__[matricula]
        # Crear la receta y añadirla a la historia clínica
        receta = Receta(paciente, medico, medicamentos)
        self.__historias_clinicas__[dni].agregar_receta(receta)

    def obtener_historia_clinica(self, dni):
        """
        Devuelve la historia clínica completa de un paciente.

        Parámetros:
            dni (str): DNI del paciente.

        Retorno:
            HistoriaClinica: objeto con turnos y recetas del paciente.

        Excepciones:
            PacienteNoExisteError: si no existe historia clínica para ese DNI.
        """
        if dni not in self.__historias_clinicas__:
            raise PacienteNoExisteError(f"No hay historia clínica para DNI {dni}.")
        return self.__historias_clinicas__[dni]

    def obtener_turnos(self):
        """
        Devuelve la lista de todos los turnos agendados.

        Retorno:
            list[Turno]: copia de la lista interna de turnos.
        """
        return list(self.__turnos__)



    def obtener_pacientes(self):
        """
        Devuelve la lista de todos los pacientes registrados en la clínica.

        Retorno:
            list[Paciente]: copia de la lista de objetos Paciente.
        """
        # Tomamos los valores del diccionario _pacientes y devolvemos una copia de la lista
        return list(self.__pacientes__.values())



    def obtener_medicos(self):
        """
        Devuelve la lista de todos los médicos registrados en la clínica.

        Retorno:
            list[Medico]: copia de la lista de objetos Medico.
        """
        # Tomamos los valores del diccionario _medicos y devolvemos una copia de la lista
        return list(self.__medicos__.values())
