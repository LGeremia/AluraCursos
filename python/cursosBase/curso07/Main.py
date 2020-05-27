from Document import Document
from Phones import Phones
from Dates import Dates

cpf = Document.generate_document("01234567890")
print(cpf)

cnpj = Document.generate_document("33969298000100")
print(cnpj)

phone = Phones(554988423605)
print(phone)

date = Dates()
print(date.week_day())
print(date.formated_create_moment)
print(date.create_time())