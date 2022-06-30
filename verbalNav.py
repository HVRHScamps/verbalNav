# inclue code to help us talk to the robot
import libhousy
import time
state = 0
goal = 0
# 0 = prompt user, 1 = driving, 2 = turning

def drive(robot, distance):
    done = 0
    if robot.lDriveEncoder.Get() >distance +3:
           robot.lDrive.Set(-0.3)
    
    elif robot.lDriveEncoder.Get() <distance -3:
        robot.lDrive.Set(0.3)
        
    else: 
        robot.lDrive.Set(0)
        done += 1

    if robot.rDriveEncoder.Get() >distance +3:
        robot.rDrive.Set(-0.3)

    elif robot.rDriveEncoder.Get() <distance -3:
        robot.rDrive.Set(0.3)
    else:
        robot.rDrive.Set(0)
        done += 1
    if done == 2:
        return True
    return False

def turn(robot, angle):
    if robot.sense_hat.get_yaw() > angle + 5:
        robot.lDrive.Set(-0.25)
        robot.rDrive.Set(0.25)
    elif robot.sense_hat.get_yaw() < angle - 5:
        robot.lDrive.Set(0.25)
        robot.rDrive.Set(-0.25)
    else:
        robot.lDrive.Set(0)
        robot.rDrive.Set(0)
        return True
    return False
def main(robot: libhousy.robot):
    global goal, state
    # Here is where your recurring code will go
    if state == 0:
        robot.control.putNumber("encRst", 5)  # reset navx
        while robot.control.getNumber("encRst", 1) != 0:
            time.sleep(0.05)  # wait for robo rio ack
        robot.control.putNumber("encRst", 6)  # reset both drivetrain encoders
        while robot.control.getNumber("encRst", 1) != 0:
            time.sleep(0.05)  # wait for robo rio ack
        command = input("Enter a command: ").split(" ")
        if command[0] == "drive":
            state = 1
            if command[1] == "forward":
                direction = 1
            else:
                direction = -1
            goal = int(command[2])*direction

        elif command[0] == "turn":
            state = 2
            if command[1] == "right":
                direction = 1
            else:
                direction = -1
            goal = int(command[2])*direction

        elif command[0] == "done":
            return libhousy.DONE
        else:
            print("Invalid input! try again.\n")
            state = 0
    elif state == 1:
        if drive(robot, goal):
            state = 0
    elif state == 2:
        if turn(robot,goal):
            state = 0
    else:
        state = 0
        
   
