from django.db import models

class employee(models.Model):
    emp_num = models.PositiveSmallIntegerField()
    emp_name = models.CharField(max_length=30)
    emp_ename = models.CharField(max_length=30)
    sex_choices = (
        ('女', 'Female',),
        ('男', 'Male',),
    )
    sex = models.CharField(
        max_length=1,
        choices=sex_choices,
    )

    birth = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()

    bloodtype_choices = (
        ('A', 'A',),
        ('B', 'B',),
        ('AB', 'AB',),
        ('O', 'O',),
    )
    bloodtype = models.CharField(
        max_length=2,
        choices=bloodtype_choices,
    )

    dep = models.CharField(max_length=30)
    job = models.CharField(max_length=30)

class employeeDetail(models.Model):
    num	=	models.PositiveSmallIntegerField()
    lname	=	models.CharField(max_length=30)
    fname	=	models.CharField(max_length=30)
    elname	=	models.CharField(max_length=30)
    efname	=	models.CharField(max_length=30)
    sex_choices = (
            ('女', 'Female',),
            ('男', 'Male',),
        )
    sex	=	models.CharField(
            max_length=1,
            choices=sex_choices,
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
    dep	=	models.CharField(max_length=30)
    job	=	models.CharField(max_length=30)
    pw	=	models.CharField(max_length=30)
