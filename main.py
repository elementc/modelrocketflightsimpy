from sim.dynamics import Dynamics
from sim.earth import Earth
from sim.obj import Obj
from sim.util import Vector3


if __name__ == '__main__':
    # initialize the world
    dynamics = Dynamics(environment=Earth())

    # create a rock
    rock = Obj(Vector3(0,0,10), Vector3(0,0,0))
    dynamics.objects.append(rock)

    # simulate it falling for a second
    dynamics.printstatus()
    for i in range(10):
        dynamics.tick(0.1)
