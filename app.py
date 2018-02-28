from flask import Flask

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

def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)
