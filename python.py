print("this is my prsctice day of python khan ")

# comp=int(input("please inter the number:"))
# print(comp)

while True:

    marks=int(input("please enter the marks of the student"))

    if  marks >=85 and marks < 90:
        print("Grade A")
    elif marks >=75 and marks <85 :
        print("Grade B")
    elif marks >=65 and marks < 75 :
        print("Grade C")
    elif marks >= 55 and marks <65 :
        print("Grade D")
    else:
        print(" Grade F")
        break 


def mymarks(mark): 


    print("this is my marks ",mark)
mymarks(int(input("enter marks ")))