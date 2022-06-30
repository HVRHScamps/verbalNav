# inclue code to help us talk to the robot
import libhousy

state = 0
goal = 0
# 0 = prompt user, 1 = driving, 2 = turning

def drive(robot, distance):
    done = 0
    if robot.lDriveEncoder.Get() >distance +5:
           robot.lDrive.Set(-0.3)
    
    elif robot.lDriveEncoder.Get() <distance -5:
        robot.lDrive.Set(0.3)
        
    else: 
        robot.lDrive.Set(0)
        done += 1

    if robot.rDriveEncoder.Get() >distance +5:
        robot.rDrive.Set(-0.3)

    elif robot.rDriveEncoder.Get() <distance -5:
        robot.rDrive.Set(0.3)
    else:
        robot.rDrive.Set(0)
        done += 1
    if done == 2:
        return True
    return False

def turn(robot, angle):
    return True
def main(robot: libhousy.robot):
    global goal, state
    # Here is where your recurring code will go
    if state == 0:
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
            if command[2] == "right":
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
        
   
