from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app=app)

# will make first resource


class Multiplication(Resource):
    def __init__(self):
        pass

    def get(self, a, b):
        return 'Result: {}'.format(a*b)

    def post(self, a, b):
        return 'Numbers are {}, {}'.format(a, b)


class squre_number(Resource):
    def get(self, c):
        # return 'Numbers is {}'.format(c) 
        return 'Square of {} is {}'.format(c, c*c)

    def post(self, c):
        return 'Numbers is {}'.format(c)   


api.add_resource(Multiplication, '/mul/<int:a>/<int:b>')
api.add_resource(squre_number, '/result/<int:c>')

if __name__ == '__main__':
    app.run(debug=True)