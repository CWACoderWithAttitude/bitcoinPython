import datetime
import hashlib

class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previousHash = 0x0
    timeStamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.blockNo).encode('utf-8')+
        str(self.data).encode('utf-8')+
        str(self.previousHash).encode('utf-8')+
        str(self.timeStamp).encode('utf-8')+
        str(self.nonce).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return str(self.blockNo) + '\n' + str(self.hash()) + '\n' + str(self.data) + '\n---------'
