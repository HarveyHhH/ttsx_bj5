from django.shortcuts import render
from .models import TypeInfo, GoodsInfo
from django.core.paginator import Paginator
from django.http import JsonResponse

# Create your views here.


def index(request):
    # 得到商品的种类列表
    type_list = TypeInfo.objects.all()
    # 遍历列表,查询每个种类符合要求的商品
    list_data = []
    for type_x in type_list:
        # 获取最新添加的四个商品
        new_list = type_x.goodsinfo_set.order_by('-id')[0:4]
        # 获取点击量最大的四件商品
        click_list = type_x.goodsinfo_set.order_by('-gclick')[0:4]
        list_data.append({'new_list':new_list, 'click_list':click_list,'t1':type_x})
    context = {'choice': 1,'title':'首页-天天生鲜','list_data': list_data}
    return render(request, 'goods/index.html', context)


def list(request,tid,pindex,sorts):
    # 根据tid提取对应id的商品类别对象
    type_x = TypeInfo.objects.get(id=int(tid))
    # 获取最新添加的商品作为新品推荐
    new_list = type_x.goodsinfo_set.order_by('-id')[0:2]
    # 获取该商品类别下的所有商品(以id排序-默认)
    goods_list = type_x.goodsinfo_set.order_by('-id')
    desc = '1'
    if int(sorts) == 2:
        # 点击一次，价格升序，再点击一次，价格降序。 通过自定义过滤器，get方式传参达到效果
        desc = request.GET.get('desc')
        if desc == '1':
            goods_list = type_x.goodsinfo_set.order_by('gprice')
        else:
            goods_list = type_x.goodsinfo_set.order_by('-gprice')
    if int(sorts) == 3:
        goods_list = type_x.goodsinfo_set.order_by('-gclick')
    # 将good_list分页
    paginator = Paginator(goods_list, 15)
    p_index = paginator.page(pindex)
    context = {'title':'天天生鲜-商品列表','choice': 1,'new_list':new_list,'p_index':p_index, 't_x': type_x,'sorts':sorts,
               'desc':desc}
    return render(request,'goods/list.html',context)


""" post vs csrf 此种方法采用js的ajax局部刷新的方法，需要同时处理上部价格、人气与下部页码两部分的点击事件
def list_check(request):
    tid = request.POST.get('id')
    choice = request.POST.get('val')
    print(choice)
    type_x = TypeInfo.objects.get(id=int(tid))
    # 判断点击的类别
    if choice == '价格':
        goods_list =type_x.goodsinfo_set.order_by('-gprice')
    elif choice == '人气':
        goods_list =type_x.goodsinfo_set.order_by('-gclick')
    else:
        goods_list =type_x.goodsinfo_set.order_by('-id')
    paginator = Paginator(goods_list,15)
    p_index = paginator.page(1)
    Str = ''
    for item in p_index:
        Str = Str + '<li><a href="detail.html"><img src="/static/'+str(item.gpic)+'"></a><h4><a href="detail.html">'+str(item.gtitle)+'</a></h4><div class="operate"><span class="prize">￥'+str(item.gprice)+'</span><span class="unit">'+str(item.gprice)+'/'+str(item.gunit)+'</span><a href="#" class="add_goods" title="加入购物车"></a></div></li>'
    return JsonResponse({'a':Str})
"""


def detail(request,gid):
    try:
        goods = GoodsInfo.objects.get(id=int(gid))
    except:
        return render(request,'404.html')
    else:
        goods.gclick +=1
        goods.save()
        type_x = goods.gtype
        new_list = type_x.goodsinfo_set.order_by('-id')[0:2]
        context = {'new_list':new_list,'goods':goods,'choice':1,'title':'商品详情'}
        response = render(request,'goods/detail.html',context)
        # cookie的存储方式为键值对，同一个键只能存储一个值，意味着需将id以字符串格式存储
        # 得到一个字符的列表
        ids = request.COOKIES.get('ids','').split(',')
        if gid in ids:
            ids.remove(gid)
        ids.insert(0,gid)
        # 只存储5个id值
        if len(ids)>5:
            ids.pop()
        response.set_cookie('ids',','.join(ids),max_age=60*60*24*7)
        return response


