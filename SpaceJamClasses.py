from direct.showbase.ShowBase import ShowBase
from CollideObjectBase import *
from direct.task import Task
from panda3d.core import *
    
class Universe(InverseSphereCollideObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Universe, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 0.9)
        self.modelNode.setPos(posVec) 
        self.modelNode.setScale (scaleVec)
        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath) 
        self.modelNode.setTexture(tex, 1)
    
    
class Planet(SphereCollideObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Planet, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 1)
        self.modelNode.setPos(posVec) 
        self.modelNode.setScale (scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath) 
        self.modelNode.setTexture(tex, 1)

        self.angle = 0

    def rotate(self, task):
        # Increment the angle
        self.angle += globalClock.getDt() * 20  # 20 degrees per second
        # Apply the rotation
        self.modelNode.setH(self.angle)
        return Task.cont

class Rock(SphereCollideObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Rock, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 1)
        self.modelNode.setPos(posVec) 
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath) 
        self.modelNode.setTexture(tex, 1)

class SpaceStation(CapsuleCollidableObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        # Adjust the collider's radius
        new_radius_top = 1
        new_radius_bottom = 11.7
        super(SpaceStation, self).__init__(loader, modelPath, parentNode, nodeName, 1, -1, new_radius_top, 1, -1, -5, new_radius_bottom)
        
        self.modelNode.setPos(posVec) 
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath) 
        self.modelNode.setTexture(tex, 1)

class Drone(SphereCollideObject):
    # How many drones have been spawned.
    droneCount = 0

    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Drone, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 2.5)
        self.modelNode.setPos(posVec) 
        self.modelNode.setScale (scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath) 
        self.modelNode.setTexture(tex, 1)

class Missile(SphereCollideObject):
    fireModels = {}
    cNodes = {}
    collisionSolids = {}
    Intervals = {}
    missileCount = 0

    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, posVec: Vec3, scaleVec: float = 1.0):
        super(Missile, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 3.0)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setPos(posVec)
        Missile.missileCount += 1
        Missile.fireModels[nodeName] = self.modelNode
        Missile.cNodes[nodeName] = self.collisionNode
        Missile.collisionSolids[nodeName] = self.collisionNode.node().getSolid(0)
        Missile.cNodes[nodeName].show()
        print("Fire torpedo #" + str(Missile.missileCount))
    