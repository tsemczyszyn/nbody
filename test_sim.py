#!/usr/bin/env python

from nbody import *

sim = Simulation()

sim.create_body("Earth", 5.972e24, 6371000.0, (0,0,0), (0, 0, 0))
sim.create_body("Moon", 7.3477e22, 1737100.0, (370000000.0,5000,10000), (0, 0, 1023))
#sim.create_body("Moon", 10.3477e24, 1737100.0, (370000000.0,5000,10000), (0, 0, 1023))
sim.create_body("ISS", 450000.0, 108.0, (-6050182.17, 2264127.38, 2084710.53), (-58.855333, -5291.239085, 5550.782895))

b = list(sim.bodies)
