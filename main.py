import pybullet as p
import pybullet_data as pd


def main():
    print("Welcome")

    p.connect(p.GUI)
    p.setAdditionalSearchPath(pd.getDataPath())
    p.setGravity(0, 0, -9.8)

    startOrient=p.getQuaternionFromEuler([0, 0, 0])

    field = p.loadURDF("plane.urdf")
    car = p.loadURDF("./formular_car/car.urdf", [0, 0, 0.1], startOrient)

    print(p.getNumJoints(car))
    for i in range(p.getNumJoints(car)):
        print(p.getJointInfo(car, i))

    while True:
        p.stepSimulation()

if __name__ == "__main__":
    main()