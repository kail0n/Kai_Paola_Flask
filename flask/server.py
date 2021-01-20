from flask import Flask, g, jsonify, request
from flask_cors import CORS
from controllers import trainers
from werkzeug import exceptions
from db import get_db

server = Flask(__name__)
CORS(server)

@server.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def init_db():
    with server.app_context():
        db = get_db()
        with server.open_resource('seeds.sql', mode='r') as f:
            db.cursor().executescript(f.read())
            for row in db.execute('SELECT * FROM trainers;'):
                print(row)
        db.commit()

@server.route('/')
def home():
    return jsonify({'message': 'Hello from Flask!'}), 200

# @server.route('/api/trainers', methods=['GET', 'POST'])
@server.route('/api/trainers', methods=['GET'])
def trainer_handler():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM trainers")
    trainers = cursor.fetchall()

    return jsonify(trainers)

    # fns = {
    #     'GET': trainers
    #     } 
    # ''' 'POST': trainers.create '''
    # resp, code = fns[request.method](request)
    # return jsonify(resp), code

# @server.route('/api/trainers/<int:trainers_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
@server.route('/api/trainers/<int:trainers_id>', methods=['GET'])
def shoe_handler(trainers_id):
    fns = {
        'GET': trainers.show
        # 'PATCH': trainers.update,
        # 'PUT': trainers.update,
        # 'DELETE': trainers.destroy
    }
    resp, code = fns[request.method](request, trainers_id)
    return jsonify(resp), code

@server.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@server.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

if __name__ == "__main__":
    server.run(debug=True)
