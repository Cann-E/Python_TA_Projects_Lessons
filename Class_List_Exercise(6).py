
class Student_Grade_System():#not finished fix
    def __init__(self):
        self.system=[]
        
    def add_student(self):
        name_add=input("Whats student name you want to add: ")
        grade_add=int(input("Whats the students grade: "))
        student=([name_add,grade_add])
        self.system.append(student)
        return student
    
    def remove_student(self):
        print(f"These are all the students {self.system}")
        student_remove=input(f"Whats the student you want to remove from the listL: ")
        for student in self.system:
            if student[0]==student_remove:
                self.system.remove(student)
                print(f"{student_remove} Student removed from the system!")
                return student
            else:
                print(f"{student_remove} not found in the system!")
                
    def update_student_grade(self):
        update_stu=input("Whats the student name you want to update grades to: ")
        for update in self.system:
            new_grade=int(input("Enter the updated grade: "))
            update[1]=new_grade
            print(f"New grade for {update_stu} is {update[1]}")
            return update
        else:
            print(f"Student not found {update_stu}")
            
    def view_student(self):
        print(f"{self.system} This is the students in the system!")
        
    def search_student(self):
        search=input("Whats the student name you looking for: ")
        for student in self.system:
            if student[0] == search:
                print(f"{search} student found!")
        else:
            print(f"{search} Student not found!")
                
    def calculate_average(self):
        if not self.system:
            print("System is empty!")
            return
        total=0
        for item in self.inventory:
            total += item[1] / item[0]  
        print(f"Average student grade is: ${total:.2f}")
        
        
can_grade_system=Student_Grade_System()

while True:
    system_start = input("Welcome to the Student Grade Management System!\n"
                    "1 - Add a Student \n"
                    "2 - Remove a Student \n"
                    "3 - Update a Student's Grade \n"
                    "4 - View All Students \n"
                    "5 - Search for a Student \n"
                    "6 - Calculate Class Average \n"
                    "7 - Exit \n"
                    ": ").lower()
    
    if system_start=="1":
      add=can_grade_system.add_student()
      print(f"{add} Student added to system!")
      
    elif system_start =="2":
        remove=can_grade_system.remove_student()
    
    elif system_start =="3":
        update=can_grade_system.update_student_grade()   
        
    elif system_start =="4":
        can_grade_system.view_student()
        
    elif system_start == "5":
        can_grade_system.search_student()
        
    elif system_start == "6":
        can_grade_system.calculate_average()
        
    elif system_start == "7":
        print("Program Terminated!")
        break

            
        