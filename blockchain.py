import datetime
import hashlib
from block import *

class BlockChain:

  block = Block('Genesis')
  head = block
  maxNone = 2**32
  diff = 20 
  target = 2**(256-diff)

  def add(self, block):
      block.previousHash = self.block.hash()
      block.blockNo = self.block.blockNo + 1

      self.block.next = block
      self.block = self.block.next

  def mine(self, block):
      for n in range(self.maxNone):
          if int(block.hash(), 16) <= self.target:
            self.add(block)
            print("found block #" + str(block.blockNo))
            break
          else:
              block.nonce += 1

  chain = []


blockchain = BlockChain()

print("Mining...")
for n in range(20):
    blockchain.mine(Block("Block #" + str(n+1)))
input("<Press Any Key>")
print("Display our lair...")
while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next
