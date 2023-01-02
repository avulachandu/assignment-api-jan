from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.IntegerField()
    unique_code=models.IntegerField(unique=True)
    sizes=(('a',10),
    ('b',20),
    ('c',30))
    size=models.CharField(max_length=1,choices=sizes)
    VALUE=(('h','high'),
        ('m','medium'),
        ('l','low'))
    quality=models.CharField(max_length=1,choices=VALUE)
    
class Productioncolour(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    choice=(('r','red'),
    ('b','blue'),
    ('g','green'),
    ('b','black'))
    image=models.CharField(choices=choice,max_length=1)
    


class Productionimage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.ImageField()
