import re

class Phones:
    def __init__(self, phone):
        if self.verify_phones(str(phone)):
            self._phone = str(phone)
        else:
            raise ValueError("Número de telefone inválido!")

        self.format_phone()
    
    def verify_phones(self, phone):
        template = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        reply = re.findall(template, phone)
        if reply:
            return True
        else:
            return False

    def __str__(self):
        return self.format_phone()

    def format_phone(self):
        template = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        reply = re.search(template, self._phone)
        
        self._formated_number = "+{} ({}) {}-{}".format(
            reply.group(1), 
            reply.group(2), 
            reply.group(3),
            reply.group(4))
        return self._formated_number