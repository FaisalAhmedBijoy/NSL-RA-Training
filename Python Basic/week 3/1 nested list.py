n=int(input())
student=[]
score_set=set()
for i in range(n):
    name = input()
    score = float(input())
    student.append([name,score])
    score_set.add(score)
    
student=sorted(student)    
#print(student)
second_score=sorted(score_set)[1]
result=[]
for name,score in student:
    if second_score==score:
        print(name)