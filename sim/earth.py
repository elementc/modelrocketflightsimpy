from .util import Vector3

class Environment:
    def extents():
        raise NotImplementedException()
    def gravity():
        raise NotImplementedException()


class Earth(Environment):
    def extents(self):
        """Returns a dict containing floats or Nones. Dynamics systems use these to determine physical simulation constraints.
           Format: {minX, miny, minz, maxX, maxY, maxZ}
           If a given key is None, the simulation will extend infinitely in that direction.
           Otherwise, the simulation stops at the bound indicated.
        """
        return dict(minX=None, minY=None, minZ=0.0, maxX=None, maxY=None, maxZ=None)
    def gravity(self):
        """Returns a vector3. Dynamics system use this to determine the passive force to apply constantly from the environment."""
        return Vector3(0,0,-9.8)
