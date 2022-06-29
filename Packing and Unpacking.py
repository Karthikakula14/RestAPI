# def data(a,b,c,d):
#     print(a,b,c,d)
#     # for i in args:
#     #     print(i)
# d1 = {'a':5,'b':8,'d':7,'c':87}
# data(*d1.items())
##========================================
# def multiply(*args):
#     total = 1
#     for arg in args:
#         total = total*arg
#     return total
#
# def multiple(*args,operator):
#     if operator == "*":
#         return multiply(*args)
#     if operator == "+":
#         return  sum(args)
#     else:
#         return "Not a valid operator"
# print(multiple(5,6,9,8,operator="-"))
##===============================================
# Creating a dictionary using **args
# def name(**args):
#     print(args)
# name(name = "karthik",age = 25)
# ##====================================================
# def data(**args):
#     print(args)
# details ={'name':"karthik","age":25,'height':5.6}
# data(**details)
##==================================================
# def named(**kwargs):
#     print(kwargs)
#
# def name_nicely(**kwargs):
#     named(**kwargs)
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
# name_nicely(name = "karthik",age= 25)
#=============================================
# def both(*args,**kwargs):
#     print(args)
#     print(kwargs)
# both(1,2,8,name = "karthik",age= 25)
##=========================================
# def name(a,b,c,d):
#     print(a,b,c,d)
# details = [25,87,41]
# name(*details,85)
# #========================
# def name(**kwargs):
#     print(kwargs)
# name(name = "karthik",age= 25)
# #=================================
#
