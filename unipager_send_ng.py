#!/usr/bin/python
import json
import pprint
import websocket
import argparse

from websocket import create_connection

#DEBUG = False

parser = argparse.ArgumentParser(description='Set status LEDs')
parser.add_argument('--hostname', default='localhost',
                    help='The host running Unipager, default localhost')
parser.add_argument('--port', default='8055',
                    help='The port Unipager is listening, default 8055')
parser.add_argument('--password', default=None, type=str,
                    help='The Unipager password, default empty')
parser.add_argument('--ric', dest='ric', default=None, type=int,
                    help='RIC to send the message to')
parser.add_argument('--type', dest='type', default=1,
                    help='0 = Numeric, 1 = Alphanumeric, default 1')
parser.add_argument('--msg', dest='msg', default='',
                    help='Message')
#parser.add_argument('--debug', dest='debug', action='store_true',
#                    help='Enable debug')

args = parser.parse_args()
#DEBUG |= args.debug
#if DEBUG: print("Debug enabled")

hostname = args.hostname
port = args.port
ric = args.ric
type = args.type
msg = args.msg
password = args.password

if not msg:
        print('No message given, nothing to do')
        exit()
if not ric:
        print('No RIC given, nothing to do')
        exit()


#websocket.enableTrace(True)

ws = create_connection('ws://' + hostname + ":" + port + '/')


########################################################################
# Switch Messagetype AlphaNum, Numeric
########################################################################

if type == 0:
        m_type = "Numeric"
elif type == 1:
        m_type = "AlphaNum"
else:
        exit()

########################################################################
# Switch Messagefunction Func0, Func1, Func2, Func3
########################################################################

#m_func = "Func0"
#m_func = "Func1"
#m_func = "Func2"
m_func = "Func3"

########################################################################
# SendMessage with Variables
########################################################################

ws.send('{"Authenticate":"' + password + '"}')
string_to_send = "{\"SendMessage\": {\"addr\": %s, \"data\": \"%s\", \"mtype\": \"%s\", \"func\": \"%s\"}}" % (ric, msg, m_type, m_func)
#print(string_to_send)
ws.send(string_to_send)
