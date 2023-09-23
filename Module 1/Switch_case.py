mark=int(input())

if mark<0 or mark>100:
    print("Inavid mark")
else:
    grade = ''  
    if mark>=90:
        grade = 'A+'
    elif mark>=80:
        grade = 'A'
    elif mark>=70:
        grade = 'B+'
    elif mark>=60:
        grade = 'B'
    elif mark>=50:
        grade = 'C'
    elif mark>=40:
        grade = 'D'
    else:
        grade = 'F'
    print('Grade = ', grade)