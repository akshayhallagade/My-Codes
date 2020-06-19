import time
import winsound
print("Made by Akshay Hallagade.")

def myalarm():
    try:
        myTime = list(map(int, input("Enter time in hr min sec\n").split()))
        if len(myTime) == 3:
            total_seconds = myTime[0]*60*60+myTime[1]*60+myTime[2]
            time.sleep(total_seconds)
            frequency = 2500
            duration = 1000
            winsound.Beep(frequency, duration)
        else:
            print("please enter time in correct format as mentioned\n")
            myalarm()
    except Exception as e:
        print("This is exception\n", e, "so!,please enter correct details.")
        myalarm()


myalarm()
