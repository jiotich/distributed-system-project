import socket
from Pyro5 import socketutil
from Pyro5 import nameserver
from Pyro5 import api
from Pyro5 import config
import time
import select

config.SERVERTYPE = "thread"

class NameServer():
    def __init__(self):
        self.HOSTNAME = socket.gethostname()
        self.IP_ADDRESS = socketutil.get_ip_address(None, workaround127=True)

    def start(self, port):
        
        #TODO: Verificar a necessidade de se lançar uma excessão 
        self.URI, self.daemon, self.broadcast = nameserver.start_ns(host=self.IP_ADDRESS, port=port)
        
        self.remote_object_daemon = api.Daemon(host=self.HOSTNAME)
        
        #print(f"PyRO {name}       URI: {self.server_uri}")
        #print(f"nameserver {name} URI: {self.URI}")


        #return [URI, daemon, broadcast, remote_object_daemon]
    
    def add_remote_object(self, remote_object, name):
        self.server_uri = self.remote_object_daemon.register(
            remote_object,
        )

        self.daemon.nameserver.register(
            name=name,
            uri=self.server_uri,
            safe=True
        )
        
        print(f"PyRO {name}       URI: {self.server_uri}")
        print(f"nameserver {name} URI: {self.URI}")
    
    def loop(self):
        while True:
            print(time.asctime(), "Waiting for requests...")
            # create sets of the socket objects we will be waiting on
            # (a set provides fast lookup compared to a list)
            nameserverSockets = set(self.daemon.sockets)
            pyroSockets = set(self.remote_object_daemon.sockets)
            rs = [self.broadcast]  # only the broadcast server is directly usable as a select() object
            rs.extend(nameserverSockets)
            rs.extend(pyroSockets)
            rs, _, _ = select.select(rs, [], [], 3)
            eventsForNameserver = []
            eventsForDaemon = []
            for s in rs:
                if s is self.broadcast:
                    print("Broadcast server received a request")
                    self.broadcast.processRequest()
                elif s in nameserverSockets:
                    eventsForNameserver.append(s)
                elif s in pyroSockets:
                    eventsForDaemon.append(s)
            if eventsForNameserver:
                print("Nameserver received a request")
                self.daemon.events(eventsForNameserver)
            if eventsForDaemon:
                print("Daemon received a request")
                self.remote_object_daemon.events(eventsForDaemon)
    