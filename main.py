from sim.dynamics import Dynamics
from sim.earth import Earth
from sim.objects.rocket import Rocket
from sim.util import Vector3
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # initialize the world
    dynamics = Dynamics(environment=Earth())

    # create a rock
    rocket = Rocket(Vector3(0, 0, 0), Vector3(0, 0, 0), "Falcon 0.9")
    dynamics.objects.append(rocket)

    # create lists to store data for later plotting
    time = []
    altitude = []
    velocity = []

    # create a function which gathers data for later plotting.
    def sample():
        time.append(dynamics.time)
        altitude.append(rocket.pos.z)
        velocity.append(rocket.vel.z)

    # liftoff is at 2 seconds. simulate until vehicle returns to the ground.
    while not rocket.touched_down:
        dynamics.tick(0.02)
        sample()

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

    # TODO: license.
