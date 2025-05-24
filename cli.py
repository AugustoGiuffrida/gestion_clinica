from datetime import datetime
from clinica import Clinica
from modelos.paciente import Paciente
from modelos.medico import Medico
from excepciones.excepciones import PacienteNoExisteError, MedicoNoExisteError, TurnoDuplicadoError

class CLI:
    def __init__(self):
        self._clinica = Clinica()

    def mostrar_menu(self):
        while True:
            print("\n--- Menú Clínica ---")
            print("1) Agregar paciente")
            print("2) Agregar médico")
            print("3) Agendar turno")
            print("4) Emitir receta")
            print("5) Ver historia clínica")
            print("6) Ver todos los turnos")
            print("7) Salir")
            op = input("Opción: ")
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
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida.")

    def _agregar_paciente(self):
        nombre = input("Nombre: ")
        dni = input("DNI: ")
        fn = input("F. Nac. (dd/mm/aaaa): ")
        p = Paciente(nombre, dni, fn)
        self._clinica.agregar_paciente(p)
        print("Paciente registrado.")

    def _agregar_medico(self):
        nombre = input("Nombre: ")
        mat = input("Matrícula: ")
        esp = input("Especialidad: ")
        m = Medico(nombre, mat, esp)
        self._clinica.agregar_medico(m)
        print("Médico registrado.")

    def _agendar_turno(self):
        dni = input("DNI paciente: ")
        mat = input("Matrícula médico: ")
        fs = input("Fecha y hora (dd/mm/aaaa HH:MM): ")
        try:
            fh = datetime.strptime(fs, "%d/%m/%Y %H:%M")
            self._clinica.agendar_turno(dni, mat, fh)
            print("Turno agendado.")
        except ValueError:
            print("Formato de fecha inválido.")
        except (PacienteNoExisteError, MedicoNoExisteError, TurnoDuplicadoError) as e:
            print("Error:", e)

    def _emitir_receta(self):
        dni = input("DNI paciente: ")
        mat = input("Matrícula médico: ")
        meds = input("Medicamentos (coma-sep): ").split(',')
        meds = [m.strip() for m in meds]
        try:
            self._clinica.emitir_receta(dni, mat, meds)
            print("Receta emitida.")
        except (PacienteNoExisteError, MedicoNoExisteError) as e:
            print("Error:", e)

    def _ver_historia(self):
        dni = input("DNI paciente: ")
        try:
            hist = self._clinica.obtener_historia_clinica(dni)
            print(hist)
        except PacienteNoExisteError as e:
            print("Error:", e)

    def _ver_turnos(self):
        turnos = self._clinica.obtener_turnos()
        if not turnos:
            print("No hay turnos.")
        else:
            for t in turnos:
                print(t)

if __name__ == "__main__":
    CLI().mostrar_menu()
