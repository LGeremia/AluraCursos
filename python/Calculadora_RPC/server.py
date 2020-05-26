from xmlrpc.server import SimpleXMLRPCServer

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def potentiation(x,y):
    return x ** y

def connection():
    return "Conexão realizada com sucesso!"


server.register_multicall_functions()
server.register_function(add, "add")
server.register_function(subtract, "subtract")
server.register_function(multiply, "multiply")
server.register_function(divide, "divide")
server.register_function(potentiation, "potentiation")
server.register_function(connection, "connection")
server.serve_forever()