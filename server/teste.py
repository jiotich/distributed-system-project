import sys
sys.dont_write_bytecode = True

import Pyro5
from Pyro5.api import Proxy

#ns = Pyro5.api.locate_ns(host="JDBOP", port=9090)
#uri = ns

with Proxy("PYRONAME:user_remote_object") as proxy:
    print(proxy.test1(2, 2))
    
with Proxy("PYRONAME:post_remote_object") as proxy:
    print(proxy.test2(2, 2))
