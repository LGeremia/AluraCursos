import xmlrpclib

server = xmlrpclib.ServerProxy("http://localhost:8888")

print server.now()