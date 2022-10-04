import math
def find_sd(l):
  amount=0
  total=0
  for i in l:
    amount+=i
  for i in l:
    total+=(i-(amount/len(l)))**2
  sd=math.sqrt(total/(len(l)-1))
  print("Standard deviation is %.2f." %sd)
score=[]
n=0
sum=0
while True:
  x = float(input("Enter score: "))
  if x==-1:
    break
  else:
    if x<0 or x>100:
      print("Score is out of range.")
    else:
      score.append(x)
      sum+=x
      n+=1
print("Maximum score is %.2f."%max(score))
print("Minimum score is %.2f."%min(score))
print("Average score is %.2f."%(sum/n))
find_sd(score)