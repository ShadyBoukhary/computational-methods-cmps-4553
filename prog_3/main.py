# Shady Boukhary
# Computational methods
# Dr. Johnson
# 10/25/2019
# Fall 19
# Simple vpython program that puts earth and mars in orbit around the sun
# The values are not to scale

from vpython import *

sunRadius = 4                 
earthRadius = sunRadius * 0.2    
marsRadius = sunRadius * 0.4
programSpeed = 0.0008  
timestep = 0.001
k = 5.8

# create the Sun object
sun = sphere( radius = sunRadius, opacity = 0.7, emissive = True, texture = "http://i.imgur.com/yoEzbtg.jpg",
            vel = vector(0,0,0),
            acc = vector(0, 0, 0),
            pos = vector(0, 0, 0),
            mass = 1000,
            force = vector(0, 0, 0),
            make_trail = True)

# Add some sunlight to the sun object
sunlight = local_light( pos = vec(0,0,0), color=color.white )
more_sunlight = local_light( pos = vec(0,0,0), color=color.white )  # I found adding two lights was about right

# Create planets with textures
earth = sphere(radius = earthRadius, texture = "http://i.imgur.com/rhFu01b.jpg", flipx = False , shininess = 0.9,
               vel = vector(0, 0.45 , 0),
               pos = vector(30, 0, 0),
               mass = sun.mass / 33000,
               force = vector(0, 0, 0),
               make_trail=True)
earth.trail_color = color.blue

mars = sphere(radius = marsRadius, texture = "https://i.imgur.com/6uxNerY.jpg", flipx = False , shininess = 0.9,
               vel = vector(0, -0.7, 0),
               pos = vector(-15, 0, 0),
               mass = sun.mass / 33000,
               force = vector(0, 0, 0),
               make_trail=True)

mars.trail_color = color.orange
scene.camera.follow(sun)   
bodies = [sun, earth, mars]

while True:   
    rate(200)   
    # N-Body simulation
    for body in bodies:
        # Reset force
        body.force = vector(0, 0, 0)
        # Calculate total force
        for otherBody in bodies:
            if body is not otherBody:
                dist = vector(otherBody.pos.x - body.pos.x, otherBody.pos.y - body.pos.y, otherBody.pos.z - body.pos.z)
                r = sqrt(pow(dist.x, 2) + pow(dist.y, 2) + pow(dist.z, 2))
                gravitation = (k * body.mass * otherBody.mass) / pow(r, 3)
                body.force = body.force + dist * gravitation
    # Update planet positions
    for body in bodies:
        a = body.force / body.mass
        dt2 = timestep **2
        body.vel = body.vel + a * dt2
        body.pos = body.pos + body.vel * timestep + 0.5 * a * dt2
     
    # rotate planets around own axis
    earth.rotate (angle = radians(programSpeed * 360), axis = vec(0, 1, 0))   # rotate the earth 360 times per year
    sun.rotate (angle = radians(programSpeed * 16), axis = vec(0, 1, 0))     
    mars.rotate (angle = radians(programSpeed * 200), axis = vec(0, 1, 0))     
