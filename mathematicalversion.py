#MATHEMATICAL VERSION - Q1, Q2, AND Q3 ARE FLOATING POINT - SOME GATES NEED WORK, MATH MIGHT NOT BE RIGHT
#QUBITS ARE FLOATING POINT, NOT 0 OR 1
#DOCUMENTATION IS IN README
q1 = 0
q2 = 0
q3 = 0
q1 = float(input("q1 position - can be floating point"))
q2 = float(input("q2 position - can be floating point"))
q3 = float(input("q3 position - can be floating point"))
#E IS FLOATING POINT
def both(bit1,bit2,e):
  global q1
  global q2
  global q3
  if bit1 == q1:
    if bit2 == q2:
      q3 = e*q1*q2
    elif bit2 == q3:
      q2 = e*q1*q3
  elif bit1 == q2:
    if bit2 == q1:
      q3 = e*q1*q2
    elif bit2 == q3:
      q1 = e*q2*q3
  elif bit1 == q3:
    if bit2 == q1:
      q2=e*q1*q3
    elif bit2 == q2:
      q1==e*q2*q3
def setsTo(bit1,e):
  global q1
  global q2
  global q3
  if bit1 == q1:
    q1=e
  elif bit1 == q2:
    q2=e
  elif bit1 == q3:
    q3=e
def invert(bit1):
  global q1
  global q2
  global q3
  if bit1 == q1:
    q1 = 1-q1
  elif bit1 == q2:
    q2 = 1-q2
  elif bit1 == q3:
    q3 = 1-q3
def all(bit1,e):
  global q1
  global q2
  global q3
  if bit1 == q1:
    q1=q1*q2*q3*e + (1-q1)*(1-q2)*(1-q3)*e
  elif bit1 == q2:
    q2=q1*q2*q3*e + (1-q1)*(1-q2)*(1-q3)*e
  elif bit1 == q3:
    q3=q1*q2*q3*e + (1-q1)*(1-q2)*(1-q3)*e
#MATH MIGHT NOT BE RIGHT-NEEDS WORK
def unequal(bit1,bit2,e):
  global q1
  global q2
  global q3
  if bit1 == q1:
    if bit2 == q2:
      q3 = e*q1*q2
    elif bit2 == q3:
      q2 = e*q1*q3
  elif bit1 == q2:
    if bit2 == q1:
      q3 = e*q1*q2
    elif bit2 == q3:
      q1 = e*q2*q3
  elif bit1 == q3:
    if bit2 == q1:
      q2=e*q1*q3
    elif bit2 == q2:
      q1==e*q2*q3
print(round(q1,4),round(q2,4),round(q3,4))
