# # 1. find the duplicate
# a = [1,2,3,4,5,1,2,3,8,7]
# result = []

# # for i in a : print(a.count(i)) # count()
# # print(a)
# # print(set(a)) # used to remove duplicate = {1, 2, 3, 4, 5, 7, 8}

# # # for i in a:
# # #     if a.count(i) > 1 and i not in result:
# # #         result.append(i)

# # # print(result)

# # method 2
# print("Method 2")

# print(a)
# print(set(a))

# for i in set(a):
#     if a.count(i):
#         result.append(i)
# print(result)



# #  2.Store 10 numbers in a list and print only the even numbers.

# b = [1,2,3,4,5,6,7,8,9,10]


# for i in b:
#     if i % 2 == 0:
#         print(i)

# getting input from user using list

# result = []

# for i in range(int(input("enter num:"))):
#     result.append(int(input()))
# print(result)

# method 2

# n = int(input("Enter num: "))
# # here the [0]*n is the method to assign values as 0 for n values
# result = [0]*n   
# for i in range(n):
#     result[i] = int(input())
#     print(result)


# # find the largest and smallest element in the list

# a = [1,3,45,23,45,2,34]
# print(min(a))
# print(max(a))
# print(min(a),max(a))

#  method 2 without using inbuilt function
# a = [1,3,45,23,45,2,34]


#  count how many times a given number appears in a list
# list = [1,2,3,2,4,2], number = 2

# list = [1,2,3,2,4,3,4,5,1,2]
# print(list.count(3))

# for i in list:
#     print(i)


# method 2 not builtin method
# count = 0
# num = int(input("Enter Num: "))
# for i in list:
#     if (num == i):
#         count = count + 1
# print(count)

# create a new list containing the squares of the all elemts in the give list
# example: [1,2,3] -> [1,4,9]

# list = [1,2,3,4]

# for i in list:
#     print(i**2)


# # this is for single operation
# print([x**2 for x in list]) 

# check  whether the num is in the list

# method 1

# list = [1,3,2,4,5]

# num = int(input("Enter num: "))

# for i in list:
#     if(num == i):
#         print("Num is in the list")
#         break
# else:
#     print("Num is not in the list" )

# # method 2

# print('Exist' if num in list else "Doesn't Exists")

# # normal method

# list = [1,3,2,4,5]
# # print(4 in list)

# if(num in list):
#     print("Exists")
# else:
#     print("Not Exists")




#  find the first  duplicate element in list


# a = [4,5,1,2,3,8,7,5]
# result = []

# for i in a:
#     if a.count(i) > 1:
#         result.append(i)
#         break
#     else:
#         print("No Duplicate")

# print(result)


# method 2

a=[1,2,3,4,1,2,3,4,2]
 
l = len(a)
x= False
for i in range(l):
    for j in range(i+1,l):
        if(a[i]==a[j] ):
            print(a[i])
            x=True
            break
    if x:
        break      

print('a')
 
