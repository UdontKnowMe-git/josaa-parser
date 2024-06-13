courses = open("course_list-josaa.txt", "r") 

sorted_course_list = open("opted_courses-josaa.txt", "w")

course_list = courses.readlines()
opted_courses = []

course-opt = input("What courses would you like to opt for?(CSE/B.Tech/ECE/other): ")
opted = []
if course-opt == "CSE":
    opted = ["Computer","CSE",">Computer"]
elif course-opt == "ECE":
    opted = [">Electronics", "Communication", "Electrical"]
elif course-opt == "B.Tech":
    opted = [">B. Tech", "Technology", "Bachelor"]
elif course-opt == "other":
    filter_courses = ["Computer","CSE",">Computer",">Electronics", "Communication", "Electrical",">B. Tech", "Technology", "Bachelor"]
    for course_ in course_list:
        for filter_course in filter_courses:
            if filter_course not in course_:
                opted_courses.append(course_)
    print("Courses sorted succesfully. Open opted_courses-josaa.txt for your course list.)
    exit()
for course in course_list:
    if opted[0] in course.split(' '):
        cse_courses.append(course)
    elif opted[1] in course.split(' '):
        cse_courses.append(course)
    elif opted[2] in course.split(' '):
        cse_courses.append(course)

sorted_course_list.writelines(cse_courses)
print("Courses sorted succesfully. Open opted_courses-josaa.txt for your course list.)
courses.close()

sorted_course_list.close()
