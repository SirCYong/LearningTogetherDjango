from django.db import models


# Create your models here.


class Class(models.Model):
    gname = models.CharField(max_length=20)
    ddate = models.DateTimeField()
    ggirlnumber = models.IntegerField()
    gboynumber = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        # return "name:{0} data:{1} girl_number:{2} boy_number:{3}isDelete:{4}\n".format(self.gname, self.ddate,
        #                                                                                self.ggirlnumber,
        #                                                                                self.gboynumber, self.isDelete)
        return "{0}{1}".format(self.gname, self.ddate)


class StudentManager(models.Manager):
    def get_queryset(self):
        # 继承Manager类的所有东东，然后返回 isDelete为 False的 value
        return super(StudentManager, self).get_queryset().filter(isDelete=False)

    def create_student(self, name, sex, age, contend, class_id):
        # 第四种写法
        stu = self.model()
        stu.sname = name
        stu.sex = sex
        stu.age = age
        stu.scontend = contend
        stu.sclass = class_id
        return stu



# def create_student(name, sex, age, contend, class_id):
#     """
#     第三种写法
#     :param name:
#     :param sex:
#     :param age:
#     :param contend:
#     :param class_id:
#     :return:
#     """
#     stu = Student(sname=name, sex=sex, age=age, scontend=contend, sclass=class_id)
#     return stu



class Student(models.Model):
    # 学生表
    # 自定义模型管理器
    """当自定义模型管理器，那么 objects 就 不存在了"""
    objects = models.Manager()
    driver = StudentManager()
    sname = models.CharField(max_length=20)
    sex = models.BooleanField()
    age = models.IntegerField()
    scontend = models.CharField(max_length=100)
    isDelete = models.BooleanField(default=False)
    # 关联外键
    sclass = models.ForeignKey("Class", on_delete=models.CASCADE)
    updateTime = models.DateTimeField(auto_now=True, db_column="lastTime")
    createTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sname

    class Meta:
        db_table = ""
        ordering = []

    # 定义一个类方法创建对象

    # @classmethod
    # def create_student(cls, name, sex, age, contend, class_id):
    #      第一种写法
    #     stu = cls(sname= name, sex=sex, age=age, scontend=contend, sclass=class_id)
    #     return stu
    # def create_student(self, name, sex, age, contend, class_id):
    #     # 第二种写法
    #     stu = Student(sname=name, sex=sex, age=age, scontend=contend, sclass=class_id)
    #     return stu

