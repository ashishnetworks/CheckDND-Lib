import requests
import json
import sys


class DND():

    def check(self,number):
        self.number=number
        self.payload = {'mobiles':self.number}
        self.url = 'http://checkdnd.com/api/check_dnd_no_api.php?'
        try:
            self.res = requests.get(self.url, params=self.payload)
        except requests.exceptions.ConnectionError:
            return 1 # Error Occured while Connecting
        self.object = json.loads(self.res.content)  # this line converts string of json values into a real json object
        return self.object['msg_text'][self.number] # Status of the Query is Sent Here ( Y|N )
