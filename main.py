from sim.dynamics import Dynamics
from sim.earth import Earth
from sim.objects.rocket import Rocket
from sim.util import Vector3
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # initialize the world
    dynamics = Dynamics(environment=Earth())

    # create a rocket and have it obey physics
    rocket = Rocket(
        initPos=Vector3(0, 0, 0), # initial position at 0, 0, 0
        initVel=Vector3(0, 0, 0), # not moving at start of sim
        name="Heracles 1-X"
        )
    dynamics.objects.append(rocket)
    
    # the resolution of our simulation, time-wise
    dt = 0.01

    # create lists to store data for later plotting
    time = []
    altitude = []
    velocity = []
    instantAccel = [0,] # instantaneous acceleration, must be seeded with a zero

    # create a function which gathers data for later plotting.
    def sample():
        time.append(dynamics.time)
        altitude.append(rocket.pos.z)
        velocity.append(rocket.vel.z)
        if len(velocity) > 1: # instantaneous acceleration can't be calculated until we have current and last velocities
            instantAccel.append((velocity[-1] - velocity[-2]) / dt)

    # liftoff is at 2 seconds. simulate until vehicle returns to the ground.
    while not rocket.touched_down:
        dynamics.tick(dt)
        sample()

    print("max g force: %fg\nmin g force: %fg" % (max(instantAccel) / 9.8, min(instantAccel) / 9.8))
    dynamics.tick(dt)
    # chart position vs time
    plt.plot(time, altitude)
    plt.xlabel('time, seconds')
    plt.ylabel('altitude, meters')
    plt.title("Vehicle Altitude")
    plt.show()

    # chart velocity vs time
    plt.plot(time, velocity)
    plt.xlabel('time, seconds')
    plt.ylabel('velocity, m/s')
    plt.title("Vehicle Velocity")
    plt.show()
    
    # chart acceleration vs time
    plt.plot(time, instantAccel)
    plt.xlabel('time, seconds')
    plt.ylabel('acceleration, m/s^2')
    plt.title("Vehicle Acceleration")
    plt.show()
