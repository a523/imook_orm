from django.db import models

# Create your models here.


class AddressInfo(models.Model):
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name="地址")
    pid = models.ForeignKey('self', null=True, blank=True, verbose_name='自关联', on_delete=models.CASCADE)
    note = models.CharField(max_length=200, null=True, blank=True, verbose_name="说明")

    def __str__(self):
        return self.address

    class Meta:
        db_table = 'address'
        ordering = ['pid_id']
        verbose_name = "省市县地址信息"
        unique_together = ('address', 'note')


class Teacher(models.Model):
    """讲师信息表"""
    nickname = models.CharField(max_length=30, primary_key=True, db_index=True, verbose_name="昵称")
    introduction = models.TextField(default="这位同学很懒，什么也没有留下", verbose_name="简介")
    fans = models.PositiveIntegerField(default="0", verbose_name="粉丝数")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "讲师信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname


class Course(models.Model):
    """课程信息表"""
    title = models.CharField(max_length=100, primary_key=True, db_index=True, verbose_name="课程名")
    teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.CASCADE,
                                verbose_name="课程讲师")  # 删除级联
    type = models.PositiveIntegerField(choices=((1, "实战课"), (2, "免费课"), (0, "其它")), max_length=1,
                            default=0, verbose_name="课程类型")
    price = models.PositiveSmallIntegerField(verbose_name="价格")
    volume = models.BigIntegerField(verbose_name="销量")
    online = models.DateField(verbose_name="上线时间")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "课程信息表"
        get_latest_by = "created_at"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.get_type_display()}-{self.title}"


class Student(models.Model):
    """学生信息表"""
    nickname = models.CharField(max_length=30, primary_key=True, db_index=True, verbose_name="昵称")
    course = models.ManyToManyField(Course, verbose_name="课程")
    age = models.PositiveSmallIntegerField(verbose_name="年龄")
    gender = models.CharField(choices=((1, "男"), (2, "女"), (0, "保密")), max_length=1,
                              default=0, verbose_name="性别")
    study_time = models.PositiveIntegerField(default="0", verbose_name="学习时长(h)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "学生信息表"
        ordering = ['age']
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname


class TeacherAssistant(models.Model):
    """助教信息表"""
    nickname = models.CharField(max_length=30, primary_key=True, db_index=True, verbose_name="昵称")
    teacher = models.OneToOneField(Teacher, null=True, blank=True, on_delete=models.SET_NULL,
                                   verbose_name="讲师")  # 删除置空
    hobby = models.CharField(max_length=100, null=True, blank=True, verbose_name="爱好")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "助教信息表"
        db_table = "courses_assistant"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname