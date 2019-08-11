from flask import Flask, request, jsonify, render_template
from flask_paginate import Pagination, get_page_args

from .views import get_primes, rabinMiller

application = Flask(__name__)

@application.route('/primes',  methods=['POST'])
def index():
    if request.method == 'POST':
        page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
        data = request.get_json(force=True) 
        if isinstance(data['number'], (int, long)):
            res = get_primes(data['number']+1)
            total = len(res)
            pagination_primes = paginate_result(res, offset=offset, per_page=per_page)
            pagination = Pagination(page=page, per_page=per_page, total=total,
                                css_framework='bootstrap4')
            
            return render_template('index.html',
                            numbers=pagination_primes,
                            page=page,
                            per_page=per_page,
                            pagination=pagination,
                            )
                            #per_page = current.app.config.get(per_page_name.upper(), 10)
        else:
            return render_template('error.json'), 500, {'Content-Type': 'application/json'}
    

        
def paginate_result(primes, offset=0, per_page=100):
    return primes[offset: offset + per_page]