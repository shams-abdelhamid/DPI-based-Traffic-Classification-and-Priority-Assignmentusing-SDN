from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller, RemoteController,OVSSwitch, Controller
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller, RemoteController,OVSSwitch, Controller
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.cli import CLI

arr = []
k=3
users=["shams","zeina","abdo"]
class Topology(Topo):
    print("Custom Topology Example.")
    def __init__(self,k):
        Topo.__init__(self)
        print ("Adding Switch")
        switch = self.addSwitch('s1')
        for x in range(k):
            print ("Adding Hosts")
            host = self.addHost(users[x])
            print(type(host))
            arr.append(host)
            print("Link host and switch.")
            self.addLink(host,switch)  


def performTest():
    print("hi")
    topo = Topology(k)
    net = Mininet(topo = topo,controller=lambda a: RemoteController(a, ip='127.0.0.1',port=6653))
    net.start()
    with open('hosts.txt',"w") as host:
        for it in range(k):
            hx = net.get(users[it]) 
            host.writelines(hx.MAC() + "\n")
    CLI(net)
        



if __name__=='__main__':
    #displaying more info 
    setLogLevel('info')
    print("h1")
    performTest()

topos= {
    'mytopo': Topology
}

#   performTest()