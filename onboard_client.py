import time
import sys
import math
from SwervDrone import Drone

def main():
	print "Starting Application.."
	drone = Drone()
	drone.mission.execute(drone)
	print "-----------\nMission Success"


if __name__ == "__main__":
    main()

