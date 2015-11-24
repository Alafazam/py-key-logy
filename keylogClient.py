# import pywin32
# import pythoncom 

# import pyHook

# import sys
import socket

from optparse import OptionParser

def OnKeyboardEvent():
    try:
        MESSAGE='Hello roadmap khan how are you these dayas'
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.sendto(MESSAGE, (options.server, options.port))
        return True
    except socket.error as e:
        sys.exit(1)
    except KeyboardInterrupt as e:
        sys.exit(1)


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-s", dest='server', default='127.0.0.1', help="name or IP address of server")
    parser.add_option("-p", dest='port', default=6666,type='int', help="port number")
    (options,args) = parser.parse_args()
    OnKeyboardEvent()
    # hm = pyHook.HookManager()
    # hm.KeyDown = OnKeyboardEvent
    # hm.HookKeyboard()
    # pythoncom.PumpMessages()