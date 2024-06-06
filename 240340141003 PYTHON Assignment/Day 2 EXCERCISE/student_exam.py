# 6) A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.



def attendance_check(classes_held, classes_attended):
    attendance_percentage = (classes_attended / classes_held) * 100
    if attendance_percentage < 75:
        print(f"Your attendance is {attendance_percentage}%. You are not allowed to sit in the exam.")
    else:
        print(f"Your attendance is {attendance_percentage}%. You are allowed to sit in the exam.")


classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

attendance_check(classes_held, classes_attended)