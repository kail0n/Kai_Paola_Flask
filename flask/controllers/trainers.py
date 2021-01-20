''' Shoes controller '''
from werkzeug.exceptions import BadRequest

def index(req):
    return [t for t in trainers], 200

def show(req, uid):
    return find_by_uid(uid), 200

def find_by_uid(uid):
    try:
        return next(shoe for shoe in trainers if shoe['id'] == uid)
    except:
        raise BadRequest(f"We don't have that brand with id {uid}!")