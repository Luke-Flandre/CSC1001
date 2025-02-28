lockers = [False] * 100#create a list of lockers, which are all locked 
for student in range(1, 101):#every one-hundred student 
    for locker in range(student - 1, 100, student):#the Nth student,changes every Nth locker from the Nth locker
        lockers[locker] = not lockers[locker]#change the lockers
for i in range(100):#every locker
    if lockers[i]:#if the locker's bool is True, it is opened, so it should be printed out
        print("Locker", i+1, "is open")

        