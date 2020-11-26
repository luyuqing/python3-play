from flask import Flask, request, jsonify
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


data = {
    "name": "testUser",
    "amount": 5.50
}


data1 = {
    "api_data": {
        "name": "testUser",
        "amount": 5.50
    }
}


data2 = {
    "api_data": {
        "api_data": {
            "name": "testUser",
            "amount": 5.50
        }
    }
}


data3 = {
    "api_data": [
        7.1,
        9.56
    ]
}


data4 = {
    "api_data": [
        {
            "x": 3.33,
            "y": 5.55
        },
        {
            "x": 17.33,
            "y": 25.55
        }
    ]
}


class TestApi(Resource):
    def get(self):
        return jsonify(data)

    def post(self):
        return jsonify(data3)


if __name__ == "__main__":
    api.add_resource(TestApi, '/')
    app.run(host='127.0.0.1', port=5000, debug=True)