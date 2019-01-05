from .obj import Obj


class Rocket(Obj):
    mass = 0.987  # kilogram
    last_zvel = 0
    burn_start_time = -1
    is_thrusting = False
    touched_down = False
    apogee_reached = False
    second_burn_start = 7.137

    f15_tc = [(0.0,  0),
              (0.25, 12.5),
              (0.5,  25),
              (0.75, 16.5),
              (1.0,  16.5),
              (1.25, 15.0),
              (1.5,  14.5),
              (2.0,  14.5),
              (2.25, 14.25),
              (2.5,  14),
              (3.0,  13),
              (3.25, 13),
              (3.5,  0)]

    # todo:  linearly interpolate here instead.
    def _get_thrust_from_tc(self, time_in_curve, tc):
        i = 0
        while i+1 < len(tc) and tc[i+1][0] < time_in_curve:
            i = i + 1
        if time_in_curve > tc[-1][0]:
            self.is_thrusting = False
        return tc[i][1]

    def _apply_engine_thrust(self, time, dt):
        time_in_curve = time - self.burn_start_time
        thrust = self._get_thrust_from_tc(time_in_curve, self.f15_tc)
        accel = thrust / self.mass
        self.vel.z += accel * dt

    # todo: linearly interpolate out engine weights
    def tick(self, time, dt):
        if self.burn_start_time == -1:
            self. is_thrusting = True
            self.burn_start_time = time
        if time-dt < self.second_burn_start and time+dt >= self.second_burn_start:
            self.is_thrusting = True
            self.burn_start_time = time

        if self.is_thrusting:
            self._apply_engine_thrust(time, dt)

        if not self.apogee_reached and self.vel.z <= 0 and self.last_zvel > 0:
            print("apogee: t=%fs, altitude = %f meters" % (time, self.pos.z))
            self.apogee_reached = True
        if self.vel.z == 0 and self.last_zvel < 0:
            print("touchdown: t=%fs, velocity = %f meters/sec" %
                  (time, self.last_zvel))
            self.touched_down = True

        self.last_zvel = self.vel.z
