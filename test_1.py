from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app=app)

Data = []
# class will add or delete names through API calls

class People(Resource):
    def get(self, name):
        for data in Data:
            if data['Data'] == name:
                return data
        return {'Data':'No Data available'}

    def post(self, name):
        tem = {'Data': name}
        Data.append(tem)
        return tem

    def delete(self, name):
        for index, data in enumerate(Data):
            if data['Data'] == name:
                tem = Data.pop(index)
                return{'Note': 'Deleted'}


# we will define our route
api.add_resource(People, '/people/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)