import Drone
#import dji_sdk.msg
import time
import sys

class Mission:

	def __init__(self, pickupLocation, dropoffLocation):
		self.state = "NULL"
		self.pickupLocation = pickupLocation
		self.dropoffLocation = dropoffLocation

	def execute(self, drone):
		# Arm the Drone
		drone.obtainControl()
		drone.arm()
		
		# Vertical Takeoff to 300 feet
		drone.navToLocation(1, 2, 300)
		
		#Navigate to Pickup Location
		drone.navToLocation(2, 2, 3)
		
		drone.navToLocation(2, 3, 3)	# Descend to safe altitude
		
		# Deploy the harness
		drone.lowerHarness()
		
		# Recall the harness
		drone.raiseHarness()
		
		# Ascend to 300 feet
		drone.navToLocation(1, 2, 3)
		
		# Navigate to Dropoff Location
		drone.navToLocation(2, 2, 3)
		
		drone.navToLocation(2, 3, 3)	# Descend to safe altitude
		
		# Deploy the harness
		drone.lowerHarness()
		
		# Recall the Harness
		drone.raiseHarness()
		
		# Ascend to 300 feet
		drone.navToLocation(3, 3, 3)
		
		# Return to home
		drone.returnToHome()
