import time

import pybullet as p
import pybullet_data as pd


def main():
    print("Welcome")

    p.connect(p.GUI)
    p.setAdditionalSearchPath(pd.getDataPath())
    p.setGravity(0, 0, -9.8)

    startPos=[0, 0, 1]
    startOrient=p.getQuaternionFromEuler([0, 0, 0])

    field = p.loadURDF("plane.urdf")
    car = p.loadURDF("./formular_car/car.urdf", startPos, startOrient)
    # car = p.loadURDF("test_car.urdf", [0, 0, 1], startOrient)

    print("<=========================================================>")
    print(f"car_joints : {p.getNumJoints(car)}")
    for i in range(p.getNumJoints(car)):
        print(p.getJointInfo(car, i))
    print("<=========================================================>")


    while True:
        p.stepSimulation()
        time.sleep(1/120)

if __name__ == "__main__":
    main()