from datetime import datetime
from clinica import Clinica
from modelos.paciente import Paciente
from modelos.medico import Medico
from excepciones.excepciones import (
    PacienteNoExisteError,
    MedicoNoExisteError,
    TurnoDuplicadoError
)

class CLI:

    def __init__(self):
        self._clinica = Clinica()

    def mostrar_menu(self):
        """
        Muestra el menú principal en bucle infinito hasta que el usuario
        seleccione la opción de salir. Cada opción invoca a un método privado
        que interactúa con la Clinica.
        """
        while True:
            print("\n--- Menú Clínica ---")
            print("1) Agregar paciente")
            print("2) Agregar médico")
            print("3) Agendar turno")
            print("4) Emitir receta")
            print("5) Ver historia clínica")
            print("6) Ver todos los turnos")
            print("7) Ver todos los pacientes")
            print("8) Ver todos los médicos")
            print("9) Salir")
            op = input("Opción: ").strip()

            # Mapeo claro de opciones a métodos, sin lógica de negocio aquí
            if op == "1":
                self._agregar_paciente()
            elif op == "2":
                self._agregar_medico()
            elif op == "3":
                self._agendar_turno()
            elif op == "4":
                self._emitir_receta()
            elif op == "5":
                self._ver_historia()
            elif op == "6":
                self._ver_turnos()
            elif op == "7":
                self._ver_pacientes()
            elif op == "8":
                self._ver_medicos()
            elif op == "9":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida.")  # Se valida la entrada mínima

    def _agregar_paciente(self):
        """
        Solicita datos de un paciente por consola y delega la creación
        a Clinica.agregar_paciente.
        Parámetros solicitados:
          - nombre: str
          - dni: str
          - fn:   str en formato dd/mm/aaaa
        """
        nombre = input("Nombre: ").strip()
        dni = input("DNI: ").strip()
        fn = input("F. Nac. (dd/mm/aaaa): ").strip()
        paciente = Paciente(nombre, dni, fn)
        # La validación de duplicados o formato de datos recae en Clinica
        self._clinica.agregar_paciente(paciente)
        print("Paciente registrado.")

    def _agregar_medico(self):
        """
        Solicita datos de un médico por consola y delega la creación
        a Clinica.agregar_medico.
        Parámetros solicitados:
          - nombre: str
          - mat:    str matrícula
          - esp:    str especialidad
        """
        nombre = input("Nombre: ").strip()
        mat = input("Matrícula: ").strip()
        esp = input("Especialidad: ").strip()
        medico = Medico(nombre, mat, esp)
        self._clinica.agregar_medico(medico)
        print("Médico registrado.")

    def _agendar_turno(self):
        """
        Solicita los datos necesarios para agendar un turno:
          - dni: str DNI del paciente
          - mat: str matrícula del médico
          - fs:  str fecha y hora en formato dd/mm/aaaa HH:MM
        Intenta parsear la fecha, luego llama a Clinica.agendar_turno.
        Captura:
          - ValueError si el formato de fecha es incorrecto.
          - PacienteNoExisteError, MedicoNoExisteError, TurnoDuplicadoError
            si hay problema de negocio.
        """
        dni = input("DNI paciente: ").strip()
        mat = input("Matrícula médico: ").strip()
        fs = input("Fecha y hora (dd/mm/aaaa HH:MM): ").strip()
        try:
            fh = datetime.strptime(fs, "%d/%m/%Y %H:%M")
            self._clinica.agendar_turno(dni, mat, fh)
            print("Turno agendado.")
        except ValueError:
            # Error de parseo de fecha
            print("Formato de fecha inválido.")
        except (PacienteNoExisteError, MedicoNoExisteError, TurnoDuplicadoError) as e:
            # Errores de negocio delegados
            print("Error:", e)

    def _emitir_receta(self):
        """
        Solicita los datos necesarios para emitir una receta:
          - dni: str DNI del paciente
          - mat: str matrícula del médico
          - meds: lista de medicamentos (cadena separada por comas)
        Llama a Clinica.emitir_receta y captura errores de negocio.
        """
        dni = input("DNI paciente: ").strip()
        mat = input("Matrícula médico: ").strip()
        meds_input = input("Medicamentos (coma-sep): ").strip()
        # Convertimos la cadena en lista y limpiamos espacios
        medicamentos = [m.strip() for m in meds_input.split(',') if m.strip()]
        try:
            self._clinica.emitir_receta(dni, mat, medicamentos)
            print("Receta emitida.")
        except (PacienteNoExisteError, MedicoNoExisteError) as e:
            print("Error:", e)

    def _ver_historia(self):
        """
        Solicita el DNI de un paciente y muestra su historia clínica completa
        (turnos y recetas). Captura PacienteNoExisteError si no se encuentra.
        """
        dni = input("DNI paciente: ").strip()
        try:
            historia = self._clinica.obtener_historia_clinica(dni)
            print(historia)  # HistoriaClinica implementa __str__
        except PacienteNoExisteError as e:
            print("Error:", e)

    def _ver_turnos(self):
        """
        Muestra todos los turnos agendados. Si no hay ningún turno,
        informa al usuario en pantalla.
        """
        turnos = self._clinica.obtener_turnos()
        if not turnos:
            print("No hay turnos.")
        else:
            for turno in turnos:
                print(turno)

    def _ver_pacientes(self):
        """
        Muestra todos los pacientes registrados. Requiere que la clase Clinica
        tenga un método obtener_pacientes() que devuelva lista de Paciente.
        """
        pacientes = self._clinica.obtener_pacientes()
        if not pacientes:
            print("No hay pacientes.")
        else:
            for paciente in pacientes:
                print(paciente)

    def _ver_medicos(self):
        """
        Muestra todos los médicos registrados. Requiere que la clase Clinica
        tenga un método obtener_medicos() que devuelva lista de Medico.
        """
        medicos = self._clinica.obtener_medicos()
        if not medicos:
            print("No hay médicos.")
        else:
            for medico in medicos:
                print(medico)

if __name__ == "__main__":
    cli = CLI()
    cli.mostrar_menu()
