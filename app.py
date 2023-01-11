from flask import Flask, make_response, jsonify, request
from db.dbConfig import database_conn

app = Flask(__name__)


def create_app():
    app.config['JSON_SORT_KEYS'] = False
    database_conn()
    return app


@app.route('/clients', '[GET]')
def get_clients():
    return make_response(jsonify(
        mensagem='Lista de clientes',
        dados="clients"
    ))


@app.route('/clients', '[GET]')
def get_clients_by_id():

    return "return clients by id"


@app.route('/clients', methods='[POST]')
def post_clients():
    return "hello"


if __name__ == '__main__':
    app = create_app()
    app.run(port=8080)
