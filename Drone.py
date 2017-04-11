#!/usr/bin/env python

from dji_sdk.dji_drone import DJIDrone
import dji_sdk.msg
import time
import sys
import math

class SwervDrone:

		def __init__(self):
			self.drone = DJIDrone()
			self.reel = SwervReel()
			self.drone.request_sdk_permission_control()

        def arm(self):
        	self.drone.arm_drone()

        def disarm(self):
        	self.drone.disarm_drone()

        def takeoff(self):
        	self.drone.takeoff()

        def land(self):
        	self.drone.landing()

        def returnToHome():
        	self.drone.gohome()

        def navToLocation(self, latitude, longitude, altitude):
        	self.drone.global_position_navigation_send_request(latitude, longitude, altitude)

        def loiter(self):
        


    	#Methods for reel system

    	def lowerHarness(self):
    		#self.reel.lower()

    	def raiseHarness(self):
    		#self.reel.raise()