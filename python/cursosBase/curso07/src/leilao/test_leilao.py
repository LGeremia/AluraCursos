from unittest import TestCase
from dominio import Usuario, Lance, Leilao

class TestLeilao(TestCase):

    def setUp(self):
        self.leo = Usuario("Leo")

        self.lance_leo = Lance(self.leo, 100.00)

        self.leilao = Leilao("Celular")

    def test_quando_adicionado_lances_ordem_crescente_deve_retornar_maior_e_menor_valor_do_lance(self):
        lais = Usuario("Lais")
        lance_lais = Lance(lais, 150.0)
        self.leilao.propoe(self.lance_leo)
        self.leilao.propoe(lance_lais)

        print(self.leilao.maior_lance)
        print(self.leilao.menor_lance)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_quando_adicionado_lances_ordem_decrescente_nao_deve_permitir_propor_lance(self):
        with self.assertRaises(ValueError):
            lais = Usuario("Lais")
            lance_lais = Lance(lais, 150.0)
            self.leilao.propoe(lance_lais)
            self.leilao.propoe(self.lance_leo)

            print(self.leilao.maior_lance)
            print(self.leilao.menor_lance)

            menor_valor_esperado = 100.0
            maior_valor_esperado = 150.0

            self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
            self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_quando_adicionado_apenas_um_lance_deve_retornar_o_mesmo_valor_de_maior_e_menor_lance(self):
        self.leilao.propoe(self.lance_leo)

        print(self.leilao.maior_lance)
        print(self.leilao.menor_lance)

        menor_valor_esperado = 150.0
        maior_valor_esperado = 150.0

    def test_quando_adicionado_tres_lances_deve_retornar_maior_e_menor_valor_do_lance(self):
        lais = Usuario("Lais")
        lance_lais = Lance(lais, 150.0)
        leona = Usuario("Leona")

        self.lance_leo = Lance(self.leo, 100.00)
        lance_leona = Lance(leona, 200.0)
        lance_lais = Lance(lais, 150.0)


        self.leilao.propoe(self.lance_leo)
        self.leilao.propoe(lance_lais)
        self.leilao.propoe(lance_leona)


        print(self.leilao.maior_lance)
        print(self.leilao.menor_lance)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_quando_nao_tiver_lances_deve_permitir_lances(self):
        self.leilao.propoe(self.lance_leo)

        quantidade_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_lances_recebido)

    def test_quando_ultimo_usuario_for_diferente_deve_permitir_lance(self):
        lais = Usuario("Lais")
        lance_lais = Lance(lais, 150.0)

        self.leilao.propoe(self.lance_leo)
        self.leilao.propoe(lance_lais)

        quantidade_lances_recebido = len(self.leilao.lances)
        self.assertEqual(2, quantidade_lances_recebido)


    def test_quando_ultimo_usuario_for_igual_nao_deve_permitir_lance(self):
        lance_leo_200 = Lance(self.leo, 200)

        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_leo)
            self.leilao.propoe(lance_leo_200)

'''
    def test_quando_lance_for_maior_que_ultimo_deve_permitir_lance(self):
        pass

    def test_quando_lance_for_menor_que_ultimo_nao_deve_permitir_lance(self):
        pass
'''
