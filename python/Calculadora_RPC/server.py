import SimpleXMLRPCServer
from datetime import datetime

server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost", 8888))
server.register_instance(datetime)

server.serve_forever()

