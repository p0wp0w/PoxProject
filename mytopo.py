# Import needed modules
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSController

TOPOS = {'MyTopo' : (lambda : MyTopo())}

# Define the topology
class MyTopo(Topo):
  def __init__(self):
    # Initialize topology
    Topo.__init__(self)

    # Switches
    s1 = self.addSwitch("s1")
    s2 = self.addSwitch("s2")
    s3 = self.addSwitch("s3")

    # Hosts
    h1 = self.addHost("h1")
    h2 = self.addHost("h2")
    h3 = self.addHost("h3")
    h4 = self.addHost("h4")
    h5 = self.addHost("h5")
    h6 = self.addHost("h6")

    # Connecting switches to hosts
    self.addLink(s1, h1)
    self.addLink(s1, h2)
    self.addLink(s1, s2)
    self.addLink(s2, h3)
    self.addLink(s2, h4)
    self.addLink(s2, s3)
    self.addLink(s3, h5)
    self.addLink(s3, h6)

# Deploying the network 
if __name__ == "__main__":
  topo = MyTopo()
  net = Mininet(topo = topo, controller = OVSController)
  net.start()
 # net.pingAll()
 # net.stop()
