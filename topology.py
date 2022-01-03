from mininet.TOPO import TOPO
from mininet.net import Mininet
from mininet.util import dumpNodeConnections

class Topology(Topo):
    def __init__(self,k=2):
        Topo.__init(self)
        switch = self.addSwitch('s1')
        for x in range(k):
            host = self.addHost('h%s' % (x + 1))
            self.addLink(host,switch)

def performTest():
    topo = Topology(k=2)
    net = Mininet(topo = topo)
    net.start()
    print "Displaying host information"
    dumpNodeConnections(net.hosts)
    print "Testing Network Connectivity"
    net.pingAll()
    # print "Checking Bandwidth between host h1 and host h2"
    # h1,h2 = net.get('h1','h2')
    # net.iperf((h1,h2))
    net.stop()


if __name__=='__main__':
    performTest()

topos= {
    'mytopo': custTopo
}