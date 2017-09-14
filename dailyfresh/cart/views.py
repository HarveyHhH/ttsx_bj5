from django.shortcuts import render, redirect
from goods.models import GoodsInfo
from user.models import UserInfo
from .models import CartsGoods
from django.http import JsonResponse
from user.user_decoration import log_status
import time

# Create your views here.


def cart(request):
    return render(request, 'cart/cart.html')


def cart_add(request):
    # 判断登入状态
    if request.session.has_key('uid'):
        info_id = int(request.GET.get('info_id'))
        count = int(request.GET.get('count',1))
        uid = int(request.session.get('uid'))
        cart = CartsGoods.objects.filter(cgoods_id=info_id,cuser_id=uid)
        if len(cart) == 1:
            cart1 = cart[0]
            cart1.c_count += count
            cart1.save()
        else:
            cart_goods = CartsGoods()
            cart_goods.cgoods = GoodsInfo.objects.get(id=info_id)
            cart_goods.cuser = UserInfo.objects.get(id=uid)
            cart_goods.c_count = count
            cart_goods.save()
        f_count = CartsGoods.objects.filter(cuser_id=uid).count()
        print(f_count)
        return JsonResponse({'data': f_count})
    else:
        return redirect('/user/login/')


def record(request):
    uid = int(request.session.get('uid'))
    gid = int(request.GET.get('gid'))
    count = int(request.GET.get('count'))
    # cart_id = int(request.GET.get('cart_id')) 将该项的ID传过来进行查询
    cart = CartsGoods.objects.filter(cuser_id=uid,cgoods_id=gid)[0]
    cart.c_count = count
    cart.save()
    return JsonResponse({'OK': 1})


def delete(request):
    uid = int(request.session.get('uid'))
    gid = int(request.GET.get('gid'))
    cart = CartsGoods.objects.filter(cuser_id=uid,cgoods_id=gid)[0]
    cart.delete()
    # time.sleep(3)
    return JsonResponse({'OK': 1})


def delete2(request):
    id = int(request.GET.get('id'))
    cart = CartsGoods.objects.get(pk=id)
    cart.delete()
    return JsonResponse({'OK': 1})


def count(request):
    uid = int(request.session.get('uid'))
    count1 = CartsGoods.objects.filter(cuser_id=uid).count()
    return JsonResponse({'count':count1})


@log_status
def index(request):
    uid = int(request.session.get('uid'))
    cart_list = CartsGoods.objects.filter(cuser_id=uid)
    context = {'title': '购物车','cart_list': cart_list}
    return render(request, 'cart/cart.html',context)


"""
def cart_init(request):
    g_id = int(request.GET.get('g_x'))
    u_id = int(request.session.get('uid'))
    cart = CartsGoods.objects.filter(cuser_id=u_id).filter(cgoods_id=g_id)
    print(len(cart))
    c_count = cart[0].c_count
    return JsonResponse({'data': c_count})
"""
