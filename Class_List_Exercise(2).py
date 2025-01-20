

class student_system():#later finish
    def __init__(self):
        self.student_names=[]
        self.student_grade=[]
        
    def add_student(self):
        student_add=input("Please Enter Student Name: ")
        student_grade=input("Please Enter Student grade: ")
        self.student_names.append(student_add)
        self.student_grade.append(student_grade)
        return student_add,student_grade
    
    def remove_student(self):
        student_remove=input("Which Student would you like the remove from the system: ")
        if student_remove in self.student_names:
            index=self.student_names.index(student_remove)
            removed_name=self.student_names.pop(index)
            removed_grade=self.student_grade.pop(index)
            print(f"{removed_name} with {removed_grade} grade is removed from the system! ")
            
    def search_student(self):
        student_search=input("Whats the students name you searching in the system: ")
        for i in range(len(self.student_names)):
            if self.student_names[i]==student_search:
                print(f"{student_search} is found with a grade of {self.student_grade[i]}!")
                break  
        else:
           print(f"{student_search} is not in the system!")
           
    def update_student_grade(self):
        
    
    