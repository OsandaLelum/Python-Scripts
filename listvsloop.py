##List comprehensions are faster than for loops because they are more concise and perform the same operations in fewer lines of code

'''
list_test=[]
for num in range(1,1000):
    if num%3==0:
        list_test.append(num)

print(list_test)
   '''

list_test = [num for num in range(1, 1000) if num%3==0]
print(list_test)