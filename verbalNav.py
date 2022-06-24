import libhousy

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

def turn(angle, direction):
    if direction == "left":
        spdmul = -1
    else:
        spdmul = 1 
    angle = angle * spdmul        
    
def main(robot: libhousy.robot):
    global running, dist, angle, direction, driveF
    #Here is where your recurring code will go
    if running:
        command = input("Type a command here").split(" ")
        if command[0] == "drive":
            dist = int(command[2])
            running = drive(dist)
        elif command[0] == "turn":
            angle = int(command[2])
            direction = command[1]
    if driveF:
        running = drive(robot, dist)
    else:
        running = turn()
        