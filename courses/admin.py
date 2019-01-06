from django.contrib import admin
from .models import AddressInfo, Course, Teacher
# Register your models here.


class AddressAdmin(admin.ModelAdmin):
    fields = ['address', 'pid']


class CoursesAdmin(admin.ModelAdmin):
    fileds = ['*']


class TeacherAdmin(admin.ModelAdmin):
    pass


admin.site.register(AddressInfo, AddressAdmin)
admin.site.register(Course, CoursesAdmin)
admin.site.register(Teacher, TeacherAdmin)