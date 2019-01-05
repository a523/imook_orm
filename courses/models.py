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
