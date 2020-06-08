

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu o lance de: {lance.valor}')

avaliador = Avaliador()

avaliador.avalia(leilao)

print(avaliador.maior_lance)
print(avaliador.menor_lance)