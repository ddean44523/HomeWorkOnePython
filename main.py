def get_grades():
  grade = []
  weight = []
  for i in range(3):
    grade.append(input(f"Enter your course {i+1} letter grade: "))
    weight.append(input(f"Enter your course {i+1} credit: "))
    print(f"Grade point for course {i+1} is: {grade[i]}")


  grade = grade_to_number(grade)

  print(f"grades{grade} at {weight}")

  
def funny_atof(l):
  for i in range(len(l)):
    l[i] = int(l[i])
  return l
def grade_to_number(l):
  for i in range(len(l)):
    if l[i] == 'A+':
      l[i] = 4.0
    elif l[i] =='A-':
      l[i] = 3.67
    elif l[i] == 'B+': 
      l[i] = 3.33
    elif l[i] == 'B':
      l[i] = 3.0
    elif l[i] == 'B-':
      l[i] = 2.67
    elif l[i] == 'C+':
      l[i] = 2.33
    elif l[i] == 'C':
      l[i] = 2.0
    elif l[i] == 'D':
      l[i] = 1.0
    else:
      l[i] = 0.0
  return l



  
get_grades()



    
  
