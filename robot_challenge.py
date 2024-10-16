North = '🠑⍐'
West = '⬅'   
South = '⍗🠓'
East = '➡'

Directions = ['NORTH','EAST','SOUTH','WEST']
DirectionIndex = 0

DataDic = {}

Placed = False


DirectionDic = {'NORTH':North,
'EAST':East,
'SOUTH':South,
'WEST':West}

# Create the table
x = 0

while x <= 5:
    
    y = 0
    while y <= 5:
        sr = str(x)+','+str(y)
        DataDic[sr] = '⬛'
        y += 1

    x +=1


def printOutput():
    x = 0
    y = 0
    printAll = ''
    
    while y <= 5:

        printLine = ''
        while x <= 5:
        
            printLine += DataDic[str(x)+','+str(y)]
            
            x += 1
            
        printAll += printLine + '\n'
        x = 0
        y += 1
        
    return printAll




CurrentDirection = 'NORTH'
CurrentCoords = '1,1'


def moveRobot(CurrentCoords,Direction):


    CurrentSplit = CurrentCoords.split(',')
    if Direction == 'WEST':
        MoveCoord = int(CurrentSplit[0])
        MoveCoord = str(MoveCoord +- 1) + ',' + str(CurrentSplit[1])
        
    elif Direction == 'SOUTH':        
        MoveCoord = int(CurrentSplit[1])
        MoveCoord =  str(CurrentSplit[0]) + ',' + str(MoveCoord + 1)
        
    elif Direction == 'NORTH':
        MoveCoord = int(CurrentSplit[1])
        MoveCoord =  str(CurrentSplit[0]) + ',' + str(MoveCoord - 1)
        
    else:
        MoveCoord = int(CurrentSplit[0])
        MoveCoord = str(MoveCoord + 1) + ',' + str(CurrentSplit[1])      
    

    if MoveCoord in DataDic:
        
        ChosenDirec = DirectionDic[Direction]
        DataDic[MoveCoord] = ChosenDirec
        return MoveCoord
    
    else:
        print('COORDINATE OUT OF RANGE')
        ChosenDirec = DirectionDic[Direction]
        DataDic[CurrentCoords] = ChosenDirec
        return CurrentCoords

    

print(printOutput())

while True:
    
    Command = input('Input Command: ')
    print()

    if 'PLACE' in Command.upper():

    
        if Placed == True:    
            DataDic[CurrentCoords] = '⬛'
        
        Command = Command.strip().split(' ')[1].split(',')
        if len(Command) < 3:
            print('PLEASE INCLUDE X,Y,DIRECTION IN THE COMMAND')
        else:
            CurrentCoords = Command[0]+','+Command[1] 
            if CurrentCoords in DataDic:
                DirectionIndex = Directions.index(Command[2].upper())
                DataDic[CurrentCoords] = DirectionDic[Command[2].upper()]
                Placed = True
            else:
                print('COORDINATE OUT OF RANGE')
                Placed = False

    elif Placed == True:
        
        if 'MOVE' in Command.upper():           
            DataDic[CurrentCoords] = '⬛'
            CurrentCoords = moveRobot(CurrentCoords,Directions[DirectionIndex])

        elif 'LEFT' in Command.upper():
            if DirectionIndex == 0:
                DirectionIndex = 3
            else:
                DirectionIndex -= 1

            DataDic[CurrentCoords] = DirectionDic[Directions[DirectionIndex]]
            
        elif 'RIGHT' in Command.upper():
            
            if DirectionIndex == 3:
                DirectionIndex = 0
            else:
                DirectionIndex += 1

            DataDic[CurrentCoords] = DirectionDic[Directions[DirectionIndex]]
        
        elif 'REPORT' in Command.upper():
            print(CurrentCoords+','+Directions[DirectionIndex]+'\n')
            
        else:
            print('INVALID COMMAND\n')

    elif Placed == False:
        print('Please place the robot first.\n')
        

        
    
    print(printOutput())



