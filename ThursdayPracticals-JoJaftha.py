# These inputs are not used in the program (can be removed)
Student1 = input("Mark1")  
Student2 = input("Mark2")  
Student3 = input("Mark3")  

# Function to calculate the average of 3 marks
def calculate_average(mark1, mark2, mark3):
    average = (mark1 + mark2 + mark3) / 3  # Add marks and divide by 3
    return average  # Return the calculated average

# Function to determine the grade based on average
def get_grade(average):
    if average >= 75:          # If average is 75 or more
        return "A"
    elif average >= 60:        # If average is between 60–74
        return "B"
    elif average >= 50:        # If average is between 50–59
        return "C"
    else:                      # If average is below 50
        return "F"
    
# Function to check if student passed or failed
def check_pass_fail(average):
    if average >= 50:          # 50 or more is a pass
        return "Pass"
    else:
        return "Fail"          # Below 50 is a fail

# Function to display the results clearly
def display_result(name, average, grade, status):
    print("Student Name:", name)   # Display student's name
    print("Average:", average)     # Display calculated average
    print("Grade:", grade)         # Display grade
    print("Status:", status)       # Display pass/fail status


def main():
    num_students = int(input("How many students? "))
    for i in range(num_students):
        print("\nStudent", i + 1)
        name = input("Enter name: ")
        mark1 = float(input("Enter mark 1: "))
        mark2 = float(input("Enter mark 2: "))
        mark3 = float(input("Enter mark 3: "))
        average = calculate_average(mark1, mark2, mark3)
        grade = get_grade(average)
        status = check_pass_fail(average)
        display_result(name, average, grade, status)
main()