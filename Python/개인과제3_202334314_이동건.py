test = [57,99,78,85,60]
print("Reseult >")
for i,value in enumerate(test):
    if(value>=70):
        print("번호[0] 학생의 점수는 {1}입니다. 합격!".format(i+1,value))
    else:
        print("번호{0} 학생의 점수는 {1}입니다. 불합격!".format(i+1,value))