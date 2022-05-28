from ryu.base import app_manager
from ryu.ofproto import ofproto_v1_3

from ryu.controller.controller import Datapath

from eventlet.green.socket import socket
from flask import Flask,jsonify


OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

print('start')  
app = Flask(__name__)
@app.route('/<name>')
def index(name):
        sock = socket()
        dp = Datapath(sock,('127.0.0.1', 57222))
        ofprotoT = dp.ofproto
        priorityT=407
        #matchT=OFPMatch({"in_port":1})
        instT={"type":"OUTPUT", "port":2}
        parserT=dp.ofproto_parser
        actionsT = [parserT.OFPActionOutput(ofprotoT.OFPP_CONTROLLER,
                                            ofprotoT.OFPCML_NO_BUFFER)]
        instT = [parserT.OFPInstructionActions(ofprotoT.OFPIT_APPLY_ACTIONS,
                                                actionsT)]
        print('hena')
        test=parserT.OFPFlowMod(datapath=dp, priority=priorityT, instructions=instT)
        dp.send_msg(test)
        print("flow added")
        return name
print('starting')
app.run()     
