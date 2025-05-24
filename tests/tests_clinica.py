import unittest
from datetime import datetime, timedelta

from clinica import Clinica
from modelos.paciente import Paciente
from modelos.medico import Medico
from excepciones.excepciones import (
    PacienteNoExisteError,
    MedicoNoExisteError,
    TurnoDuplicadoError,
)

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("Juan Perez", "12345678", "01/01/1990")
        self.medico = Medico("Dr. House", "M001", "Diagnóstico")
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)

    def test_agendar_turno_exitoso(self):
        fecha = datetime.now() + timedelta(days=1)
        self.clinica.agendar_turno(self.paciente.obtener_dni(), self.medico.obtener_matricula(), fecha)
        turnos = self.clinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)
        self.assertEqual(turnos[0].obtener_fecha_hora(), fecha)

    def test_agendar_turno_paciente_inexistente(self):
        fecha = datetime.now() + timedelta(days=1)
        with self.assertRaises(PacienteNoExisteError):
            self.clinica.agendar_turno("00000000", self.medico.obtener_matricula(), fecha)

    def test_agendar_turno_medico_inexistente(self):
        fecha = datetime.now() + timedelta(days=1)
        with self.assertRaises(MedicoNoExisteError):
            self.clinica.agendar_turno(self.paciente.obtener_dni(), "M999", fecha)

    def test_agendar_turno_duplicado(self):
        fecha = datetime.now() + timedelta(days=1)
        self.clinica.agendar_turno(self.paciente.obtener_dni(), self.medico.obtener_matricula(), fecha)
        with self.assertRaises(TurnoDuplicadoError):
            self.clinica.agendar_turno(self.paciente.obtener_dni(), self.medico.obtener_matricula(), fecha)

    def test_emitir_receta_exitoso(self):
        medicamentos = ["MedA", "MedB"]
        self.clinica.emitir_receta(self.paciente.obtener_dni(), self.medico.obtener_matricula(), medicamentos)
        historia = self.clinica.obtener_historia_clinica(self.paciente.obtener_dni())
        recetas = historia.obtener_recetas()
        self.assertEqual(len(recetas), 1)
        self.assertListEqual(recetas[0]._medicamentos, medicamentos)

    def test_emitir_receta_paciente_inexistente(self):
        with self.assertRaises(PacienteNoExisteError):
            self.clinica.emitir_receta("00000000", self.medico.obtener_matricula(), ["MedA"])

    def test_emitir_receta_medico_inexistente(self):
        with self.assertRaises(MedicoNoExisteError):
            self.clinica.emitir_receta(self.paciente.obtener_dni(), "M999", ["MedA"])

    def test_obtener_historia_clinica_existe(self):
        fecha = datetime.now() + timedelta(days=1)
        self.clinica.agendar_turno(self.paciente.obtener_dni(), self.medico.obtener_matricula(), fecha)
        self.clinica.emitir_receta(self.paciente.obtener_dni(), self.medico.obtener_matricula(), ["MedA"])
        historia = self.clinica.obtener_historia_clinica(self.paciente.obtener_dni())
        turnos = historia.obtener_turnos()
        recetas = historia.obtener_recetas()
        self.assertEqual(len(turnos), 1)
        self.assertEqual(len(recetas), 1)

    def test_obtener_historia_clinica_no_existe(self):
        with self.assertRaises(PacienteNoExisteError):
            self.clinica.obtener_historia_clinica("00000000")

if __name__ == "__main__":
    unittest.main()

