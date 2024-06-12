courses = open("course_list-josaa.txt", "r")

sorted_course_list = open("cse_courses-josaa.txt", "w")

course_list = courses.readlines()
cse_courses = []

for course in course_list:
    if "Computer" in course.split(' '):
        cse_courses.append(course)
    elif "CSE" in course.split(' '):
        cse_courses.append(course)
    elif ">Computer" in course.split(' '):
        cse_courses.append(course)

sorted_course_list.writelines(cse_courses)

courses.close()

sorted_course_list.close()