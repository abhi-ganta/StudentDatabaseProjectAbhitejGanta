import sqlite3

connection = sqlite3.connect('StudentDB.db')
cursor = connection.cursor()

cursor.execute("SELECT Student.Last_Name, Student.First_Name, Student_Grades.Test_Grade, Course_Info.Course_Name FROM Student, Student_Grades, Course_Info WHERE Student_Grades.Student_ID = Student.Student_ID AND Student_Grades.Course_ID = Course_Info.Course_ID AND Student_Grades.Test_Grade >85")
results = cursor.fetchall()

for course in results:
    Last_Name, First_Name, Test_Grade, Course_Name = course
    print "%s %s" %(First_Name, Last_Name)
    print "%s : %s" %(Course_Name, Test_Grade)
    print ""




connection.close()