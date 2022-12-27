__author__ = '@bsysop'
__date__ = '20221227'
__version__ = '0.1'
__description__ = """\
IP Logger is a Burp Extension that captures the actual external IP and store in a file called iplogger.json.
"""

from burp import IBurpExtender
import json
import urllib2
import datetime

class BurpExtender(IBurpExtender):
    def registerExtenderCallbacks( self, callbacks):
        
        url = "https://api.ipify.org?format=json"
        response = urllib2.urlopen(url)
        data = response.read()
        values = json.loads(data)
        ip = values["ip"]

        print ("Burp IP Logger loaded.")
        print ("Copyright (c) 2022 bsysop")
        print("Your actual IP is: "+ip)

        # Serializing date and IP.
        dict = {
            "date": str(datetime.datetime.now()),
            "ip": ip
        }
        json_object = json.dumps(dict, indent=4)
        
        # Writing to iplogger.json
        with open("iplogger.json", "a") as outfile:
            outfile.write(json_object + "\n")

        return