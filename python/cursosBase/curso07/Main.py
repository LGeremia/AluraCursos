from Document import Document
from Phones import Phones

cpf = Document.generate_document("01234567890")
print(cpf)

cnpj = Document.generate_document("33969298000100")
print(cnpj)

phone = Phones(49988423605)