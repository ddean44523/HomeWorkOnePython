def get_grades():
  grade = []
  weight = []
  for i in range(3):
    grade.append(g_to_n(input(f"Enter your course {i+1} letter grade: ")))
    
    weight.append(input(f"Enter your course {i+1} credit: "))

    print(f"Grade point for course {i+1} is: {grade[i]}")
  funny_atof(weight)

  print(f"Your GPA is: {gpa_calc(grade,weight)}")
  
def funny_atof(l):
  for i in range(len(l)):
    l[i] = int(l[i])
  return l

def g_to_n(l):
  print(l)
  if l == 'A+':
     l = 4.0
  elif l =='A-':
      l = 3.67
  elif l == 'B+': 
      l = 3.33
  elif l == 'B':
      l = 3.0
  elif l == 'B-':
      l = 2.67
  elif l == 'C+':
      l = 2.33
  elif l == 'C':
      l = 2.0
  elif l == 'D':
      l = 1.0
  else:
      l = 0.0
  return l
  ##I hope it's not too obvious that I am self taught

def gpa_calc(l,y):
  '''GPA = (gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3) '''
  gpa = 0 
  div = y[0] +y[1] +y[2]
  for i in range(len(l)):
      gpa += l[i] * y[i]
  gpa = gpa/div

  return gpa

get_grades()

#this may be a little convoluted 



    
  
