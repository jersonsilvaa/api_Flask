from flask import Flask, jsonify, request
import json

from products import products
app=Flask(__name__ )

#######verificar conexion#########
@app.route('/ping',methods=['GET'])
def ping():
    return jsonify({"message":"Funciona"})


#######lista de productos#########
@app.route('/products',methods=['GET'])
def getProducts():
    with open('prueba.json') as json_file:
        data = json.load(json_file)
    return jsonify({"products": data,",message":"Lista de productos"})


#######agrega un nuevo prodcuto#########   
@app.route('/sendproducts',methods=['POST'])
def addProduct():
    new_product = {
        "name":request.json['name'],
        "price":request.json['price'],
        "quantity":request.json['quantity']
    }
    products.append(new_product)
    with open('prueba.json', 'w') as json_file:
        json.dump(products, json_file)    
    return jsonify({"message": "product added sussefuly","products":products})


@app.route('/products/<string:product_name>',methods=['GET'])
def getProduct(product_name):
    resultado = "null"
    with open('prueba.json') as json_file:
        data = json.load(json_file)
        
        for item in data:
                
            if(item['name']==product_name):
                resultado =  [
                {  "name" : item['name'],
                    "price" : item['price'],
                    "quantity" : item['quantity']
                } ,
                
                ]
    if(resultado=="null"):
        return jsonify({"message": "product not found"})
    else:
        return jsonify({"products": resultado,",message":"Lista de productos"})
     

'''
    
    with open('prueba.json') as file:
        
        info = json.loads(file)
        print('User count:', len(info))
 
        for item in info:
            print('name', item['name'])
            print('price', item['price'])
            print('quantity', item['quantity'])

    return jsonify({"products":info})
'''
           
'''      
    if(len(product_found)>0):
        return jsonify({"products":product_found[0]})
    else:
         return jsonify({"message": "product not found"})

'''



        


'''
@app.route('/products/<string:product_name>',methods=['DELETE'])
def deleteProduc(product_name):
    product_found=[product for product in products if product['name']==product_name ]
    if(len(product_found)>0):
        products.remove(product_found[0])
        return jsonify({"message": "product delete sussefuly","products":products})
    return jsonify({"message": "product not found"})



@app.route('/products/<string:product_name>',methods=['PUT'])
def editProduct(product_name):
    product_found=[product for product in products if product['name']==product_name ]
    if(len(product_found)>0):
        product_found[0]['name']=request.json['name']
        product_found[0]['price']=request.json['price']
        product_found[0]['quantity']=request.json['quantity']
        return jsonify({"message": "product update sussefuly","products":products})
    return jsonify({"message": "product not found"})
'''




if __name__=='__main__':
    app.run(debug=True, port=4000)