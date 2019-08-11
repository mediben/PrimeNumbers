from flask import Flask, request, jsonify
from .views import get_primes

application = Flask(__name__)

@application.route('/primes',  methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json(force=True) 
        res = get_primes(data)
        return jsonify(msg=res)
    
    elif request.method == 'GET':
        pass
        
