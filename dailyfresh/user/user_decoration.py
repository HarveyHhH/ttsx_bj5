from django.shortcuts import redirect


# 判断用户登录状态：未登录，禁止访问一些页面，并返回至登录页面
def log_status(func):
    def func1(request, *args, **kwargs):
        if request.session.has_key('uid'):
            return func(request,*args,**kwargs)
        else:
            return redirect('/user/login/')
    return func1