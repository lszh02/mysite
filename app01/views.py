from django.shortcuts import render, HttpResponse, redirect


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
    else:
        print(request.POST)
        user_name = request.POST.get('user')
        password = request.POST.get('pwd')
        if user_name == 'root' and password == '123':
            # return HttpResponse('登录成功')
            return redirect('http://www.10010.com/net5/051/')
        else:
            return render(request, 'login.html', {'error_msg': '用户名或密码错误'})
