#MATHEMATICAL VERSION-NO LOOPS
#MATH MIGHT BE WRONG, PLEASE TELL IF IT IS
#QUBITS ARE FLOATING POINT, NOT 0 OR 1
#DOCUMENTATION IS IN README
q1 = float(input("q1 position - can be floating point"))
q2 = float(input("q2 position - can be floating point"))
q3 = float(input("q3 position - can be floating point"))
qubits=[q1,q2,q3]
#E IS FLOATING POINT
def both(bit1,bit2,e):
  global qubits
  if bit1 == qubits[0]:
    if bit2 == qubits[1]:
      qubits[2] = e*qubits[0]*qubits[1]+e*(1-qubits[0])*(1-qubits[1])
    elif bit2 == qubits[2]:
      qubits[1] = e*qubits[0]*qubits[2]+e*(1-qubits[0])*(1-qubits[2])
  elif bit1 == qubits[1]:
    if bit2 == qubits[0]:
      qubits[2] = e*qubits[0]*qubits[1]+e*(1-qubits[1])*(1-qubits[0])
    elif bit2 == qubits[2]:
      qubits[0] = e*qubits[1]*qubits[2]+e*(1-qubits[1])*(1-qubits[2])
  elif bit1 == qubits[2]:
    if bit2 == qubits[0]:
      qubits[1]=e*qubits[0]*qubits[2]+e*(1-qubits[2])*(1-qubits[0])
    elif bit2 == qubits[1]:
      qubits[0]==e*qubits[1]*qubits[2]+e*(1-qubits[2])*(1-qubits[1])
def setsTo(bit1,e):
  global qubits
  if bit1 == qubits[0]:
    qubits[0]=e
  elif bit1 == qubits[1]:
    qubits[1]=e
  elif bit1 == qubits[2]:
    qubits[2]=e
def invert(bit1):
  global qubits
  if bit1 == qubits[0]:
    qubits[0] = 1-qubits[0]
  elif bit1 == qubits[1]:
    qubits[1] = 1-qubits[1]
  elif bit1 == qubits[2]:
    qubits[2] = 1-qubits[2]
def all(bit1,e):
  global qubits
  if bit1 == qubits[0]:
    qubits[0]=qubits[0]*qubits[1]*qubits[2]*e + (1-qubits[0])*(1-qubits[1])*(1-qubits[2])*e
  elif bit1 == qubits[1]:
    qubits[1]=qubits[0]*qubits[1]*qubits[2]*e + (1-qubits[0])*(1-qubits[1])*(1-qubits[2])*e
  elif bit1 == qubits[2]:
    qubits[2]=qubits[0]*qubits[1]*qubits[2]*e + (1-qubits[0])*(1-qubits[1])*(1-qubits[2])*e
#MATH MIGHT NOT BE RIGHT-NEEDS WORK
def unequal(bit1,bit2,e):
  global qubits
  if bit1 == qubits[0]:
    if bit2 == qubits[1]:
      qubits[2] = e*(1-qubits[0])*qubits[1]+e*qubits[0]*(1-qubits[1])
    elif bit2 == qubits[2]:
      qubits[1] = e*(1-qubits[0])*qubits[2]+e*qubits[0]*(1-qubits[2])
  elif bit1 == qubits[1]:
    if bit2 == qubits[0]:
      qubits[2] = e*(1-qubits[1])*qubits[0]+e*qubits[1]*(1-qubits[0])
    elif bit2 == qubits[2]:
      qubits[0] = e*(1-qubits[1])*qubits[2]+e*qubits[1]*(1-qubits[2])
  elif bit1 == qubits[2]:
    if bit2 == qubits[0]:
      qubits[1] = e*(1-qubits[0])*qubits[2]+e*qubits[0]*(1-qubits[2])
    elif bit2 == qubits[1]:
      qubits[0] = e*(1-qubits[2])*qubits[0]+e*qubits[2]*(1-qubits[0])
print(round(qubits[0],4),round(qubits[1],4),round(qubits[2],4))
