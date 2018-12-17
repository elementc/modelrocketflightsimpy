from .obj import Obj


class Rocket(Obj):
    mass = 1.0  # kilogram
    engine_thrust = 0.5  # newtons
    last_zvel = 0
    touched_down = False

    def tick(self, time, dt):
        if time > 1.0 and time < 2.0:
            accel = self.engine_thrust / self.mass
            self.vel.z += accel/dt

        if self.vel.z <= 0 and self.last_zvel > 0:
            print("apogee: t=%fs, altitude = %f meters" % (time, self.pos.z))
        if self.vel.z == 0 and self.last_zvel < 0:
            print("touchdown: t=%fs, velocity = %f meters/sec" %
                  (time, self.last_zvel))
            self.touched_down = True
        self.last_zvel = self.vel.z
