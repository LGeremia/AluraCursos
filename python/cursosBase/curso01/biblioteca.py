def invitation(name):
    final_part = len(name)
    initial_part = len(name) - 4
    part1 = name[0:4]
    part2 = name[initial_part:final_part]
    total = part1+" "+part2
    return total

def send(name):
    print("Enviando convite para: "+name)

def prepare(name):
    nome = invitation(name)
    send(nome)