from django.db import models

class employeeDetail(models.Model):
    num	=	models.PositiveSmallIntegerField(primary_key=True)
    lname	=	models.CharField(max_length=30)
    fname	=	models.CharField(max_length=30)
    elname	=	models.CharField(max_length=30)
    efname	=	models.CharField(max_length=30)
    sex_choices = (
            ('女', 'f',),
            ('男', 'm',),
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
    dep_choices = (
            ('営業', 'sales',),
            ('広報', 'pr',),
            ('開発', 'dev',),
        )
    dep	=	models.CharField(
            max_length=2,
            choices=dep_choices,
        )
    job_choices = (
            ('一般', 'regular',),
            ('組織長', 'administrator',),
        )
    job	=	models.CharField(
            max_length=3,
            choices=job_choices,
        )
    pw	=	models.CharField(max_length=30)
