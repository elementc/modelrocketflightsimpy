class Dynamics:
    def __init__(self, environment, elasticcollisions=False, logticks=False):
        self.env = environment
        self.logticks = logticks
        self.objects = []
        self.elasticcollisions = elasticcollisions
        self.time = 0.0
        if self.logticks:
            print('Dynamics initialized.')
            print('bounds: ', self.env.extents())
            print('f(gravity): ', self.env.gravity())

    def reset(self):
        for obj in self.objects:
            obj.reset()
        self.time = 0.0

    def printstatus(self):
        print('t = %fsec' % self.time)
        for i in range(len(self.objects)):
            print("\t[%d] %s" % (i, self.objects[i]))

    # prevent objects from leaving sim bounds
    def _clamp_to_bounds(self, obj):
        if self.env.extents()['minX'] is not None and\
           obj.pos.x < self.env.extents()['minX']:
            obj.pos.x = self.env.extents()['minX']
            if obj.vel.x < 0:
                if self.elasticcollisions:
                    # elastic collision preserves kinetic energy
                    obj.vel.x = -obj.vel.x
                else:
                    # inelastic collision just kinda stops
                    obj.vel.x = 0.0
        if self.env.extents()['maxX'] is not None and\
           obj.pos.x > self.env.extents()['maxX']:
            obj.pos.x = self.env.extents()['maxX']
            if obj.vel.x > 0:
                if self.elasticcollisions:
                    # elastic collision preserves kinetic energy
                    obj.vel.x = -obj.vel.x
                else:
                    # inelastic collision just kinda stops
                    obj.vel.x = 0.0
        if self.env.extents()['minY'] is not None and\
           obj.pos.y < self.env.extents()['minY']:
            obj.pos.y = self.env.extents()['minY']
            if obj.vel.y < 0:
                if self.elasticcollisions:
                    # elastic collision preserves kinetic energy
                    obj.vel.y = -obj.vel.y
                else:
                    # inelastic collision just kinda stops
                    obj.vel.y = 0.0
        if self.env.extents()['maxY'] is not None and\
           obj.pos.y > self.env.extents()['maxY']:
            obj.pos.y = self.env.extents()['maxY']
            if obj.vel.y > 0:
                if self.elasticcollisions:
                    # elastic collision preserves kinetic energy
                    obj.vel.y = -obj.vel.y
                else:
                    # inelastic collision just kinda stops
                    obj.vel.y = 0.0
        if self.env.extents()['minZ'] is not None and\
           obj.pos.z < self.env.extents()['minZ']:
            obj.pos.z = self.env.extents()['minZ']
            if obj.vel.z < 0:
                if self.elasticcollisions:
                    # elastic collision preserves kinetic energy
                    obj.vel.z = -obj.vel.z
                else:
                    # inelastic collision just kinda stops
                    obj.vel.z = 0.0
        if self.env.extents()['maxZ'] is not None and\
           obj.pos.z > self.env.extents()['maxZ']:
            obj.pos.z = self.env.extents()['maxZ']
            if obj.vel.z > 0:
                if self.elasticcollisions:
                    # elastic collision preserves kinetic energy
                    obj.vel.z = -obj.vel.z
                else:
                    # inelastic collision just kinda stops
                    obj.vel.z = 0.0

    def tick(self, dt, sample=None):
        self.time += dt
        # tick all objects
        for obj in self.objects:
            obj.tick(self.time, dt)

        # physically simulate all objects
        # todo: apply atmospheric drag here.
        for obj in self.objects:
            # accelerate...
            obj.vel += self.env.gravity() * dt
            # translate
            obj.pos += obj.vel * dt
            # clamp to bounds
            self._clamp_to_bounds(obj)

        if self.logticks:
            # print out the state of the world
            self.printstatus()
