# Simple Model Rocket Sim

I wrote this as an exercise, to duplicate a matlab/simulink physics sim used in a popular model rocket youtube series.

This is a python script which simulates physics. It mostly just simulates rocks falling, but the object class has a subclass called Rocket which has the ability to apply estes f15 thrust curves twice to rocks of varying weights. This is a "good enough" physics sim for model rocket evaluations.

## Layout
The sim/ directory contains code building blocks which are assembled into a usable simulation in the main.py file. 

sim/dynamics.py is the main physics simulation. It stores a set of objects, and translates their positions according to their current velocities. Once constructed, a Dynamics object exposes an objects list to which new objects can be added, as well as a function called tick(). You must supply a delta-t to tick(). Dynamics will then call the tick function on all objects it tracks, apply a gravitational acceleration to all objects, calculate the translation of each object, and return.

sim/earth.py provides environment classes, most importantly, Earth, which Dynamics will consume. This way, if one wishes to test with other gravitational constants, they could do so by writing a new Environmnet class.

sim/util.py provides a 3d vector class for 3d math. It has some operators implemented.

sim/objects/obj.py has the base object class. It doesn't do anything.

sim/objects/rocket.py has the rocket logic. it has a tick() function which is called by dynamics, which calculates thrusts to apply from up to two estes engines.

## main.py
This is my very simple "bring it all together" script. It creates a dynamics instance, creates a rocket, simulates the motion of the rocketuntil the rocket reports touchdown, then generates graphs of position, velocity, and acceleration.

Position and velocity graphs are generated directly from the simulation output, but the acceleration is caluclated from the velcity values made by the sim, and therefore is a little flaky at moments of impact. Thus, my instantaneous acceleration clamps to 20m/s^2 for graph legibility. It's still being simulated correctly, just a weakness in my probe() function that calculates accel.

The simulation itself is pure python3, but the graphs are made with matplotlib. You can install the appropriate packages by running pip install -r requirements.txt in the root of this directory.

## Example Outputs
```
Casey@picon MINGW64 ~/checkouts/modelrocketflightsimpy (master)
$ python main.py
apogee: t=5.351000s, altitude = 51.017962 meters
touchdown: t=10.685000s, velocity = -2.287473 meters/sec
Max g force: 2.040816g
Min g force: -1.000000g
```
![](/img/Figure_1.png)
![](/img/Figure_2.png)
![](/img/Figure_3.png)
![](/img/Figure_4.png)

## License
MIT Licensed. See LICENSE.md for details

## Contributing
Pull requests accepted. I generally work with the Collective Code Construction Contract: 
1) accept all PRs
2) give helpful feedback afterward
3) decline only PRs in bad faith

## Contact
cdoran2011@my.fit.edu
