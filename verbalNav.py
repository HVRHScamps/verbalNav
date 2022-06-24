import libhousy

forward = True
#You can define helper functions here, make sure to but them *above* the main function
def main(robot: libhousy.robot):
    global forward
    #Here is where your recurring code will go

    command = input("Type a command here").split(" ")
    if command[0] == "drive":
        
        dist = int(command[2])
        drive(dist)
    elif command[0] == "turn":
        angle = int(command[2])
        turn(angle, command[1])
        