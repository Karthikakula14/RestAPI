# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age  = age
#     # def __str__(self):
#     #     return f"Person '{self.name}',{self.age} years old"
#     def __repr__(self):
#         return f"<Person ('{self.name}',{self.age})>"
# obj = Student("AK",25)
# print(obj)
##======================================
# class Store:
#     def __init__(self, name):
#         self.name = name
#         self.item = []
#
#     def add_item(self, name, price):
#         d = {'name': name, 'price': price}
#         self.item.append(d)
#
#     def stock_price(self):
#         return sum(item['price'] for item in self.item)
# store = Store('apple')
# store.add_item("Orange",5)
# print(store.stock_price())
##============================================
# class Allmethods:
#     def instanceMethod(self):
#         print(f"called as Instance Method of {self}")
#     def __str__(self):
#         return "Methods checking"
# ak =Allmethods()
# print(ak)
##================================================
# class Book:
#     TYPES = ('Hardcopy','Paperback')
#     def __init__(self,name,type,weight):
#         self.name = name
#         self.type = type
#         self.weight = weight
#     # def __str__(self):
#     #     return f"< Book name {self.name} type {self.type} weight {self.weight} types"
#     def __repr__(self):
#         return f"< Book name {self.name} type {self.type} weight {self.weight}"
# book = Book("harrypoter",'hardcaopy','1500gm')
# print(book)
##=============================================================
# class Book:
#     TYPES = ("Hardcopy","Paperback")
#     def __init__(self,name,type,weight):
#         self.name = name
#         self.type = type
#         self.weight =weight
#
#     def __repr__(self):
#         return f"< Book name {self.name} type {self.type} weight {self.weight} >"
#     @classmethod
#     def Hardcover(cls,name,weight):
#         return cls(name,Book.TYPES[0],weight)
#     @classmethod
#     def Paperback(cls,name,weight):
#         return cls(name,Book.TYPES[1],weight)
# book = Book.Hardcover('AK',1500)
# book1 = Book.Paperback("ASK",1600)
# print(book.name)
# print(book)
# print(book1)
###======================================================
# class Store:
#     def __init__(self,name):
#         self.name = name
#         self.item  = []
#     def addItem(self,name,count):
#         self.item.append({'name':name,'count':count})
#         return self.item
#     def stock_count(self):
#         total = 0
#         for items in self.item:
#             total +=  items['count']
#         return total
#     @classmethod
#     def franchise(cls,obj):
#         return "It is {} Franchise".format(obj.name)
#     @staticmethod
#     def storeDetails(obj):
#         return "In {} store {} is available stock".format(obj.name,obj.item)
#         # def __repr__(self):
#         #     return "It is {} Franchise".format(obj.name)
# store = Store('Amazon')
# store.addItem('book',1)
# store.addItem('pencil',5)
# store2 = Store("Google")
# store2.addItem('SQL',2)
# store2.addItem('Chrome',5)
# print(store.stock_count())
# print(Store.franchise(store2))
# print(Store.storeDetails(store2))
####====================================================================================
# class Book:
#     Types = ["hardcopy",'paperback']
#     def __init__(self,name,type,price):
#         self.name  = name
#         self.price = price
#         self.type = type
#     @classmethod
#     def Hardcopy(cls,name,price):
#         return name,Book.Types[0],price
#     @classmethod
#     def Paperback(cls,name,price):
#         return (name,Book.Types[1],price)
#     # def __repr__(self):
#     #     return f"<Book {self.name}, type: {self.type}, price: {self.price}>"
#     @classmethod
#     def InfoMethod(cls):
#         return "this is book class"
# book1 = Book.Hardcopy('GK',500)
# print(book1)
# book2 = Book.Paperback("MOS",1000)
# # print(book2)
# book3 = Book('DOM','Paperback',125)
# print(book3.InfoMethod())
# print(book1.Hardcopy('TOM',502))
#####===============================================
# class Device:
#     def __init__(self,name,connected_by):
#         self.name = name
#         self.connected_by = connected_by
#         self.connected  = True
#     def __str__(self):
#         return f"Device {self.name!r} connected by {self.connected_by!r} connection {self.connected}"
#     def disconnect(self):
#         self.connected = False
#         return "Disconnected"
# class Printer(Device):
#     def __init__(self,name,connected_by,capacity):
#         super().__init__(name,connected_by)
#         self.capacity  = capacity
#         self.remaining_Pages = capacity
#     def __str__(self):
#         return f"{super().__str__()} {self.remaining_Pages} pages are remaining"
#     def print(self,pages):
#         if not self.connected:
#             return f"{self} not connected"
#         self.remaining_Pages -= pages
#         print(self.remaining_Pages)
# xeon_printer = Printer('Xeon1',"USB",500)
# xeon_printer.print(50)
# print(xeon_printer)
# xeon_printer.disconnect()
# Printer.print(xeon_printer,50)
# print(xeon_printer)
# print(xeon_printer)
####====================================================================
# class Device:
#     def __init__(self,name,connected_by):
#         self.name = name
#         self.connected_by = connected_by
#         self.connection_status = True
#     def disconnect_Device(self):
#         self.connection_status = False
#     def __str__(self):
#         return f"Device name: {self.name}, Connect by: {self.connected_by}, connection status: {self.connection_status}"
# class Printer(Device):
#     def __init__(self,name,connected_by,pages):
#         super().__init__(name,connected_by)
#         self.pages = pages
#     def print_pages(self,pages_print):
#         self.pages_print = pages_print
#         if not self.connection_status:
#             print("Turn on the Device")
#         else:
#             self.remaining_pages = self.pages - self.pages_print
#             self.pages = self.remaining_pages
#             print("Printing Completed",self.pages_print)
#     def __str__(self):
#         return f"{super().__str__()}, {self.remaining_pages} pages remaining"
#     def pages_remaining(self):
#         print(self.remaining_pages)
# xerox = Printer('xerox','USB',550)
# xerox.print_pages(55)
# print(xerox.pages_remaining())
# xerox.disconnect_Device()
# Printer.print_pages(xerox,50)
# Printer.print_pages(xerox,48)
# Printer.pages_remaining(xerox)
# print(xerox)
#####===============================================================
######CLASS COMPOSITION
# class BookShelf:
#     def __init__(self,*book):
#         self.book = book
#         # print(self.book)
#
#     def __str__(self):
#         return f"BookShelf contains {len(self.book)} books"
# class Book:
#     def __init__(self,book):
#         self.book = book
#     def __str__(self):
#         return f"{self.book}"
# book1 = Book("IronMan")
# book2 = Book("Thor")
# mcu = BookShelf(book1,book2)
# print(mcu)
####===========================================================
# class ToManyPagesRead(ValueError):
#     pass
# class Book:
#     pagesread = 0
#     def __init__(self,name,pages):
#         self.name = name
#         self.pages = pages
#     def read(self,num):
#         self.pagesread +=num
#         try:
#             if self.pages < self.pagesread:
#                 self.pagesread -= num
#                 raise ToManyPagesRead(f"You are trying to read more than {self.pages}")
#             else:
#                 print(f"Reading of {num} pages completed")
#         except ToManyPagesRead as E:
#             print(E)
#     def pageslefttoread(self):
#         print(self.pages-self.pagesread,"pages are available to read")
#     def totalpagesread(self):
#         print(self.pagesread,"pages are read in it this book")
#     def __str__(self):
#         return f"{self.name} is a book with {self.pages} pages and {self.pagesread} pages are read in this book"
# thor = Book("Thor",500)
# thor.read(25)
# thor.read(30)
# thor.pageslefttoread()
# thor.totalpagesread()
# thor.read(47)
# thor.totalpagesread()
# print(thor)
