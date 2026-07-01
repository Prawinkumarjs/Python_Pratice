# # square pattern
# a = int(input("Enter the Number: "))
# for i in range(a):
#     for j in range(a):
#         print("*" ,end=" ")
#     print()



# # square pattern without 2 loops

# b = int(input("Enter num: "))
# for i in range(b):
#     print("* " *b)



# # hollow square method 1

# a = int(input("Enter num: "))

# for i in range(a):
#     container = ""
#     for j in range(a):
#         if(j == 0 or j == a-1 or i == 0 or i == a-1):
#             container += '*_'
           
#         else:
#             container += '  '
           
#     print(container[:-1])

# #  hollow square method 2 without 2 loop

# row = int(input("Enter row: "))

# for i in range(1,row+1):
#     if i==1 or i==row:
#         print(('* '*row).strip())
#     else:
#         print('* '+'  '*(row-2)+'*')


# left triangle

a = int(input('Enter num: '))
for i in range(a):
    for j in range(i+1):
        print("* ", end=" ")
    print()

 