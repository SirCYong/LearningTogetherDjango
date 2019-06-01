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
    student = Student.objects.all()[(page-1)*limit: page*limit]
    return render(request, 'myapp/student.html', {'student': student})

