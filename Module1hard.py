scores = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}
students = list (students)
students.sort ()
Average_score = [sum (scores[0]) / len (scores[0]), sum (scores[1]) / len (scores[1]), sum (scores[2]) / len (scores[2]),sum (scores[3]) / len (scores[3]),sum (scores[4]) / len (scores[4])]
grade = dict(zip(students,Average_score))
print('Успеваемость в классе : ', grade)