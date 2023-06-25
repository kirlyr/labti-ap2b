from flask import Flask, jsonify, request

app = Flask(__name__)
stores = [
    {
        'name': 'Toko Roti',
        'items': [
            {
                'name': 'Roti Tawar',
                'price': 9000
            }
        ]
    },
    {
        'name': 'Toko Ikan',
        'items': [
            {
                'name': 'Ikan Cupang',
                'price': 2500
            }
        ]
    }
]

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'Store not found'})

@app.route('/store/<string:name>/item')
def get_store_items(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return jsonify({'message': 'Store not found'})

@app.route('/store', methods=["POST"])
def create_store():
    req_data = request.get_json()
    new_store = {
        'name': req_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    for store in stores:
        if store['name'] == name:
            req_data = request.get_json()
            new_item = {
                'name': req_data['name'],
                'price': req_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)

@app.route('/')
def home():
    return "t t t t t tengkyu"

if __name__ == '__main__':
    app.run(debug=True, port=8000)
