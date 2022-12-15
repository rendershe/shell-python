from django.http import JsonResponse
from django.db.models import F
from django.db import IntegrityError, transaction
import time
from  common.models import  Order,OrderMedicine

import json

def dispatcher(request):

    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
            'msg': 'unlogged',
            'redirect': '/mgr/sign.html'},
            status=302)

    if request.session['usertype'] != 'mgr':
        return JsonResponse({
            'ret': 302,
            'msg': 'User non-mgr type',
            'redirect': '/mgr/sign.html'},
            status=302)


    if request.method == 'GET':
        request.params = request.GET

    elif request.method in ['POST','PUT','DELETE']:

        request.params = json.loads(request.body)


    action = request.params['action']
    if action == 'list_order':
        return listorder(request)
    elif action == 'add_order':
        return addorder(request)



    else:
        return JsonResponse({'ret': 1, 'msg': 'No class type HTTP request'})
