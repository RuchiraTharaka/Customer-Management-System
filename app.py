from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample customer data
customers = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com"},
    {"id": 3, "name": "Alice Johnson", "email": "alice@example.com"},
    {"id": 4, "name": "Bob Brown", "email": "bob@example.com"},
    {"id": 5, "name": "Charlie Davis", "email": "charlie@example.com"}
]

# Create a new customer
@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    new_id = max(c['id'] for c in customers) + 1
    new_customer = {"id": new_id, "name": data['name'], "email": data['email']}
    customers.append(new_customer)
    return jsonify(new_customer), 201

# Read all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify(customers)

# Read a specific customer by ID
@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = next((c for c in customers if c['id'] == customer_id), None)
    if customer is None:
        return jsonify({'error': 'Customer not found'}), 404
    return jsonify(customer)

# Update a customer by ID
@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    data = request.get_json()
    customer = next((c for c in customers if c['id'] == customer_id), None)
    if customer is None:
        return jsonify({'error': 'Customer not found'}), 404
    
    customer['name'] = data.get('name', customer['name'])
    customer['email'] = data.get('email', customer['email'])
    return jsonify(customer)

# Delete a customer by ID
@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    global customers
    customers = [c for c in customers if c['id'] != customer_id]
    return jsonify({'message': 'Customer deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)