import json

#ToDos
#   1.Limit the grades
#   2.Order the list
#   3.Grade should be a number
#   4.

def loadSetupData():

    with open('gc_setup.json') as data_file:
        course = json.load(data_file)
    setup = course["course_setup"]
    return setup

def loadStudentGrades():
    with open("gc_grades.json") as data_file:
        existing=json.load(data_file)
    return existing


def askForAssignmentMarks(grades, gnahatakanner, student_id):
    current_grades = {}

    if gnahatakanner and (student_id in gnahatakanner):
        for key in grades:
            if gnahatakanner[student_id][key] > -1:
                print "Your Grade from " + key + " is " + str(gnahatakanner[student_id][key])
                current_grades[key] = gnahatakanner[student_id][key]
                answer = raw_input("Do you want to update your score y/n")
                if answer == "y":
                    current_grades[key] = input("please enter your new score")
            else:
                current_grades[key] = input("What is your Current Grade for: " + key + " . Please insert -1 if you don't have a grade yet")
    else:
        for key in grades:
            current_grades[key] = input(
                "What is your Current Grade for: " + key + " . Please insert -1 if you don't have a grade yet")

    gnahatakanner[student_id] = current_grades
    return gnahatakanner

def saveGrades(current_grades):
    print (json.dumps(current_grades))
    file = open("gc_grades.json", "w")
    file.write(json.dumps(current_grades))
    file.close()

def printCurrentGrade(grades, current_grades,student_id):
    curr_grade = 0
    for key in current_grades[student_id]:
        if current_grades[student_id][key] != -1:
            calc_grade = float(current_grades[student_id][key]) * grades[key] / 100
            curr_grade = curr_grade + calc_grade
    print (curr_grade)
    return curr_grade

def printLetterGrade(curr_grade,conv_matrix):
    letter_grade = "N/A"

    for i in range(len(conv_matrix)):
        if curr_grade>conv_matrix[i]["min"] and curr_grade<=conv_matrix[i]["max"]:
            letter_grade=conv_matrix[i]["mark"]
    print letter_grade
    return letter_grade





def main():
    setup = loadSetupData()
    grades = setup["grade_breakdown"]
    conv_matrix = setup["conv_matrix"]
    student_id=raw_input("your id ??")
    gnahatakanner = loadStudentGrades()
    current_grades = askForAssignmentMarks(grades, gnahatakanner, student_id)
    saveGrades(current_grades)
    curr_grade = printCurrentGrade(grades, current_grades, student_id)
    letter=printLetterGrade(curr_grade, conv_matrix)
main()