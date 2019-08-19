#尋找分數第二高的學生
def second_highest(students):
    grades = [s[1] for s in students] #只拿成績出來
    grades = sorted(grades, reverse=True) #由大到小排名
    second = grades[1] #第二名的位置，第一名為grades[0]
    #接下來尋找分數對應的人員
    second_students = [s[0] for s in students if s[1] == second]

    for student in second_students:
        print(student)

second_highest([['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]])