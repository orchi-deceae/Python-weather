from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def use1():
    return render_template('index.html')

@app.route('/notindex')
def use2():
    return 'not index.html!<p><form action="/"><button>back</button></form>'

@app.route('/get-user/<user_id>')
def get_user(user_id):
    user_data = {
        'user_id': user_id,
        'name': 'jonny test',
        'email': 'jonny@gmail.com'
    }

    extra = request.args.get('extra')
    if extra:
        user_data['extra'] = extra
        
    return jsonify(user_data), 200
    # get-user/123?extra=HelloWorld
    # query parm: extra=HelloWorld

@app.route('/create-user', methods=['POST'])
def create_user():
    data = request.get_json()

    return jsonify(data), 201
    
# GET -    Request data from a specified resource
# POST -   Create a resource 
# PUT -    Update a resource
# DELETE - Delete a resource

if __name__ == '__main__':
    app.run(debug=True) 
    # localhost: 5000




# @app.route('/')
# def home():
#     return 'Home'