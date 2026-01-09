stud_dict={"Ram":85,"Shyam":90,"Mohan":78,"Sohan":88}
name=input("Enter the name of the student: ")
if name in stud_dict:
    print(f"{name}'s marks:{stud_dict[name]}")
else:
    print("Student not found")
    