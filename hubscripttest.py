from pox.core import core
import pox.openflow.libopenflow_01 as of

class Hub (object):
  def __init__ (self, connection):
    self.connection = connection
    connection.addListeners(self)

  def _handle_PacketIn (self, event):
    packet = event.parsed  # deinfing packet as the event information (the packet)
   
    src_mac = packet.src # extracting the source and destination mac addresses.
    dst_mac = packet.dst
   
    flow = of.ofp_flow_mod() # creating a flow entry 
    flow.match = of.ofp_match(dl_dst=dst_mac, dl_src=src_mac)
    
    flow.actions.append(of.ofp_action_output(port = of.OFPP_ALL)) # setting the action for this flow to forward on every port.
   
    self.connection.send(flow) # send this flow to controller

def launch ():
  def start_switch (event):
    Hub(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)