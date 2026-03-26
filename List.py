print("Please enter the numnber of students in their class")

num_of_students = int(input("Enter the number of students here"))

StudentList = []
StudentList.append("Max")
StudentList.append("Amy")
StudentList.append("Jessica")
StudentList.append("Caiden")
StudentList.append("Lutho")

for y in range(0,num_of_students):
    StudentList[y] = input("Enter student details:")

for x in StudentList:
 print(x)
 