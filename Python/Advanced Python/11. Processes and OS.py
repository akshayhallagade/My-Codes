import os
processid = os.getpid()
userID = os.getuid()
operatingSystem = os.uname()
print(processid)
print(userID)
print(operatingSystem)
