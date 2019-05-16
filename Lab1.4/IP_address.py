
from ipaddress import IPv4Network
import random


class IPv4RandomNetwork(IPv4Network):
  def __init__(self):
      self.network = random.randint(0x0B000000, 0xDF000000)
      self.prefix = random.randint(8, 24)
      IPv4Network.__init__(self, (self.network, self.prefix), strict=False)

  def key_value(self):

    return (int(self.network_address) + 2**32 * int(self.netmask))


L = []
for x in range(0, 120):
    net = IPv4RandomNetwork()
    L.append(net)

    def func_compare(x):
        q = int(x.network_address) + 2**32 * int(x.netmask)
        return (q)

    sorted (L, key = func_compare)
print (L, x)
