from django.shortcuts import render, HttpResponse


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
