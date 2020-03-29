# NGOC D TRAN
# IST 440 - 101
# TEAM PREP - DEVELOPMENT PHASE

## Mill operating program
import sys
import time
import numpy
import numpy as np
import Adafruit_DHT
import enum
import subprocess

recipe = input('Enter recipe: ')
raw_materials = input('Enter raw materials: ')
quality_checks = input('Enter quality checks: ')
process_duration = input('Enter process duration: ')

# Dummy code to trigger shell command according to the user input, may update later
subprocess.Popen("echo {} {} {} {}".format(recipe, raw_materials, quality_checks, process_duration), shell=True)
