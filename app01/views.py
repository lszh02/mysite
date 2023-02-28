from django.shortcuts import render, HttpResponse, redirect

from app01.models import Department, UserInfo


def index(request):
    return HttpResponse('欢迎使用')


def user_list(request):
    return render(request, "../templates/user_list.html")


def user_add(request):
    return HttpResponse('用户添加')


def tpl(request):
    name = "德克士"
    roles = ["管理员", "CEO", "保安"]
    user_info = {'name': "德克士", 'salary': 95000, 'role': 'CEO'}
    return render(request, 'tpl.html', {'n1': name, 'n2': roles, 'n3': user_info})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    print(request.POST)
    user_name = request.POST.get('user')
    password = request.POST.get('pwd')
    if user_name == 'root' and password == '123':
        # return HttpResponse('登录成功')
        return redirect('http://www.10010.com/net5/051/')

    # return HttpResponse('登录失败')
    return render(request, 'login.html', {'error_msg': '用户名或密码错误'})


def orm(request):
    # """新建数据"""
    # Department.objects.create(title='销售部')
    # Department.objects.create(title='运营部')
    # Department.objects.create(title='售后部')
    # UserInfo.objects.create(name='陈奕迅', password='123', age=22)
    # UserInfo.objects.create(name='周杰伦', password='666', age=28)
    #
    # """删除数据"""
    UserInfo.objects.filter(id=1).delete()
    # Department.objects.all().delete()

    """获取数据"""
    # queryset = UserInfo.objects.all()
    # print(queryset)
    # for obj in queryset:
    #     print(obj.id, obj.name, obj.age)
    # 获取一条数据
    # row_obj = UserInfo.objects.filter(id=1).first()
    # print(row_obj.id, row_obj.name)

    """更新数据"""
    # UserInfo.objects.all().update(password=123456)
    # UserInfo.objects.filter(name='zsl').update(password=8888888)

    return HttpResponse('成功')


def info_list(request):
    # 获取所有用户信息
    data_list = UserInfo.objects.all()
    print(data_list)

    return render(request, 'info_list.html', {'data_list': data_list})


def info_add(request):
    if request.method == 'GET':
        return render(request, 'info_add.html')

    # 获取用户提交数据
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')

    # 添加到数据库
    UserInfo.objects.create(name=user, password=pwd, age=age)

    # 自动跳转
    return redirect('/info/list/')
