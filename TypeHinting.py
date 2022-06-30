from typing import List
# def data_avg(sequence: List) -> float:
#     return sum(sequence)/len(sequence)
# print(data_avg([123,78,52,96,71]))
####==========================================
# class Book:
#     Types = ['Hardcopy',"Papercopy"]
#     def __init__(self,name:str,type:str,cost:int):
#         self.name =name
#         self.type = type
#         self.cost  = cost
#     @classmethod
#     def Hardcopy(cls,name:str,cost:int) ->"BOOK Details":
#         return cls(name,cls.Types[0],cost)
#     @classmethod
#     def Papercopy(cls,name:str,cost:int) ->"BOOK Details":
#         return cls(name,cls.Types[1],cost)
#     def __repr__(self) -> str:
#         return f"Book name is {self.name}, Cost: {self.cost}, Type: {self.type},"
# book1 = Book.Hardcopy('Iron',1500)
# book2 = Book.Papercopy('Thor',9005)
# book3 = Book.Papercopy('Thor 2',900)
# print("Module from file",__name__)
###=================================================
# def divide(a,b):
#     if b==0:
#         raise ZeroDivisionError("Division cannot be zero")
#     else:
#         return a/b
# grades = ['ki']
# try:
#     average = divide(sum(grades),len(grades))
#     print(f"The avergae of given number is {average}")
# except ZeroDivisionError as e:
#     print(e)
#     print("Input cannot be zero")
# except TypeError as p:
#     print(p)
#     print("type error")
####==========================================
# k1 = [{"name":"karthik"},{"name":"karthik"},{"name":"Ramzan"},{"name":"Sasi"},{"name":"Ramzan"},{"name":"RK"},{"name":"karthik"},{"name":"RK"},{"name":"RK"},{"name":"Sasi"},]
# idx_num = []
# for i in range(len(k1)):
#     if k1[i]["name"] == "Sasi" or k1[i]["name"] == "Ramzan":
#         idx_num.append(i)
# for i in range(len(idx_num)-1,-1,-1):
#     k1.pop(idx_num[i])
# print(k1)
###==============================================
# k1 = [{"name":"karthik"},{"name":"karthik"},{"name":"Ramzan"},{"name":"sasi"},{"name":"Ramzan"},{"name":"RK"},{"name":"karthik"},{"name":"RK"},{"name":"RK"},{"name":"Sasi"},]
# for i in k1:
#     if i["name"] == "karthik":
#         print(k1.index(i))
#
# k1 = [{"name":"karthik"},{"name":"karthik"},{"name":"Ramzan"},{"name":"karthik"},{"name":"Ramzan"},{"name":"RK"},{"name":"karthik"},{"name":"RK"},{"name":"RK"},{"name":"Sasi"},]
# k1.pop(2)
# k2 = k1
# print(k2)