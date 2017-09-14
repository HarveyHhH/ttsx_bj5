from django.shortcuts import render, redirect
from cart.models import CartsGoods
from user.models import UserInfo
from .models import OrderMain, OrderDetail
from django.db import transaction
import datetime

# Create your views here.


def order(request):
    uid = int(request.session.get('uid'))
    user = UserInfo.objects.get(pk=uid)
    cart_id_list = request.POST.getlist('cart_id')
    cart_list = CartsGoods.objects.filter(id__in=cart_id_list)
    context = {'title': '天天生鲜-提交订单', 'user': user, 'cart_list': cart_list,
               'cart_ids': ','.join(cart_id_list)}
    print(','.join(cart_id_list))
    return render(request, 'order/place_order.html', context)


@transaction.atomic
def order_submit(request):
    """
    下订单操作：
    1、创建主表
    2、接收购物车id
    3、遍历购物车
    4、判断库存数量
    5、如果库存足够则
        5.1、创建详单
        5.2、修改数量
        5.3、删除购物车
    6、如果库存不足则回滚
    7、计算总价

    """
    sid = transaction.savepoint()
    is_commit = True
    try:
        # 获取请求的购物车信息
        c_ids = request.POST.get('c_ids').split(',')
        cart_ids = []
        for i in c_ids:
            i = int(i)
            cart_ids.append(i)
        # 创建订单主表
        main = OrderMain()
        time_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        user_id = request.session.get('uid')
        main.orderid = '%s%d'%(time_str,user_id)
        main.user_id = user_id
        main.save()
        cart_list = CartsGoods.objects.filter(id__in=cart_ids)
        print(cart_list)
        total = 0
        for cart in cart_list:
            if cart.c_count<=cart.cgoods.gstore:
                # 如果库存足够则添加到详单
                detail = OrderDetail()
                detail.order = main
                detail.goods = cart.cgoods
                detail.count = cart.c_count
                detail.price = cart.cgoods.gprice
                total += cart.c_count * cart.cgoods.gprice
                detail.save()
                cart.cgoods.gstore -= cart.c_count
                cart.cgoods.save()
                # 完成订单信息保存之后，删除购物车
                cart.delete()
            else:
                # 如果库存不够则购买失败回滚
                transaction.savepoint_rollback(sid)
                is_commit = False
    except:
        is_commit = False
        transaction.savepoint_rollback(sid)
    if is_commit:
        return redirect('/user/center_order/')
    else:
        return redirect('/cart/index/')
