from flask import Flask, jsonify, request

app = Flask(__name__)
stores = [
    {
        'name':'Hello Store',
        'items': [
            {
                'name':'mango',
                'price': 110
            },
            {
                'name':'apple',
                'price': 65
            }
        ]
    }

]

# get stores
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# post create store
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# get store by name
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'store not found'})

# post create item in store
@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})

# get item in store
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return jsonify({'message': 'store not found'})

app.run(debug=True, port=5000)