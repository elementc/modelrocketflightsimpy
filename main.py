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
        name="Artesia 1-X"
        )
    dynamics.objects.append(rocket)
    
    # the resolution of our simulation, time-wise
    dt = 0.001

    # create lists to store data for later plotting
    time = []
    altitude = []
    velocity = []
    instant_acceleration = [0,] # instantaneous acceleration, must be seeded with a zero

    # create a function which gathers data for later plotting.
    def sample():
        time.append(dynamics.time)
        altitude.append(rocket.pos.z)
        velocity.append(rocket.vel.z)
        if len(velocity) > 1: # instantaneous acceleration can't be calculated until we have current and last velocities
            instant_acceleration.append((velocity[-1] - velocity[-2]) / dt)
            # accel calculations break down and get very large at collisions. clamp to 20m/s^2
            if instant_acceleration[-1] > 20.0:
                instant_acceleration[-1] = 20

    # simulate until vehicle returns to the ground.
    while not rocket.touched_down:
        dynamics.tick(dt)
        sample()

    print("Max g force: %fg\nMin g force: %fg" % (max(instant_acceleration) / 9.8, min(instant_acceleration) / 9.8))
    # # chart position vs time
    plt.plot(time, altitude)
    plt.xlabel('time, seconds')
    plt.ylabel('altitude, meters')
    plt.title("Vehicle Altitude")
    plt.show()

    # # chart velocity vs time
    plt.plot(time, velocity)
    plt.xlabel('time, seconds')
    plt.ylabel('velocity, m/s')
    plt.title("Vehicle Velocity")
    plt.show()
    
    # # chart acceleration vs time
    plt.plot(time, instant_acceleration)
    plt.xlabel('time, seconds')
    plt.ylabel('acceleration, m/s^2')
    plt.title("Vehicle Acceleration")
    plt.show()
        
    # chart acceleration vs time
    fig, ax1 = plt.subplots()
    ax1.set_xlabel('time, seconds')
    ax1.set_ylabel('acceleration, m/s^2', color='red')
    ax1.plot(time, instant_acceleration, color='red')
    plt.title("Velocity vs Acceleration")
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    ax2.set_ylabel('velocity, m/s', color='blue')
    ax2.plot(time, velocity, color='blue')
    plt.show()
