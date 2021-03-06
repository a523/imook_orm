# Generated by Django 2.1.5 on 2019-01-05 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='地址')),
                ('note', models.CharField(blank=True, max_length=200, null=True, verbose_name='说明')),
                ('pid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.AddressInfo', verbose_name='自关联')),
            ],
            options={
                'verbose_name': '省市县地址信息',
                'db_table': 'address',
                'ordering': ['pid'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='addressinfo',
            unique_together={('address', 'note')},
        ),
    ]
