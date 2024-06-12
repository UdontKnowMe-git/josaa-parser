file = open("JOSAA choices.txt","r")
sorted_josaa = open("course_list-josaa.txt", "w")

sorted_josaa.writelines(["JOSAA course list:", ""])

contents = file.read()
file.close()

courses = []

for i in range(len(contents)-1):
    word = ""
    if contents[i] == ">":
        while contents[i] != "<":
            word += contents[i]
            i += 1
        courses.append(word)
    
for course in courses:
    if course == ">":
       courses.pop(courses.index(course))

for i in courses:
    sorted_josaa.write(i + "\n")

sorted_josaa.close()