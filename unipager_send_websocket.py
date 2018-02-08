import json
import pprint
import websocket
from websocket import create_connection
websocket.enableTrace(True)

ws = create_connection('ws://localhost:8055/')


########################################################################
# Switch Messagetype AlphaNum, Numeric
########################################################################

m_type = "AlphaNum"
#m_type = "Numeric"

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

ric = "1234567" 

text = "TESTNACHRICHT UEBER WEBSOCKET"


string_to_send = "{\"SendMessage\": {\"addr\": %s, \"data\": \"%s\", \"mtype\": \"%s\", \"func\": \"%s\"}}" % (ric, text, m_type, m_func)
print(string_to_send)
ws.send(string_to_send)
