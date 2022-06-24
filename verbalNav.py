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

def turn(angle, direction):
    if direction == "left":
        spdmul = -1
    else:
        spdmul = 1 
    angle = angle * spdmul        
    
def main(robot: libhousy.robot):
    global forward
#Here is where your recurring code will go
    command = input("Type a command here").split(" ")
    if command[0] == "drive":
        dist = int(command[2])
        drive(dist)
    elif command[0] == "turn":
        angle = int(command[2])
        turn(angle, command[1]