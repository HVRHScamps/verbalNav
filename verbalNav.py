import libhousy
#You can define helper functions here, make sure to but them *above* the main function
def drive(robot: libhousy.robot, distance: int):

        if robot.rDriveEncoder.Get() < distance:
            robot.rDrive.Set(0.8)

        else:
            robot.rDrive.Set(0)

        if robot.lDriveEncoder.Get() < distance:
            robot.lDrive.Set(0.8)

        else:
            robot.lDrive.Set(0)
def main(robot: libhousy.robot):
    #Here is where your recurring code will go
    robot.drive(robot)