#!/usr/bin/env python

from nbody import *

sim = Simulation()

sim.create_body("Earth", 5.972e24, 6371000.0, (0,0,0), (0, 0, 0))
sim.create_body("Moon", 7.3477e22, 1737100.0, (-80564131.3, 396741241, -32710834.8), (-953.1708, -187.9949, -32.9456))
sim.create_body("ISS", 450000.0, 108.0, (-6050182.17, 2264127.38, 2084710.53), (-58.855333, -5291.239085, 5550.782895))

b = list(sim.bodies)
