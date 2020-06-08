from unittest import TestCase
from dominio import Usuario, Lance, Leilao, Avaliador

class TestAvaliador(TestCase):
    def test_avalia(self):
        leo = Usuario("Leo")
        lais = Usuario("Lais")

        lance_leo = Lance(leo, 100.00)
        lance_lais = Lance(lais, 150.0)

        leilao = Leilao("Celular")


        leilao.lances.append(lance_leo)
        leilao.lances.append(lance_lais)

        avaliador = Avaliador()

        avaliador.avalia(leilao)

        print(avaliador.maior_lance)
        print(avaliador.menor_lance)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

        