import time
import sys
import math
import SwervDrone

def main():
	print "Should be running"
	drone = SwervDrone()
	drone.obtainControl()
	drone.arm()


if __name__ == "__main__":
    main()

