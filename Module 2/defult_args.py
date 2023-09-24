# def sum(num1,num2):
#     result = num1+num2
#     return result
# def sum(num1,num2,num3):
#     result = num1+num2+num3
#     return result
# def sum(num1,num2,num3,num4):
#     result = num1+num2+num3+num4
#     return result

# total = sum(99,11,5)
# print('total: ', total)

#args 
def all_sum(*numbers):
    print(numbers)
    s=0
    for num in numbers:
        print(num)
        s+=num
    return s

total = all_sum(45,56,90,3,23,54,74)
print('total ',total)