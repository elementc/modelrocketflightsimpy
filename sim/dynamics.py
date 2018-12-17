class Dynamics:
    def __init__(self, environment, elasticcollisions=False):
        self.env = environment
        self.objects = []
        self.elasticcollisions = elasticcollisions
        self.time = 0.0
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

    def tick(self, dt, sample=None):
        self.time += dt
        for obj in self.objects:
            # accelerate...
            obj.vel += self.env.gravity() * dt
            # translate
            obj.pos += obj.vel * dt

            # clamp to bounds
            # TODO: repeat for additional extents
            if obj.pos.z < self.env.extents()['minZ']:
                obj.pos.z = self.env.extents()['minZ']
                if obj.vel.z < 0:
                    if self.elasticcollisions:
                        # elastic collision preserves kinetic energy
                        obj.vel.z = -obj.vel.z
                    else:
                        # inelastic collision just kinda stops
                        obj.vel.z = 0

        if callable(sample):
            sample()
        self.printstatus()
