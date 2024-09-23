grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
srednee = {}
students_new = sorted(students)
srednee[students_new[0]] = sum(grades[0]) / len(grades[0])
srednee[students_new[1]] = sum(grades[1]) / len(grades[1])
srednee[students_new[2]] = sum(grades[2]) / len(grades[2])
srednee[students_new[3]] = sum(grades[3]) / len(grades[3])
srednee[students_new[4]] = sum(grades[4]) / len(grades[4])
print(srednee)