from .obj import Obj


class Rocket(Obj):
    mass = 1.0  # kilogram
    engine_thrust = 0.5  # newtons

    def tick(self, time, dt):
        if time > 1.0 and time < 2.0:
            accel = self.engine_thrust / self.mass
            self.vel.z += accel/dt
