from flask import abort
from flask import make_response
from flask import Flask, jsonify

app = Flask(__name__)

tasks= [
    {'id': 1,
     'title': 'Buy groceries',
     'description': 'Milk, Cheese,Pizza,Fruit, Tylenol',
     'done': False},
    {'id': 2,
     'title': 'Learn Python',
     'description': 'Get a good tutorial',
     'done': False},
]

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_tasks(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'tasks': task[0]})

if __name__ == '__main__':
    app.run(debug=True)
