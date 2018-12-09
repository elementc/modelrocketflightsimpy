class Dynamics:
    def __init__(self, environment, tickiterations=50):
        self.tickiterations = tickiterations
        self.env = environment
        self.objects = []
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

    def tick(self, dt):
        self.time += dt
        for obj in self.objects:
            for i in range(self.tickiterations):
                # accelerate...
                obj.vel += self.env.gravity() * (dt / self.tickiterations)
                # translate
                obj.pos += obj.vel * (dt / self.tickiterations)
        self.printstatus()
