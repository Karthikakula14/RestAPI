# students_data = [{'name': 'Karthik', 'grades': [34]},{'name':'Akula','grades':[]},{'name':'Veera','grades':[98]}]
# c = False
# try:
#     for student in students_data:
#         name = student["name"]
#         grades = student['grades']
#         average = sum(grades)/len(grades)
#         print(f"{name} grade is {average}")
# except ZeroDivisionError:
#     print(f"{name} has no grades")
# except TypeError:
#     print(f"{name} has invalid data")
# else:
#     print("All the students grades calculated")
#     c = True
# finally:
#     if c == True:
#         print("*****End of calculating the data*****")
#     else:
#         print("Program Abonded")
####======================================================
# class ToManyPagesRead(ValueError):
#     pass
# class Book:
#     def __init__(self,name: str,pages: int):
#         self.name = name
#         self.pages = pages
#         self.pagesread = 0
#     def read(self,pagecount: int):
#         self.pagecount = pagecount
#         self.pagesread += self.pagecount
#         if self.pagesread > self.pages:
#             raise ToManyPagesRead(f"You are trying to read more than {self.pages} pages")
#     def pagesleft(self):
#             return f"Pages remaining : {self.pages - self.pagesread}"
#     def __str__(self):
#         return f"Book name: {self.name}, Page count: {self.pages}, PagesRead: {self.pagesread}, Pagesremaining: {self.pagesleft()}"
# hulk = Book('Hulk',452)
# hulk.read(73)
# hulk.read(880)
# print(hulk.pagesleft())
# print(hulk)
# try:
#     hulk.read(45)
#     print(f"Pages left after reading {hulk.pagesread} is {hulk.pagesleft()}")
#     hulk.read(770)
#     print(hulk.pagesleft())
# except ToManyPagesRead as Exception:
#     print(Exception)
#####==================================================
#####First class function
# from operator import itemgetter
# def search(sequence,expected,finder):
#     for elem in sequence:
#         if finder(elem) == expected:
#             return elem
#     raise RuntimeError(f"Could not find an element matching {expected}")
# students_data = [{'name': 'karthik', 'grades': [34, 54, 3, 76]},{'name':'Akula','grades':[56]},{'name':'Veera','grades':[98]}]
# def getname(n):
#     return n['name']
# print(search(students_data,'karthik',getname))
# print(search(students_data,'RK',lambda k: k['name']))
# print(search(students_data,'Veera',itemgetter('name')))
# def search(sequence,expected,finder):
#     for i in sequence:
#         if finder(i) == expected:
#             return i
#     raise RuntimeError("data doesn't exists")
# print(search(students_data,'Akula',getname))
######========================================================
# user1 = {'name':'karthik','access_level':'guest'}
# user2 = {'name':'Akula','access_level':'admin'}

# def make_secure(userdata):
#     def make_secure2(func):
#         def secure_pass():
#             if  userdata['access_level'] == 'admin':
#                 return func()
#             else:
#                 return "No Permission"
#         return secure_pass
#     return make_secure2
# @make_secure(user2)
# def get_password():
#     return '1234'
# print(get_password())
#####=========================================
# user1 = {'name':'karthik','access_level':'guest'}
# user2 = {'name':'Akula','access_level':'admin'}
# import functools
# def make_secure(func):
#     @functools.wraps(func)  ### TO keep the name of the main function intact
#     def secure_pass(userdata):
#         if  userdata['access_level'] == 'admin':
#             return func(userdata)
#         else:
#             return f"No Permission for {userdata['name']}"
#     return secure_pass
# @make_secure
# def get_password(n):
#     return '1234'
# print(get_password(user1))
# print(get_password.__name__)
#####==========================================
# import functools
# def make_secure(func):
#     @functools.wraps(func)
#     def secure_pass(*args,**kwargs):
#         if user['access_level'] == 'admin':
#             return func(*args,**kwargs)
#         else:
#             return f"Permission not available for {user['name']}"
#     return secure_pass
# user = {'name':'karthik','access_level':'guest'}
# @make_secure
# def get_pass(data):
#     if data == 'admin':
#         return 1234
#     if data == 'billing':
#         return "More secure password"
# print(get_pass('admin'))
#######=====================================================
# user = {'name':'karthik','access_level':'guest'}
# import functools
# def make_secure(access_level):
#     def decorator(func):
#         @functools.wraps(func)
#         def secure_pass(*args,**kwargs):
#             if user['access_level'] == access_level:
#                 return func(*args,**kwargs)
#             else:
#                 return f"Permission not available for {user['name']}"
#         return secure_pass()
#     return decorator
# user = {'name':'karthik','access_level':'guest'}
# @make_secure("admin")
# def get_admin_pass():
#     return 1234
# @make_secure('guest')
# def get_dash_password():
#     return f"User: user password"
# print(get_admin_pass)
# print(get_dash_password)
######==============================================
# user1 = {'name':'karthik','access_level':'guest'}
# user2 = {'name':'Akula','access_level':'admin'}
# import functools
# def make_secure(access_level):
#     def dec(func):
#         @functools.wraps(func)
#         def secure_pass(user):
#             if user['access_level'] == access_level :
#                 return func(user)
#             else:
#                 return f"Permission not available for {user['name']}"
#         return secure_pass
#     return dec
# @make_secure('admin')
# def get_admin_pass(n):
#     return 1234
# @make_secure('guest')
# def get_dash_password(n):
#     return "User: user password"
# print(get_admin_pass(user2))
# print(get_dash_password(user1))
#####=======================================================
# stores = [
#             {
#      'name':"Amazon",
#         'item':[
#                 {'name': 'Books',
#                  'price': 20
#                  },
#                 {'name': 'Bags',
#                  'price': 25
#                  }
#                 ]
#             }
#         ]
# def delete_item_in_store(stores):
#     for store in stores:
#         if store['name'] == "Amazon":
#             for item in store["item"]:
#                 if item["name"] == "Bags":
#                     store["item"].remove(item)
#                     return store
#             return "Item not found"
# print(delete_item_in_store(stores))
                    # return jsonify({"item left":store["item"]})
                    # item["item"].remove(request_data["item"])
    #         return jsonify({"items":store['item']})
    # return jsonify({"Message: ": "Store not found"})
####=========================================================
# students_data = [{'name': 'Karthik', 'grades': [34]},{'name':'Akula','grades':[45,78,96]},{'name':'Veera','grades':[98]}]
# c = False
# try:
#     for student in students_data:
#         grade = sum(student["grades"])/len(student["grades"])
#         print(f"{student['name']} grade is {grade}")
# except ZeroDivisionError:
#     print(student["name"],"has no grades")
#     # print(f"{student['name'] } has no grades")
# except TypeError:
#     print(f"{student['name']} has invalid grades")
# else:
#     print(f"End of calculating the grades")
#     c = True
# finally:
#     if c ==True:
#         print("All the student data calculated")
#     else:
#         print("Calculation abonded due to data error")
