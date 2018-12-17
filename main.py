from sim.dynamics import Dynamics
from sim.earth import Earth
from sim.obj import Obj
from sim.util import Vector3
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # initialize the world
    dynamics = Dynamics(environment=Earth())

    # create a rock
    rock = Obj(Vector3(0, 0, 10), Vector3(0, 0, 0))
    dynamics.objects.append(rock)

    # create lists to store data for later plotting
    time = []
    altitude = []
    velocity = []

    # create a function which gathers data for later plotting.
    def sample():
        time.append(dynamics.time)
        altitude.append(rock.pos.z)
        velocity.append(rock.vel.z)

    # simulate it falling for two seconds
    dynamics.printstatus()
    for i in range(20 * 50):
        dynamics.tick(0.1 / 50)
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
