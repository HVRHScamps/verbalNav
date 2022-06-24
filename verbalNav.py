from pkgutil import read_code
import libhousy
import time

running = False
dist = 0
angle = 0
direction = "Right"
driveF = True

#You can define helper functions here, make sure to but them *above* the main function
def drive(robot: libhousy.robot, distance: int):
    ok = 0
    if robot.rDriveEncoder.Get() < distance:
        robot.rDrive.Set(0.8)
    else:
        robot.rDrive.Set(0)
        ok += 1
    if robot.lDriveEncoder.Get() < distance:
        robot.lDrive.Set(0.8)
    else:
        robot.lDrive.Set(0)
        ok += 1
    if ok == 2:
        return True
    else:
        return False
def turn(robot, angle, direction):
    p = 0.01
    if direction == "left":
        spdmul = -1
    else:
        spdmul = 1 
    angle = angle * spdmul   
    if robot.sense_hat.get_yaw() > angle:
        error=robot.sense_hat.get_yaw()+angle
        speed= error * p
        if abs(speed)>1:
            speed = speed/abs(speed)
        robot.lDrive.Set(-speed)
        robot.rDrive.Set(speed)
        # stuff and things
    elif robot.sense_hat.get_yaw() < -angle: #overshot
        error=-angle-robot.sense_hat.get_yaw()
        speed= error * p
        if abs(speed)>1:
            speed = speed/abs(speed)
        robot.rDrive.Set(-speed)
        robot.lDrive.Set(speed)
    else:   
        robot.rDrive.Set(0)
        robot.lDrive.Set(0)
        return True
    if speed < 0.1:
        return True
    return False     
    
def main(robot: libhousy.robot):
    global running, dist, angle, direction, driveF
    #Here is where your recurring code will go
    if running:
        command = input("Type a command here: ").split(" ")
        robot.lDriveEncoder.Reset()
        time.sleep(0.1)
        robot.rDriveEncoder.Reset()
        time.sleep(0.1)
        if command[0] == "drive":
            dist = int(command[2])
            driveF = True
        elif command[0] == "turn":
            angle = int(command[2])
            driveF = False
            direction = command[1]
    if driveF:
        running = drive(robot, dist)
    else:
        running = turn(robot,angle,direction)
