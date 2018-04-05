# UniPager-SendWebsocket
## Version 1: unipager_send_websocket.py
Original from dk4pa
Send local Message over Websocket connection.

Options are:

ric, text, m_type(AlphaNum or Numeric), m_func(Func0-3)

## Version 2: unipager_send_ng.py
* Password authentification implemented
* Command line arguments with default values

````
usage: unipager_send.py [-h] [--hostname HOSTNAME] [--port PORT]
                        [--password PASSWORD] [--ric RIC] [--type TYPE]
                        [--func FUNC] [--msg MSG] [--debug]

Send paging call direct via Unipager

optional arguments:
  -h, --help           show this help message and exit
  --hostname HOSTNAME  The host running Unipager, default localhost
  --port PORT          The port Unipager is listening, default 8055
  --password PASSWORD  The Unipager password, default empty
  --ric RIC            RIC to send the message to
  --type TYPE          0 = Numeric, 1 = Alphanumeric, default 1
  --func FUNC          Function Bits in POCSAG datagram, default 3
  --msg MSG            Message, if containing spaces: "TEXT WITH SPACES"
  --debug              Enable debug
````
