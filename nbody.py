#!/usr/bin/env python

from visual import *

#Ideas:
#Allow bodies to be selected from a menu and centered in the view
#Selected bodies can print their current keplerian elements
#Creation of bodies from TLEs
#Proper usage of time and synchronization with real world
#Better integrator
#Simulation in a thread so I can use ipython to manipulate


class Body(object):

    def __init__(self, name, mass, radius, position, v_initial):

        self.mass = mass
        self.radius = radius
        self.position = vector(position[0], position[1], position[2])
        self.velocity = vector(v_initial[0], v_initial[1], v_initial[2])
        self.name = name
        self.net_force = vector(0, 0, 0)

    def accum_force(self, fvector):
        self.net_force += fvector

    def clear_force(self):
        self.net_force = vector(0, 0, 0)


class Simulation(object):

    def __init__(self):
        self.bodies = []
        self.G = 6.67384e-11

    def create_body(self, name, mass, radius, position, v_initial):
        self.bodies.append(Body(name, mass, radius, position, v_initial))

    def newtonian(self, primary, other):

        r = other.position - primary.position

        F = ((self.G * primary.mass * other.mass)/r.mag**2)*r.norm()

        return F

    def start(self):

        rotation = 7.2921150e-5

        scene = display(title="N-Body Simulation")
        stars = materials.loadTGA("stars.tga")
        moon = materials.loadTGA("moon.tga")
        st_texture = materials.texture(data=stars, mapping='spherical')
        moon_texture = materials.texture(data=moon, mapping='spherical')

        body1 = self.bodies[0]
        body2 = self.bodies[1]
        body3 = self.bodies[2]
        skybox = sphere(pos=(0, 0, 0), radius=600000000, material=st_texture)
        sphere1 = sphere(pos=body1.position, radius=body1.radius,
                         make_trail=True, material=materials.BlueMarble)
        sphere2 = sphere(pos=body2.position, radius=body2.radius,
                         make_trail=True, material=moon_texture)
        sphere3 = sphere(pos=body3.position, radius=100000, color=color.green,
                         make_trail=True)

        while 1:
            rate(500)
            for b in self.bodies:
                #for i in [body for body in self.bodies if body is not b]:
                for i in self.bodies:
                    if b.name is not i.name:
                        b.accum_force(self.newtonian(b, i))

            for b in self.bodies:

                accel = (b.net_force.mag/b.mass)*b.net_force.norm()
                b.velocity += accel
                b.position += b.velocity
                b.clear_force()

            sphere1.pos = body1.position
            sphere1.rotate(angle=rotation, axis=(0, 1, 0), origin=sphere1.pos)
            sphere2.pos = body2.position
            sphere3.pos = body3.position
