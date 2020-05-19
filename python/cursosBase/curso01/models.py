class Perfil(object):
    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0 #faz com que mude o nome da várivael para uma outra aleatóriamente em todas as istâncias dela.

    def imprimir(self):
        print("nome: %s, telefone: %s, empresa: %s, curtidas: %s" % (self.nome, self.telefone, self.empresa, self.__curtidas))

    def curtir(self):
        self.__curtidas += 1

    def obter_curtidas(self):
        return self.__curtidas

    #@staticmethod faz com que não precise criar um prefil para poder acessar então o método
    @classmethod #faz com que não precise criar um prefil para poder acessar então o método e também dê de especificar
                #em qual classe será instanciado
    def gerar_perfils(classe, nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        perfils = []
        for linha in arquivo:
            valores = linha.split(',')
            perfils.append(classe(*valores))
        arquivo.close()
        return perfils

class Perfil_Vip(Perfil):
    def __init__(self, nome, telefone, empresa, apelido=' '):
        super(Perfil_Vip, self).__init__(nome, telefone, empresa)
        self.apelido = apelido

    def get_credit(self):
        return super(Perfil_Vip, self).obter_curtidas() * 10.
        
class Argumento_Invalido_Erro(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    def __str__(self):
        return repr(self.mensagem)

    
