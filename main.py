import random
#PREP
i=0
#QUBIT AVERAGE
q1average = 0
q2average = 0
q3average = 0
#CALCULATIONAMOUNT
calculationamount = 100000
#DIVIDER - SETS REAL VALUE OF PRESUPERPOSITIONS (0 TO 1)
divider = 0.50
#QUBITS
q1 = 0
q2 = 0
q3 = 0
#SUM OF ALL BITS IF GATE ACTING WEIRD
e=q1+q2+q3
#GATES
#SETS TO 0 OR 1
#BIT=QUBIT BEING OPERATED ON, POSITION = 0 OR 1
def setsTo(bit1, position):
    global q1
    global q2
    global q3
    if bit1 == q1:
        q1 = position
    elif bit1 == q2:
        q2 = position
    elif bit1 == q3:
        q3 = position
#SETS BIT1 TO OPPOSITE OF BIT1 (INVERTS)
def invert(bit1):
    global q1
    global q2
    global q3
    if bit1 == q1:
      if q1 == 1:
        q1 = 0
      elif q1 == 0:
        q1 = 1
    elif bit1 == q2:
      if q2 == 1:
        q2 = 0
      elif q2 == 0:
        q2 = 1
    elif bit1 == q3:
      if q3 == 1:
        q3 = 0
      elif q3 == 0:
        q3 = 1
#SETS REMAINING QUBIT TO E IF QUBIT 1 AND 2 ARE THE SAME
def both(bit1,bit2,e):
  global q1
  global q2
  global q3
  global divider
  if bit1 == q1 and bit2 == q2 and q1==q2:
    q3=e
  elif bit1 == q1 and bit2 == q3 and q1==q3:
    q2=e
  if bit1 == q2 and bit2 == q3 and q2==q3:
    q1=e
  elif bit1 == q2 and bit2 == q1 and q1==q2:
    q3==e
  if bit1 == q3 and bit2 == q1 and q1==q3:
    q2=e
  elif bit1 == q3 and bit2 == q2 and q2==q3:
    q1=e
  divider = 0.5
#IF EVERY SINGLE ONE IS EQUAL, BIT1 FLIPS TO E.
def all(bit1,e):
  global q1
  global q2
  global q3
  if q3 == q2 and q2 == q1:
    if bit1 == q1:
      q1=e
    elif bit1 == q2:
      q2=e
    elif bit1 == q3:
      q3=e
#IF BIT 1 AND BIT 2 ARE NOT EQUAL, REMAINING BIT IS FLIPPED TO E
def unequal(bit1,bit2,e):
  global q1
  global q2
  global q3
  if bit1 == q1:
    if bit2 == q2 and q1 != q2:
      q3 = e
    elif bit2 == q3 and q1 != q3:
      q2 = e
  if bit1 == q2:
    if bit2 == q3 and q2 != q3:
      q1=e
    elif bit2 == q1 and q1 != q2:
      q3=e
  if bit1 == q3:
    if bit2 == q2 and q2 != q3:
      q1=e
    elif bit2 == q1 and q1 != q3:
      q2=e
#LOOP OF CALCULATIONS
while i < calculationamount:
    i += 1
    #SETS PRE SUPERPOSITION
    q1 = random.uniform(0, 1)
    q2 = random.uniform(0, 1)
    q3 = random.uniform(0, 1)
    #SETS REAL POSITION
    if q1 < divider:
        q1 = 0
    else:
        q1 = 1
    if q2 < divider:
        q2 = 0
    else:
        q2 = 1
    if q3 < divider:
        q3 = 0
    else:
        q3 = 1
    if i % 1000 == 1:
      print(q1, q2, q3, "original")
    #APPLY GATES TO QUBITS HERE
    #PUT THIS AT VERY END
    q1average += q1 / calculationamount
    q2average += q2 / calculationamount
    q3average += q3 / calculationamount
    if i % 1000 == 1:
      print(q1, q2, q3, "modified")
print(round(q1average,4), round(q2average,4), round(q3average,4))
