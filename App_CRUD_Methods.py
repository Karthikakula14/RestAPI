# from flask import Flask,jsonify,request,render_template
#
# app = Flask(__name__)
#
# stores = [{
#     'name': 'My Store',
#     'items': [{'name':'my item', 'price': 15.99 }]
# }]

# @app.route('/')
# def home():
#     return "Checking"
  # return render_template('index.html')
#
# #post /store data: {name :}
# @app.route('/store' , methods=['POST'])
# def create_store():
#   request_data = request.get_json()
#   new_store = {
#     'name':request_data['name'],
#     'items':[]
#   }
#   stores.append(new_store)
#   return jsonify(new_store)
#   #pass
#
# #get /store/<name> data: {name :}
# @app.route('/store/<string:name>')
# def get_store(name):
#   for store in stores:
#     if store['name'] == name:
#           return jsonify(store)
#   return jsonify ({'message': 'store not found'})
#   #pass
#
# #get /store
# @app.route('/store')
# def get_stores():
#   return jsonify({'stores': stores})
#   #pass
#
# #post /store/<name> data: {name :}
# @app.route('/store/<string:name>/item' , methods=['POST'])
# def create_item_in_store(name):
#   request_data = request.get_json()
#   for store in stores:
#     if store['name'] == name:
#         new_item = {
#             'name': request_data['name'],
#             'price': request_data['price']
#         }
#         store['items'].append(new_item)
#         return jsonify(new_item)
#   return jsonify ({'message' :'store not found'})
#   #pass
#
# #get /store/<name>/item data: {name :}
# @app.route('/store/<string:name>/item')
# def get_item_in_store(name):
#   for store in stores:
#     if store['name'] == name:
#         return jsonify( {'items':store['items'] } )
#   return jsonify ({'message':'store not found'})
#
#   #pass
#
# app.run(port=5000)
######=========================
from flask import Flask,jsonify,request,render_template
app = Flask(__name__)
app.run(port = 3500)
@app.route('/')
def Home():
    # pass
    return render_template('index.html')

# # print(app)
stores = [
            {
     'name':"Amazon",
        'item':[
                {'name': 'Books',
                 'price': 20
                 }
                ]
            }
        ]

####ENDPOINTS
# POST -- Used to receive data
# GET -- Used to send data back only

# POST /store data: {name:} -- Create a new store with a given name in the DB


@app.route('/store',methods = ['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {"name":request_data['name'],
                 "item":[]}
    stores.append(new_store)
    return jsonify({"new store":new_store})


@app.route('/store',methods = ['DELETE'])
def del_store():
    request_data = request.get_json()
    for store in stores:
        if store["name"] == request_data["name"]:
            stores.pop(stores.index(store))
            return jsonify(stores)
    return jsonify({"Message:": "Store not found"})



@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if name == store["name"]:
            return jsonify(store)
    return jsonify({"Message": "Store not found"})


@app.route('/store')  # http://127.0.0.1:500/store
def get_store_list():
    return jsonify({'store': stores})


@app.route('/store/<string:name>/item',methods = ['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    new_item = {'name':request_data['name'],'price':request_data['price']}
    for store in stores:
        if store['name'] == name:
            store["item"].append(new_item)
            return jsonify(new_item)
    return jsonify({'Message ': " Store not found"})



@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({"items":store['item']})
    return jsonify({"Message: ": "Store not found"})


@app.route('/store/<string:name>/item',methods = ["PUT"])
def update_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            for item in store["item"]:
                if item["name"] == request_data["item"]:
                    item["price"] = request_data["price"]
                    return jsonify(item)
            return jsonify({"message":"item not found"})
        return jsonify({"message":"Store not found"})

@app.route('/store/<string:name>/item',methods = ["DELETE"])
def delete_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            for i in store["item"]:
                if i["name"] == request_data["item"]:
                    store["item"].remove(i)
                    return jsonify({"items": store["item"]})
            return jsonify({"message":"item not found"})
    return jsonify({"message": "Store not found"})

# @app.route('/store',methods = ["DELETE"])
# def delete_item_in_store():
#     request_data = request.get_json()
#     for store in stores:
#         if store["name"] == request_data["store"]:
#             for i in store["item"]:
#                 if i["name"] == request_data["item"]:
#                     store["item"].remove(i)
#                     return jsonify({"items": store["item"]})
#             return jsonify({"message":"item not found"})
#     return jsonify({"message": "Store not found"})
#####=============================================