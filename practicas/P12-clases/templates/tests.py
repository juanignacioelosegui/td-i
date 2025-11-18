import unittest

from dataset_viajes import DatasetViajes

class DatasetViajesTest(unittest.TestCase):
    def setUp(self):
        self.dataset: DatasetViajes = DatasetViajes(
            usuarios_filename='test-usuarios-data.csv',
            viajes_filename='test-viajes-data.csv',
        )

    def test_sin_minutos_pedaleando(self):
        self.assertEqual(self.dataset.minutos_pedaleando(id_usuario=5), 0)

    def test_minutos_pedaleando_un_viaje(self):
        self.assertAlmostEqual(self.dataset.minutos_pedaleando(id_usuario=2), 18.33, places=2)

    def test_minutos_pedaleando_varios_viaje(self):
        self.assertAlmostEqual(self.dataset.minutos_pedaleando(id_usuario=1), 15, places=2)

    def test_promedio_con_persona_sin_viajes(self):
        self.assertAlmostEqual(self.dataset.minutos_promedio_para_edad(32), 7.5, places=2)

    def test_promedio_con_dos_personas(self):
        self.assertAlmostEqual(self.dataset.minutos_promedio_para_edad(54), 22, places=2)

    def test_promedio_con_una_persona(self):
        self.assertAlmostEqual(self.dataset.minutos_promedio_para_edad(20), 18.33, places=2)

    def test_promedio_con_edad_inexistente(self):
        self.assertAlmostEqual(self.dataset.minutos_promedio_para_edad(20), 18.33, places=2)


unittest.main()
