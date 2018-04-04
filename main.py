import json


# ToDos
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
        existing = json.load(data_file)
    exist_gr = existing["mygrades"]
    return exist_gr


def askForAssignmentMarks(grades, st_grades):
    current_grades = {"mygrades": {}}

    for key in grades:
        try:
            if st_grades[key] > -1:

                "Your Grade from " + key + " is " + str(st_grades[key])
                current_grades["mygrades"][key] = st_grades[key]
                answer = raw_input("Do you want to update your score y/n")
                if answer == "y":
                    current_grades["mygrades"][key] = input("your new score")
            else:
                current_grades["mygrades"][key] = input(
                    "What is your Current Grade for: " + key + " . Please insert -1 if you don't have a grade yet")
        except:
            current_grades["mygrades"][key] = input(
                "What is your Current Grade for: " + key + " . Please insert -1 if you don't have a grade yet")

    return current_grades


def saveGrades(current_grades):
    print(json.dumps(current_grades))
    file = open("gc_grades.json", "w")
    file.write(json.dumps(current_grades))
    file.close()


def printCurrentGrade(grades, current_grades):
    curr_grade = 0
    for key in current_grades["mygrades"]:
        if current_grades["mygrades"][key] != -1:
            calc_grade = float(current_grades["mygrades"][key]) * grades[key] / 100
            curr_grade = curr_grade + calc_grade
    print(curr_grade)
    return curr_grade


def printLetterGrade(curr_grade, conv_matrix):
    for i in range(len(conv_matrix)):
        if curr_grade > conv_matrix[i]["min"] and curr_grade <= conv_matrix[i]["max"]:
            letter_grade = conv_matrix[i]["mark"]

    return letter_grade



def main():
    setup = loadSetupData()
    grades = setup["grade_breakdown"]
    conv_matrix = setup["conv_matrix"]
    st_grades = loadStudentGrades()
    current_grades = askForAssignmentMarks(grades, st_grades)
    saveGrades(current_grades)
    curr_grade = printCurrentGrade(grades, current_grades)
    letter = printLetterGrade(curr_grade, conv_matrix)


main()