from django.test import TestCase


class EstudianteFormularioTests(TestCase):
    def test_formulario_permite_indicar_no_asistencia(self):
        response = self.client.get('/estudiantes/')
        html = response.content.decode('utf-8')

        self.assertEqual(response.status_code, 200)
        self.assertIn('name="asistencia"', html)
        self.assertIn('No asistió', html)
        self.assertIn('value="false"', html)
