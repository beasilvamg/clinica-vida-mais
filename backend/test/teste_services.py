import unittest
from backend.models.paciente import Paciente
# Importa a função que será testada
from backend.services.estatisticas import gerar_relatoio_estatistico

class TestEstatisticasService(unittest.TestCase):

    def setUp(self):
        self.pacientes_teste = [        
        Paciente(nome="Joao", idade=20, telefone="(11) 99180-2110"),
        Paciente(nome="Maria", idade=30, telefone="(11) 99180-2110"),
        Paciente(nome="Pedro", idade=40, telefone="(11) 99180-2110")
    ]

    def test_relatorio_vazio(self):
        # Testa para retorna dados padrão quando a lista está vazia.
        resultado = gerar_relatoio_estatistico([])
        self.assertEqual(resultado["total_pacientes"], 0)
        self.assertEqual(resultado["media_idade"], 0.0)

    def test_relatorio_completo(self):
        # Testa se a média e totais são calculados corretamente.
        resultado = gerar_relatoio_estatistico(self.pacientes_teste)
        
        # 20 + 30 + 40 = 90. Média: 90 / 3 = 30.0
        self.assertEqual(resultado["total_pacientes"], 3)
        self.assertEqual(resultado["media_idade"], 30.0)
        self.assertEqual(resultado["mais_novo"], 20)
        self.assertEqual(resultado["mais_velho"], 40)

if __name__ == '__main__':
    unittest.main()