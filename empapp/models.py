from django.db import models

class employeeDetail(models.Model):
    num	=	models.PositiveSmallIntegerField(primary_key=True)
    lname	=	models.CharField(max_length=30)
    fname	=	models.CharField(max_length=30)
    elname	=	models.CharField(max_length=30)
    efname	=	models.CharField(max_length=30)
    f = 'f'
    m = 'm'
    SEX = [
        (f, '女'),
        (m, '男'),
    ]

    sex	=	models.CharField(
            max_length=1,
            choices=SEX,
        )
    email	=	models.EmailField(max_length=254)
    birth	=	models.CharField(max_length=30)
    age	=	models.PositiveSmallIntegerField()
    bloodtype_choices = (
        ('A', 'A',),
        ('B', 'B',),
        ('AB', 'AB',),
        ('O', 'O',),
        )
    bloodtype	=	models.CharField(
            max_length=2,
            choices=bloodtype_choices,
        )
    sales = 'sales'
    pr = 'pr'
    dev = 'dev'
    DEP = [
        (sales, '営業'),
        (pr, '広報'),
        (dev, '開発'),
    ]
    dep	=	models.CharField(
            max_length=5,
            choices=DEP,
        )
    reg = 'regular'
    admin = 'administrator'
    JOB = (
        (reg, '一般'),
        (admin, '組織長'),
    )
    job	=	models.CharField(
            max_length=13,
            choices=JOB,
        )
    pw	=	models.CharField(max_length=30)
