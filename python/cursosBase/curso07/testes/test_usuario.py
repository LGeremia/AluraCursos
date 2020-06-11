import sys

sys.path.append('../src/leilao')

import dominio

from dominio import Usuario, Leilao
from excecoes import LanceInvalido
import pytest

@pytest.fixture
def leo():
    return Usuario('Leo', 100.0)

@pytest.fixture
def leilao():
    return Leilao("Celular")

def test_quando_usuario_der_um_lance_deve_subtrair_valor_da_carteira(leo,leilao):
    leo.propoe_lance(leilao, 50.0)
    assert leo.carteira == 50.0

def test_quando_valor_eh_menor_que_saldo_carteira_deve_permitir_lance(leo,leilao):
    leo.propoe_lance(leilao, 1.0)
    assert leo.carteira == 99.0

def test_quando_valor_eh_igual_que_saldo_carteira_deve_permitir_lance(leo,leilao):
    leo.propoe_lance(leilao, 100.0)
    assert leo.carteira == 0.0

def test_quando_valor_eh_maior_que_saldo_carteira_nao_deve_permitir_lance(leo,leilao):
    with pytest.raises(LanceInvalido):
        leo.propoe_lance(leilao, 101.0)
        assert leo.carteira == 100.0
