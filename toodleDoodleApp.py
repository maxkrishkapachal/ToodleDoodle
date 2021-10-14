allTasks = []
returnTasks = []

def newTask(newTaskName, newTaskDue, newTaskNotes):
  string = "\U0001F518 " + newTaskName + " - " + newTaskNotes + " - " + newTaskDue
  allTasks.append(string)

def deleteTask(taskNum):
  allTasks.pop(taskNum - 1)

def getTasks():
  del returnTasks[:] #clear the array
  counter = 1
  for sObj in allTasks: #cycle through all the strings
    count = str(counter)
    string = count + "  " + sObj
    returnTasks.append(string)
    counter += 1
  return returnTasks 

def checkTask(taskNum):
  allTasks[taskNum - 1] = allTasks[taskNum - 1].replace("\U0001F518", "\U00002705")