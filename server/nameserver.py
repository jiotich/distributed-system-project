import socket
from Pyro5 import socketutil
from Pyro5 import nameserver
from Pyro5 import api

class NameServer():
    def __init__(self):
        self.HOSTNAME = socket.gethostname()
        self.IP_ADDRESS = socketutil.get_ip_address(None, workaround127=True)

    def start(self, remote_object, name, port):
        
        #TODO: Verificar a necessidade de se lançar uma excessão 
        URI, daemon, broadcast = nameserver.start_ns(host=self.IP_ADDRESS)
        
        remote_object_daemon = api.Daemon(host=self.HOSTNAME)

        server_uri = remote_object_daemon.register(
            remote_object,
        )

        daemon.nameserver.register(
            name=name,
            uri=server_uri,
            safe=True
        )

        print(f"PyRO {name}       URI: {server_uri}")
        print(f"nameserver {name} URI: {URI}")


        return remote_object_daemon
    