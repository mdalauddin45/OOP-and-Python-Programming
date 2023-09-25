numbers=[47,38,79,34,75,86,8,78,90]
# odds=[]
# even=[]
# for num in numbers:
#     if num%2==1 and num %5==0:
#         odds.append(num)
#     else:
#         even.append(num)
# print(odds)
# print(even)

odd_nums = [num for num in numbers if num%2==1]
odd_num1 = [num for num in numbers if num%2==1 and num%5==0]
odd_num2 = [num for num in numbers if num%2==1 or num%5==0]
print(odd_nums)
print(odd_num1)
print(odd_num2)