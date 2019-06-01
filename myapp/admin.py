from django.contrib import admin

# Register your models here.
from .models import Class, Student

# 注册


class ClassManyStudent(admin.TabularInline):  # StackedInline
    model = Student
    extra = 2


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    inlines = [ClassManyStudent]
    """列表页属性"""

    list_display = ['id', 'gname', 'ddate', 'ggirlnumber', 'gboynumber', 'isDelete']
    list_filter = ['gname', 'ddate', 'ggirlnumber', 'gboynumber', 'isDelete']  # 过滤器
    search_fields = ['gname']
    list_per_page = 15
    """添加、修改页 属性"""
    # fields = ['gname', 'ggirlnumber', 'gboynumber', 'isDelete', 'ddate']
    fieldsets = [
        ('number', {'fields':['ggirlnumber', 'gboynumber']}),
        ('baseInfo', {'fields': ['gname', 'ddate', 'isDelete']}),
    ]


# admin.site.register(Class, ClassAdmin)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.sex = None
        self.age = None

    def view_sex(self):
        if self.sex:
            return '男'
        else:
            return '女'

    view_sex.short_description = "性别"  # 列的描述

    def view_age(self):
        return self.age

    view_age.short_description = "年龄"
    """列表页属性"""
    list_display = ['id', 'sname', view_sex, view_age, 'scontend', 'isDelete']
    list_filter = ['sname']
    search_fields = ['sname']
    list_per_page = 15
    """添加、修改页 属性"""
    # fields = ['gname', 'ggirlnumber', 'gboynumber', 'isDelete', 'ddate']
    # fieldsets = [
    #     ('关注点', {'fields': ['age', 'sex']}),
    #     ('baseInfo', {'fields': ['sname', 'sex', 'isDelete', 'scontend']}),
    #     ('关联班级', {'fields': ['sclass']}),
    # ]
    #  执行动作的位置
    actions_on_bottom = True  # 底部显示
    actions_on_top = False  # 顶部显示

