from mininet.TOPO import TOPO
from mininet.net import Mininet
from mininet.node import RemoteController,OVSSwitch
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.util import dumpNodeConnections

class Topology(Topo):
    print("Custom Topology Example.")
    def __init__(self,k=2):
        Topo.__init(self)
        print "Adding Switch"
        switch = self.addSwitch('s1')
        for x in range(k):
            print "Adding Hosts"
            host = self.addHost('h%s' % (x + 1))
            print("Link host and switch.")
            self.addLink(host,switch)

def performTest():
    topo = Topology(k=2)
    net = Mininet(topo = topo,controller=lambda name: RemoteController(name,ip='192.168.1.50',port=6633, switch=OVSSwitch))
    net.start()
    print "Displaying host information"
    dumpNodeConnections(net.hosts)
    print "Testing Network Connectivity"
    net.pingAll()
    print "Checking Bandwidth between host h1 and host h2"
    h1,h2 = net.get('h1','h2')
    net.iperf((h1,h2))
    net.stop()


if __name__=='__main__':
    #displaying more info 
    setLogLevel('info')
    performTest()

topos= {
    'mytopo': custTopo
}