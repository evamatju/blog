#coding=utf-8
from django.shortcuts import render_to_response,HttpResponseRedirect,HttpResponse
from blog.article.models import Article,Order,Device
import json
import time
from django.http import JsonResponse
# Create your views here.


def rejson(error=False,msg='',username=None):
    if error:
        code = 101
    else:
        code = 100
    if username:
        result = {'error': error, 'result': {'msg': msg, 'code': code,'username':username}}
    else:
        result = {'error': error, 'result': {'msg': msg, 'code': code}}
    return result


def user_in(username):
    user_loggedin = Article.objects.filter(username=username)
    return user_loggedin


def home(request):

    py = {'foo': 'bar'}
    a = json.dumps(py, sort_keys=True, ensure_ascii=False)
    print type(a)
    HttpResponse(a)
    return JsonResponse({'a':'低'})


def admin_login(request):

    # if request.method == 'POST':
    #
    #     username = request.POST.get('name',None)
    #     password = request.POST.get('pw',None)
    #     #user = Article.objects.filter(username=username,password=password)
    #     if username == 'admin' and password == 'admin':
    #         request.session['username'] = username
    #         return JsonResponse(rejson(False, 'you are logged in !'))
    #
    #     username = request.session.get('username',None)
    #     if username == 'admin':
    #        # return render_to_response('admin_login.html',{'username':username})
    #         return JsonResponse(rejson(False,'you are logged in !'))
    #     try:
    #         m = Article.objects.get(username=username)
    #         if m.password == password:
    #     #  return render_to_response('admin_login.html',{'username':username})
    #             return JsonResponse(rejson(False,'you are logged in !'))
    #     except Article.DoesNotExist:
    #         return JsonResponse(rejson(True,'you are not logged in !'))
    # return render_to_response('admin_login.html')

    username = request.session.get('username', None)
    if user_in(username) or username == 'admin':
        response = JsonResponse(rejson(False, 'you are logged in !', username))
        response.set_cookie("username",
                            username)
        return response
    if request.method == 'POST':
        username = request.POST.get('name', None)
        password = request.POST.get('pw',None)
        if username == 'admin' and password == 'admin':
            request.session['username'] = username
            response = JsonResponse(rejson(False, 'you are logged in !', username))
            response.set_cookie("username",
                                username)
            return response

        user = Article.objects.filter(username=username,pw=password)
        if user:
            request.session['username'] = username
            response = JsonResponse(rejson(False, 'you are logged in !', username))
            response.set_cookie("username",
                                username)
            return response
        else:
            return JsonResponse(rejson(True, 'you are not logged in !'))
    return render_to_response('admin_login.html')

def admin_logout(request):
    try:
        del request.session['username']
        response = JsonResponse(rejson(False,'you are logged out !'))
        response.delete_cookie("username")
    except KeyError:
        return JsonResponse(rejson(True,'failed to log out !'))
    return response

def add(request):
    username = request.session.get('username', None)
    # print username
    # m = Article.objects.get(username=username)
    if user_in(username) or username == 'admin':
        if request.method == 'POST':
            get_username = request.POST.get('name',None)
            get_password = request.POST.get('pw',None)
            get_level = request.POST.get('level', None)
            try:
                new = Article(username=get_username,pw=get_password,level=get_level)
                new.save()
            except:
                return JsonResponse(rejson(True,'failed to add user !'))
            return JsonResponse(rejson(False, 'add order successfully!'))
        return render_to_response('add.html')
    return JsonResponse(rejson(True, 'please login!'))

def del_user(request):
    username = request.session.get('username', None)
    if user_in(username) or username == 'admin':
        #articles = Article.objects.order_by('-id').all()
        if request.method == 'POST':
            get_username = request.POST.get('name', None)
            try:
                userdel = Article.objects.get(username=get_username)
                userdel.delete()
            except:
                return JsonResponse(rejson(True,'failed to del user!'))
            return JsonResponse(rejson(False,'delete user successfully!'))
        return render_to_response('del_user.html')
    return JsonResponse(rejson(True, 'please login!'))

def get_user(request):
    if request.method == 'GET':
        userlist = []
        try:
            users = Article.objects.order_by('-id').all()
            for i in users:
                userdic = {'name':i.username,'password':i.pw,'level':i.level}
                userlist.append(userdic)
        except:
            return JsonResponse(rejson(True, 'failed to get users!'))
        return JsonResponse({'error':False,'result':userlist})
    return JsonResponse(rejson(True,'failed to get users!'))


def ch_pw(request):
   # username = request.session.get('username', None)
   # if user_in(username) or username == 'admin':
    if request.method == 'POST':
        get_name = request.POST.get('name', None)
        get_pw = request.POST.get('oldPw',None)
        get_newpw = request.POST.get('newPw',None)
        try:
            m = Article.objects.get(username=get_name, pw=get_pw)
            m.pw = get_newpw
            m.save()
        #  return render_to_response('admin_login.html',{'username':username})
        except Article.DoesNotExist:
            return JsonResponse(rejson(True,'failed to change !'))
        return JsonResponse(rejson(False, 'changed successfully !'))

    return render_to_response('ch_pw.html')
   # return JsonResponse(rejson(True, 'please login!'))

def list(request):
    username = request.session.get('username', None)
    if user_in(username) or username == 'admin':
        articles = Article.objects.order_by('-id').all()

        return render_to_response('list.html',{'articles':articles})
    return HttpResponseRedirect('/login/')

def add_order(request):
    username = request.session.get('username', None)
    if user_in(username) or username == 'admin':
        if request.method == 'POST':
            get_ordername = request.POST.get('orderName',None)
            get_type = request.POST.get('type',None)
            get_detail = request.POST.get('detail', None)
            get_operator = request.POST.get('operator', None)
            get_publisher = username
            a = time.time()
            get_orderid = int(a)
            #get_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(a))
            try:
                new = Order(publisher=get_publisher,operator=get_operator,orderId=get_orderid,name=get_ordername,detail=get_detail,type=get_type)
                new.save()
            except:
                return JsonResponse(rejson(error=True,msg='failed to add order !'))

            return JsonResponse(rejson(error=False,msg='add order successfully !'))
        return render_to_response('add_order.html')
    return JsonResponse(rejson(True, 'please login!'))

def list_order(request):
    username = request.session.get('username', None)
    if user_in(username) or username == 'admin':
        orders = Order.objects.order_by('-id').all()

        return render_to_response('list_order.html',{'orders':orders})
    return HttpResponseRedirect('/login/')

def get_order(request):
    # username = request.session.get('username', None)
    # if user_in(username) or username == 'admin':
        if request.method == 'GET':
            get_type = request.GET.get('type',None)
            get_id = request.GET.get('orderid', None)
            if get_type:
                if get_type == 'all':
                    get_orders = Order.objects.all()
                elif get_type == 'normal' or get_type == 'critical':
                    get_orders = Order.objects.filter(type=get_type)
                elif get_type == 'done':
                    get_orders = Order.objects.filter(progress=100)
                else :
                    get_orders = Order.objects.filter(progress__lt=100)
            if get_id:
                get_orders = Order.objects.filter(orderId=get_id)
            orderlist = []
            try:
                for i in get_orders:
                    orderdic = {'id':i.orderId,'name':i.name,'detail':i.detail,'type':i.type,'date':i.date,'publisher':i.publisher,'operator':i.operator,'progress':i.progress}
                    orderlist.append(orderdic)
            except:
                return JsonResponse({'error': True, 'result': orderlist})

            return JsonResponse({'error':False,'result':orderlist})
        return JsonResponse(rejson(True,'failed to get order!'))
    # return JsonResponse(rejson(True, 'please login!'))

def device_query(request):
    # username = request.session.get('username', None)
    # if user_in(username) or username == 'admin':
        if request.method == 'POST':
            get_did = request.POST.get('key',None)
            try:
                devices = Device.objects.get(deviceId=get_did)
                devicedic = {'deviceId': devices.deviceId, 'name': devices.name, 'type': devices.type,
                         'detail': devices.detail}
            except:
                return JsonResponse({'error': True, 'result': devicedic})

            return JsonResponse({'error': False, 'result': devicedic})
        return render_to_response('device_query.html')
    # return JsonResponse(rejson(True, 'please login!'))

def del_order(request):
    username = request.session.get('username', None)
    if user_in(username) or username == 'admin':
        if request.method == 'POST':
            get_orderid = request.POST.get('orderId', None)
            try:
                orderdel = Order.objects.get(orderId=get_orderid)
                orderdel.delete()
            except:
                return JsonResponse(rejson(True,'failed to del order!'))
            return JsonResponse(rejson(False,'delete order successfully!'))
        return render_to_response('del_order.html')
    return JsonResponse(rejson(True, 'please login!'))

def ch_order(request):
    username = request.session.get('username', None)
    if user_in(username) or username == 'admin':
        if request.method == 'POST':
            get_orderid = request.POST.get('orderId', None)
            get_type = request.POST.get('type', None)
            get_detail = request.POST.get('detail', None)
            get_operator = request.POST.get('operator', None)
            get_progress = request.POST.get('progress', None)
            get_name = request.POST.get('name', None)
            print get_operator
            try:
                chorder = Order.objects.get(orderId=get_orderid)
                chorder.type = get_type
                chorder.detail = get_detail
                chorder.operator = get_operator
                chorder.progress = get_progress
                chorder.name = get_name
                chorder.save()
            except:

                return JsonResponse(rejson(True,'failed to change order!'))
            return JsonResponse(rejson(False,'change order successfully!'))
        return render_to_response('ch_order.html')
    return JsonResponse(rejson(True, 'please login!'))