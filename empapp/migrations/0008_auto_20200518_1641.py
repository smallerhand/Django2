# Generated by Django 2.0.2 on 2020-05-18 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0007_auto_20200517_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetail',
            name='dep',
            field=models.CharField(choices=[('sales', '営業'), ('pr', '広報'), ('dev', '開発')], max_length=2),
        ),
        migrations.AlterField(
            model_name='employeedetail',
            name='job',
            field=models.CharField(choices=[('regular', '一般'), ('administrator', '組織長')], max_length=3),
        ),
        migrations.AlterField(
            model_name='employeedetail',
            name='sex',
            field=models.CharField(choices=[('f', '女'), ('m', '男')], max_length=1),
        ),
    ]
