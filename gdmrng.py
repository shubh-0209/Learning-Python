import time 
timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)

# hour = int(time.strftime('%H'))

hour = int(input("Enter Hour:"))
name = str(input("Enter your name:"))

if(hour>0 and hour<12):
    print("Good Morning " + name + "!")

elif(hour>=12 and hour<17):
    print("Good Afternoon " + name + "!")

elif(hour>=17 and hour<20):
    print("Good Evening " + name + "!")

else:
    print("Good Night " + name + "!")    