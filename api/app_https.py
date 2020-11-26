from flask import Flask, request, jsonify
from flask_restful import Resource, Api


import ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('/home/ubuntu/aaaaa/systest.crt', '/home/ubuntu/aaaaa/systest.key')

app = Flask(__name__)
api = Api(app)


books = [
    {'book_name': 'Crazy Rich Asians', 'book_price': 9.99, 'book_rating': 4.5},
    {'book_name': 'Harry Potter', 'book_price': 8.99, 'book_rating': 4.6},
    {'book_name': 'Two And A Half Men', 'book_price': 5.99, 'book_rating': 4.3}
]


class BookStore(Resource):
    def get(self):
        return jsonify(books)

    def post(self):
        print("###############################")
        print(request.json)
        book_name = request.json.get('book_name')
        for book in books:
            if book['book_name'] == book_name:
                return jsonify(book)
        else:
            return jsonify('Book not found')


if __name__ == "__main__":
    api.add_resource(BookStore, '/')
    app.run(host='127.0.0.1', port=5000, debug=True, ssl_context=context)
