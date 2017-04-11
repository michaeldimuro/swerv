#!/usr/bin/env python

from dji_sdk.dji_drone import DJIDrone
import dji_sdk.msg
#import somereel API
import time
import sys
import math

class SwervDrone:
	
    def __init__(self):
        self.drone = DJIDrone()
        self.obtainControl()
        self.arm()
        self.takeoff()

    def obtainControl(self):
        print "Obtaining Control"
        self.drone.request_sdk_permission_control()
        time.sleep(2)

    def releaseControl(self):
        self.drone.release_sdk_permission_control()
        time.sleep(2)

    def arm(self):
        print "Armed"
    	self.drone.arm_drone()
        time.sleep(10)

    def disarm(self):
    	self.drone.disarm_drone()
        time.sleep(2)

    def takeoff(self):
        print "Taking off"
    	self.drone.takeoff()

    def land(self):
    	self.drone.landing()

    def returnToHome():
    	self.drone.gohome()

    def navToLocation(self, latitude, longitude, altitude):
    	self.drone.global_position_navigation_send_request(latitude, longitude, altitude)