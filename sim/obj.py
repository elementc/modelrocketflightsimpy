class Obj:
    """A physically simulated object. The class name 'Object' is overloaded in python so we use Obj to disambiguate."""
    def __init__(self, initPos, initVel, name="rock"):
        self.initPos = initPos
        self.initVel = initVel
        self.reset()
        self.name = name

    def reset(self):
        self.pos = self.initPos.copy()
        self.vel = self.initVel.copy()

    def __repr__(self):
        return str("%s: {position: %s, velocity: %s}" % (self.name, self.pos, self.vel))
