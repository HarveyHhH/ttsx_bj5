from django.shortcuts import render, redirect
from .models import UserInfo
from hashlib import sha1
from django.http import JsonResponse

# Create your views here.


# 返回注册页面j
def register(request):
    return render(request,'user/register.html')


# 注册信息判断与记录
def register_log(request):
    # 用于判断是否存在重名的用户
    if request.method == 'GET':
        user_name = request.GET.get('username')
        result = UserInfo.objects.filter(uname=user_name)
        # Json不能传递对象
        result = len(result)
        return JsonResponse({'data': result})
    else:
        user = UserInfo()
        # 获取表单提交信息, 并存储至数据库
        post = request.POST
        user.uname = post.get('user_name')
        user.umail = post.get('user_email')
        # 密码加密
        s1 = sha1()
        s1.update(post.get('user_pwd').encode())
        user.upwd = s1.hexdigest()
        user.save()
        return redirect('/user/login/')


# 返回登入界面
def login(request):
    uname = request.COOKIES.get('uname','')
    return render(request,'user/login.html',{'uname':uname})


# 判断登入界面输入的信息是否匹配，登入成功转入用户中心界面
def login_check(request):
    # 用模板语言变量将数据库中的信息传给页面
    name = request.POST.get('username')
    request.session['h1']='hello'
    pwd = request.POST.get('pwd').encode()
    umemory = request.POST.get('memory',0)
    print(umemory)
    # sha1加密
    s1 = sha1()
    s1.update(pwd)
    pwd = s1.hexdigest()
    result = UserInfo.objects.filter(uname=name)
    if len(result) == 0:
        return render(request, 'user/login.html',{'data':1})
    else:
        if result[0].upwd == pwd:
            response = redirect('/user/center_info/')
            request.session['uid'] = result[0].id
            if umemory == '1':
                response.set_cookie('uname',name)
            else:
                response.set_cookie('uanme','',max_age=-1)
            return response
        else:
            return render(request, 'user/login.html',{'data':2})


def center_info(request):
    user = UserInfo.objects.get(pk=request.session['uid'])
    context = {'choice':0,'title':'天天生鲜-用户中心','user':user}
    return render(request, 'user/center_info.html',context)


def center_order(request):
    context = {'title':'天天生鲜-用户中心'}
    return render(request, 'user/center_order.html', context)


def center_site(request):
    user = UserInfo.objects.get(pk=request.session['uid'])
    if request.method == 'POST':
        post = request.POST
        urecv = post.get('urecv')
        uaddress = post.get('uaddress')
        ucode = post.get('ucode')
        uphone = post.get('uphone')

        user.urecv = urecv
        user.uaddress = uaddress
        user.ucode = ucode
        user.uphone = uphone
        user.save()
    context = {'user': user}
    return render(request, 'user/site.html', context)
