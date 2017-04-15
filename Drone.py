#!/usr/bin/env python

#from dji_sdk.dji_drone import DJIDrone
#import dji_sdk.msg
#from MissionPlanner import Mission
import time
import sys
import math

class Drone:

	def __init__(self):
		print "Initializing Drone.."
		#self.drone = DJIDrone()
		self.mission = Mission(25, 15)

	def obtainControl(self):
		print "Obtaining Control.."
		#self.drone.request_sdk_permission_control()

	def releaseControl(self):
		print "Releasing Control"
		#self.drone.release_sdk_permission_control()

	def arm(self):
		print "Arming"
		#self.drone.arm_drone()

	def disarm(self):
		print "Disarming"
		#self.drone.disarm_drone()

	def takeoff(self):
		print "Taking Off"
		#self.drone.takeoff()

	def land(self):
		print "Landing"
		#self.drone.landing()

	def returnToHome():
		print "Returning to Home"
		#self.drone.gohome()

	def navToLocation(self, latitude, longitude, altitude):
		print "Navigating to New Location"
		#self.drone.global_position_navigation_send_request(latitude, longitude, altitude)
	
	def lowerHarness(self):
		print "Lowering Enclosure"
		#self.reel.lower()

	def raiseHarness(self):
		print "Raising Enclosure"
		#self.reel.raise()
