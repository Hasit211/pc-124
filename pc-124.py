from flask import Flask,jsonify, request

app = Flask(__name__)

tasks = [
    {
        'Contact': 1234567890,
        'Name': 'Ravi',
        'done': False,
        'id': 1
    },
    {
        'Contact': 12304454664,
        'Name': 'Raju',
        'done': False, 
        'id': 2
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)