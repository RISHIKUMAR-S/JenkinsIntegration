students = [{"name": "ram", "rollno": 120, "cgpa": 9.5}, {"name": "rajesh", "rollno": 88, "cgpa": 7.9}, {"name": "harini", "rollno": 92, "cgpa": 8.8}, {"name": "dinesh", "rollno": 70, "cgpa": 9.0}, {"name": "ajay", "rollno": 55, "cgpa": 7.0}, {
    "name": "shiva", "rollno": 20, "cgpa": 7.8}, {"name": "abi", "rollno": 2, "cgpa": 9.2}, {"name": "harish", "rollno": 10, "cgpa": 8.2}, {"name": "venkat", "rollno": 34, "cgpa": 8.5}, {"name": "sidhu", "rollno": 11, "cgpa": 10}]
minimum_cgpa = int(input("Enter the minimum cgpa : "))
for student in students:
    if student["cgpa"] >= minimum_cgpa:
        print(student)

strength = int(input("Enter the number of students : "))
student = list()
for i in range(strength):
    detail = dict()
    detail["name"] = input("Enter the {} student\'s name : ".format(i+1))
    detail["roll"] = int(input("Enter the rollno : "))
    detail["cgpa"] = int(input("Enter the cgpa : "))
    student.append(detail)
print(student)
