from django.contrib.auth.models import User
from django.db import models


#CATEGORY = (
#    ('вареные колбасы', 'Вареные колбасы'),
#    ('варено-копченые колбасы', 'Варено-копченые колбасы'),
#    ('полукопченые колбасы', 'Полукопченые колбасы'),
#    ('сырокопченые колбасы', 'Сырокопченые колбасы'),
#    ('соски и сардельки', 'Сосиски и сардельки'),
#    ('колбасы из субпродуктов', 'Колбасы из субпродуктов'),
#    ('крупнокусковые полуфабрикаты', 'Крупнокусковые полуфабрикаты'),
#    ('мелкокусковые полуфабрикаты', 'Мелкокусковые полуфабрикаты'),
#    ('мясные полуфабрикаты', 'Мясные полуфабрикаты'),
#    ('пельмени', 'Пельмени'),
#    ('фарши', 'Фарши'),
#    ('вареники', 'Вареники'),
#    ('субпродукты', 'Субпродуты'),
#)


class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Promo (models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    discription = models.TextField()
    start_data = models.DateField()
    end_data = models.DateField()

    def __str__(self):
        return self.name


#class Order(models.Model):
#    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
#    date_order = models.DateTimeField(auto_now_add=True)

