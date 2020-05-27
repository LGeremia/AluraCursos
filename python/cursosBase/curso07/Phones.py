import re

class Phones:
    def __init__(self, phone):
        if self.verify_phones(str(phone)):
            self._phone = phone
        else:
            raise ValueError("Número de telefone inválido!")
    
    def verify_phones(self, phone):
        template = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
        reply = re.findall(template, phone)
        if reply:
            return True
        else:
            return False