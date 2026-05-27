
#if


score = int(input("score=?"))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:    
    grade = 'F'
5
print("your score ",score," and grade is " ,grade)


print("your score "+str(score)+" and grade is " +grade)