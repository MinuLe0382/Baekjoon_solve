import math 

case_number = int(input())

count = 0
result = []     

for i in range(case_number):
  a, b = map(int, input().split(' '))

  distance = b - a  
  square_root = math.floor(math.sqrt(distance))  
  squared = square_root**2  
  
  if distance <= 3: 
    count = distance
  elif distance == squared:
    count = (square_root*2)-1
  elif squared < distance <= square_root + squared:
    count = (square_root*2)
 
  elif square_root + squared < distance:
    count = (square_root*2)+1
  result.append(count) 
for k in result:
  print(k)