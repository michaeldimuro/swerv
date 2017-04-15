import sys
import time

class ReelMotor:
	
	def __init__(self):
		self.state = "Ready"
	
	def lowerEnclosure(self):
		print "Lowering enclosure"
		self.spinMotor('d', 500)
	
	def raiseEnclosure(self):
		print "Raising enclosure"
		self.spinMotor('u', 500)
