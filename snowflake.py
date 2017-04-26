import time
from math import floor

'''
  Offset from Unix Epoch
  Unix Epoch : January 1 1970 00:00:00 GMT
  Epoch Offset : September 9 2001 12:13:00 GMT
'''

class SnowflakeGenerator:
  def __init__(self, datacenter_id, machine_id):
    self.epoch_offset = 1000210380000
    self.datacenter_id = datacenter_id
    self.machine_id = machine_id
    self.last_timestamp = self.getUnixTimestamp()
    self.sequence_number = 1

  def generateID(self):
    timestamp = int(self.getUnixTimestamp() - self.epoch_offset)
    sequence = self.getNextSequence(timestamp)
    self.last_timestamp = timestamp
    snowflake_id = (timestamp << 22) | (self.datacenter_id << 5) | (self.machine_id << 5) | (sequence << 12)
    return int(snowflake_id)

	def getUnixTimestamp(self):
		return floor(time.time() * 1000)

	def getNextSequence(self, timestamp):
		if self.last_timestamp == timestamp:
			self.sequence_number += 1
		else:
			self.sequence_number = 1
		return self.sequence_number