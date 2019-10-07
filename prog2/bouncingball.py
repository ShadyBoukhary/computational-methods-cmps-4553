from vpython import *
#GlowScript 2.9 VPython

# Shady Boukhary
# Computational Methods
# Fall 19
# Dr. Johnson

scene.range = 15
scene.camera.pos = vector(7, 0, 25)
scene.forward = vector(3, -1, -2)

g = 9.8       # gravity
r = 0.2         


floor = box(pos = vector(-3, 0, 0),
            width = 8,
            length = 8,
            height = 0.05,
            color = color.blue)
            
# Start ball with acceleration = -g
ball = sphere(pos = vector(-3, 5, 0),
              radius = 0.7 * r,
              color = color.red,
              vel = vector(0,0,0),
              acc = vector(0, -g, 0))



t = 0       # t(0)
dt = 0.01   # time step 

while t <= 15:
    rate(100)
    ball.vel = ball.vel + ball.acc * dt
    ball.pos = ball.pos + ball.vel * dt + 0.5 * ball.acc * dt * dt
    t = t + dt
    # Flip and reduce velocity when hitting floor
    if ball.pos.y <= r:
        ball.vel.y =  - 0.8*ball.vel.y
        ball.pos.y = r
