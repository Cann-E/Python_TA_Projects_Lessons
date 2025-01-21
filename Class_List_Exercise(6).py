class Student_Grade_System():
    def __init__(self):
        self.system = []
        
    def add_student(self):
        name_add = input("What's the student's name you want to add: ")
        grade_add = int(input("What's the student's grade (0-100): "))
        student = [name_add, grade_add]
        self.system.append(student)
        return student
    
    def remove_student(self):
        print(f"These are all the students: {self.system}")
        student_remove = input("What's the student you want to remove from the list: ").strip()
        for student in self.system:
            if student[0] == student_remove:
                self.system.remove(student)
                print(f"{student_remove} has been removed from the system!")
                return student
        print(f"{student_remove} not found in the system!")
        return None  # Return None if the student is not found
                
    def update_student_grade(self):
        update_stu = input("What's the student name you want to update grades for: ").strip()
        for student in self.system:
            if student[0] == update_stu:  # Check if the student exists
                new_grade = int(input("Enter the updated grade: "))
                student[1] = new_grade  # Update the grade
                print(f"New grade for {update_stu} is {student[1]}")
                return student
        print(f"Student {update_stu} not found in the system!")
        return None
            
    def view_student(self):
        if not self.system:
            print("The system is empty!")
        else:
            print(f"Students in the system: {self.system}")
        
    def search_student(self):
        search = input("What's the student name you're looking for: ").strip()
        for student in self.system:
            if student[0] == search:
                print(f"{search} student found with grade {student[1]}!")
                return
        print(f"{search} student not found!")
                
    def calculate_average(self):
        if not self.system:
            print("System is empty!")
            return
        total = sum(student[1] for student in self.system)  # Sum all grades
        average = total / len(self.system)  # Calculate the average
        print(f"The average student grade is: {average:.2f}")
        

# Main Program
can_grade_system = Student_Grade_System()

while True:
    system_start = input("Welcome to the Student Grade Management System!\n"
                         "1 - Add a Student \n"
                         "2 - Remove a Student \n"
                         "3 - Update a Student's Grade \n"
                         "4 - View All Students \n"
                         "5 - Search for a Student \n"
                         "6 - Calculate Class Average \n"
                         "7 - Exit \n"
                         ": ").strip().lower()
    
    if system_start == "1":
        add = can_grade_system.add_student()
        print(f"{add[0]} with grade {add[1]} has been added to the system!")
      
    elif system_start == "2":
        remove = can_grade_system.remove_student()
        if remove:
            print(f"Removed student: {remove[0]}")
    
    elif system_start == "3":
        update = can_grade_system.update_student_grade()
        if update:
            print(f"Updated student: {update[0]} with new grade {update[1]}")
        
    elif system_start == "4":
        can_grade_system.view_student()
        
    elif system_start == "5":
        can_grade_system.search_student()
        
    elif system_start == "6":
        can_grade_system.calculate_average()
        
    elif system_start == "7":
        print("Program Terminated!")
        break
    
    else:
        print("Invalid option! Please try again.")
