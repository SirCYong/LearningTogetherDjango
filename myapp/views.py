import json

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from myapp.models import Class, Student


def index(request):
    return HttpResponse("cy is good man")


def detail(request, **kwargs):
    return HttpResponse("detail {0}, {1}".format(kwargs['num'], kwargs['num2']))


def myapp_class(request, **kwargs):
    # 去模型中取数据
    class_list = Class.objects.all()
    # 将数据传递给模板，，，模板渲染页面 然后 返回给浏览器
    return render(request, 'myapp/class.html', {'Class': class_list})


def student_info(request, **kwargs):
    print(kwargs)
    # user_id = int(kwargs['user_id'])
    user_id = kwargs['user_id']

    # user_id = int(user_id)
    one_student_info = Student.objects.get(id=user_id)
    print(one_student_info)
    print(type(one_student_info))
    return render(request, 'myapp/student_info.html', {'student_info': one_student_info})


def myapp_student(request):
    student_list = Student.objects.all()
    return render(request, 'myapp/student.html', {'student': student_list})


def class_student(request, class_id):
    one_class = Student.objects.filter(sclass_id=class_id)
    # one_class_student = one_class.student_set.all()
    return render(request, 'myapp/class_and_student.html', {'student': one_class})


def view_delete_student(request):
    student = Student.driver.all()
    return render(request, 'myapp/view_delete_student.html', {'delete_student': student})


def add_student(request):
    from faker import Faker
    f = Faker(locale='zh_CN')
    name = f.name()
    sex = f.boolean()
    import random
    age = random.randint(18, 26)
    contend = f.sentences()
    all_class_id = Class.objects.all()
    class_id = random.choice(all_class_id)
    # from myapp.models import create_student  # 是用的方法 对应第三种写法
    # student = create_student(name, sex, age, contend, class_id)  # 对应第三种写法
    # student = Student().create_student(name, sex, age, contend, class_id)  # 对应 models 的第二种写法
    # student = Student.create_student(name, sex, age, contend, class_id)  # 对应第一种写法
    student = Student.driver.create_student(name, sex, age, contend, class_id)  # 对应第四种写法
    student.save()
    return HttpResponse("学生 {0}添加成功,关联在{1}".format(name, class_id))


def student_page(request, page):
    page = int(page)
    limit = 5
    student = Student.objects.all()[(page - 1) * limit: page * limit]
    return render(request, 'myapp/student.html', {'student': student})


def hello_world(request):
    print(type(request))
    print(request)
    print('get:', request.GET)

    if request.GET.get('num', False) :
        resp = {'code': 1000, 'detail': 'success! hello'}
    else:
        resp = {'code': 2100, 'detail': 'fail'}

    return HttpResponse(json.dumps(resp), content_type="application/json")


def attribute(request):
    """查看他们的属性"""
    print("path:", request.path)
    print('method:', request.method)
    print('encoding:', request.encoding)
    print('get:', request.GET)
    print('post:', request.POST)
    print('cookies:', request.COOKIES)
    print('session:', request.session)
    print('files:', request.FILES)
    return HttpResponse('attribute')


def attribute_get1(request):
    """查看他们的属性"""
    a = request.GET['a']
    b = request.GET.get('b')
    c = request.GET['c']
    print("path:", request.path)
    print('method:', request.method)
    print('encoding:', request.encoding)
    print('get:', request.GET)
    print('post:', request.POST)
    print('cookies:', request.COOKIES)
    print('session:', request.session)
    print('files:', request.FILES)
    return HttpResponse("a:{a}\nb:{b}\nc:{c}".format(a=a, b=b, c=c))


def attribute_get2(request):
    """查看他们的属性"""
    a = request.GET.getlist('a')
    b = request.GET.getlist('b')
    c = request.GET.getlist('c')
    print("path:", request.path)
    print('method:', request.method)
    print('encoding:', request.encoding)
    print('get:', request.GET)
    print('post:', request.POST)
    print('cookies:', request.COOKIES)
    print('session:', request.session)
    print('files:', request.FILES)
    return HttpResponse("a:{a}\nb:{b}\nc:{c}".format(a=a, b=b, c=c))


def show_register(request):
    return render(request, 'myapp/register.html')


def register(request):
    name = request.POST['name']
    age = request.POST['age']
    sex = request.POST['sex']
    bobby = request.POST.getlist('bobby')
    info = {
        'name': name,
        'age': age,
        'sex': sex,
        'hobby': bobby,
        'code': 1000
    }
    return HttpResponse(json.dumps(info), content_type='application/json')


def show_response(request):
    result = HttpResponse()
    result.content = b'good'
    print(result.charset)
    print(result.content)
    print(result.status_code)
    return result


def show_cookie(request):
    """设置cookie"""
    res = HttpResponse()
    # cookie = request.COOKIES
    # res.write("<h2>{}</h2>".format(cookie['sid']))
    res.delete_cookie('sid')  # 删除 cookie
    # res.set_cookie('sid', 'WSEGSLIF87665DFWS0j')
    return res


from django.http import HttpResponseRedirect
from django.shortcuts import redirect


# 重定向
def show_redirect1(request):
    """url 配置 这个 但是 跳转到下面的一个"""
    return HttpResponseRedirect('/show_redirect2')
    # return redirect('/show_redirect2')


def show_redirect2(request):
    data = {
        'code': 1000,
        'status': 1
    }
    return HttpResponse(json.dumps(data))
