from django.shortcuts import render
import pandas
from pandas._libs import json
import pymysql
from  django.http import JsonResponse,HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.hashers import make_password, check_password
import requests
from .models import Restaurant,Cache,rtsp, idconfig, user

@require_http_methods(["GET"])
def search_restaurant(request):
    response = []
    result = []
    information = {'state':'1'}
    s = requests.session()
    a = s.post(
        'http://39.98.52.189:82/api/open/companyList',
        headers={'auth':'gAAAAABcfjh_HP3zWYfdz_j1Cs15uECzHHNt3ujXJtV5C_'
                        'mbWuk-xEeshqunTYacVQVglTqa1pIhaESn3iuqLu9b6UFIhZ-wt4V6hCqJX3vLFQuc5cPP1_'
                        'qPiQcsl3fH6y-NDE3TqS4qKXZY9_gUkHl09eDMZeHgxw==',
                 'Content-Type':'application/json'},
        data=json.dumps(information))
    j = json.loads(a.text)
    print(j)
    for company in j['companyList']:
        response.append({"id": company['id'], "name": company['brand']})
        result.append((company['id'],company['brand']))
        #db = pymysql.connect("127.0.0.1","root","zwd19941224","abc",charset='utf8')
        print("here")
        #cursor = db.cursor()
        #inesrt_re = "insert into configuration_restaurant(res_id,name)values(%s,%s)"
        #cursor.executemany(inesrt_re, result)
        #db.commit()
        #cursor.close()
    if response == {}:
        response = {"name": "wrong"}
    return JsonResponse(response,safe=False)

@require_http_methods(["GET"])
def search_open_restaurant(request):
    response = {'code': 20000}
    response['rows'] = []
    obj = Restaurant.objects.all()
    for it in obj:
        response['rows'].append({'id': it.res_id})
    return JsonResponse(response, safe=False)

@require_http_methods(['GET'])
def search_idconfig_by_restaurant(request):
    response = []
    res_id = request.GET.get('res_id')
    id_config = idconfig.objects.filter(res_id=res_id)
    config = id_config.first().config
    for it in id_config:
        print(it.res_id)
    if id_config:
        for i in range(int(len(config) / 45)):
            maozi = '关'
            kouzhao = '关'
            mouse = '关'
            picture = '关'
            i = i * 45
            cam_id = config[i + 1:i + 4]
            p_1 = config[i + 5:i + 7]
            p_2 = config[i + 15:i + 17]
            p_3 = config[i + 25:i + 27]
            p_4 = config[i + 35:i + 37]
            if p_1 == '11':
                maozi = '开'
            if p_2 == '21':
                kouzhao = '开'
            if p_3 == '31':
                mouse = '开'
            if p_4 == '41':
                picture = '开'
            response.append(
                {'res_id': res_id,  'cam_id': cam_id, 'maozi': maozi, 'kouzhao': kouzhao,
                 'mouse': mouse, 'picture': picture})
    else:
        response.append({'res': 'no'})
    return JsonResponse(response, safe=False)

@require_http_methods(['GET'])
def close_restaurant(request):
    response = {}
    state = request.GET.get('state')
    companyId = request.GET.get('companyId')
    s = requests.session()
    information = {'state':state,'companyId':companyId}
    a = s.put(
        'http://39.98.52.189:82/api/open/companyList',
        headers={'auth': 'gAAAAABcfjh_HP3zWYfdz_j1Cs15uECzHHNt3ujXJtV5C_'
                         'mbWuk-xEeshqunTYacVQVglTqa1pIhaESn3iuqLu9b6UFIhZ-wt4V6hCqJX3vLFQuc5cPP1_'
                         'qPiQcsl3fH6y-NDE3TqS4qKXZY9_gUkHl09eDMZeHgxw==',
                 'Content-Type':'application/json'},
        data=json.dumps(information))
    j = json.loads(a.text)
    print(j['msg'])
    if j['msg'] == 'success':
        response = {"res": "ok"}
    else:
        response = {"res": "wrong"}
    return JsonResponse(response, safe=False)

@require_http_methods(['GET'])
def change_idconfig(request):
    res_id = request.GET.get('res_id')
    config = request.GET.get('config')
    obj = idconfig.objects.filter(res_id=res_id)
    if obj:
        obj.update(res_id=res_id,config=config)
        response={'res':'yes'}
    else:
        response={'res':'no'}
    return JsonResponse(response, safe=False)

@require_http_methods(["POST"])
def change_cache(request):
    index = request.POST.get('index')
    volume = request.POST.get('volume')
    obj = Cache.objects.filter()
    if obj:
        obj.update(index = index,volume=volume)
        response={'res':'yes'}
    else:
        Cache.objects.create(index=index,volume=volume)
        response={'res':'no','but':'已默认到D:/,50'}
    return JsonResponse(response, safe=False)


@require_http_methods(['GET'])
def login(request):
    username = request.GET.get('name')
    password = request.GET.get('psw')
    res = user.objects.filter(user_name=username)
    result = check_password(password, res.first().user_password)
    if result:
        response = {"info": "ok"}
    else:
        response = {"info": "no"}
    return JsonResponse(response, safe=False)