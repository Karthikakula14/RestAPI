# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
###==========================================================
# n = -5
# fact = 1
# for i in range(n,-1,-1):
#     fact = fact*i
# print(fact)
##=========================
# n = 29
# for i in range(2,n):
#     if n%2 == 0:
#         print("NOt prime")
#         break
#     else:
#         pass
# else:
#     print(n, "The given numebr is prime number")
###=============================================
# l1 = [10,20,30,40]
# a = 34
# l1 = l1[:-1]+[a]+l1[-1:]
#   #  [10,20,30]
# print(l1)
##======================
# l1 = [3,4,5,7,8,10]
# for i in l1:
#     if i%2==0:
#         print(i)
##===========================
# k1 = 153
# k2 = 0
# for i in str(k1):
#      k2 +=int(i)**len(str(k1))
# if k1 == k2:
#     print("Armstrong number")
# else:
#     print("Not armstrong")
# print(k2)
###===============================
# n = int(input("Enter number:: "))
# rev_num = ""
# for i in str(n):
#     rev_num = i+ rev_num
# print(rev_num)
####============================
# n = 5
#
# def fibbonaci(n):
#     fib = 0
#     n1 = 0
#     n2 = 1
#     for i in range(n):
#         fib += n1
#         n1 = n2
#         n2 = fib
#
# print(fibbonaci(8))
###==========================
# k1 = "zef"
# for i in k1:
#     print(ord(i)-96,end=" ")
# l1 = list(range(2,100))
# k1 = filter(lambda n:n%2==0,l1)
# print(list(k1))
l1 = [25,448,78,5,33,1,25,12,45,85,885,447,56]
l1.sort()  ## ASCENDING METHOD
print(l1)
l1.sort(reverse=True)  ### DESCENDING METHOD
print(l1)
for i in range(len(l1)):
    for j in range(len(l1)):
        if l1[i] < l1[j]:
            l1[i],l1[j] = l1[j],l1[i]
print(l1)