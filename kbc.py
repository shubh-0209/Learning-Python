ques = [
    ['What does OS stand for?','Operational Software','Operating System','Open Software','Operating Solution',2],    
    ['What does OS stand for?','Operational Software','Operating System','Open Software','Operating Solution',2],
    ['What does OS stand for?','Operational Software','Operating System','Open Software','Operating Solution',2],
    ['What does OS stand for?','Operational Software','Operating System','Open Software','Operating Solution',2],
    ['What does OS stand for?','Operational Software','Operating System','Open Software','Operating Solution',2],
    ['What does OS stand for?','Operational Software','Operating System','Open Software','Operating Solution',2],
    ['What does OS stand for?','Operational Software','Operating System','Open Software','Operating Solution',2],
    ["What does OS stand for?","Operational Software",'Operating System','Open Software','Operating Solution',2],
    ['What does OS stand for?','Operational Software','Operating System','Open Software','Operating Solution',2],
    ['What does OS stand for?','Operational Software','Operating System','Open Software','Operating Solution',2]
]
total = 0

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

for i in range(0, len(ques)):
    print(f"Question for Rs.{levels[i]}")
    print(f"1.{ques[1][1]}                2.{ques[1][2]}")
    print(f"3.{ques[1][3]}                4.{ques[1][4]}")

    reply = int(input("Enter your answer(1-4):"))

    if(reply == ques[1][-1]):
        print(f"Correct Answer. You have won Rs.{levels[i]}")

        if(i==4):
           money = 10000
        elif(i==9):
            money = 320000

    else:
        print("Wrong Answer!")       
        break 