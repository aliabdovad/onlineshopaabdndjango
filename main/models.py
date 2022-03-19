from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField('پروفایل', upload_to='Customer_avatar_images')
    description = models.CharField('توضیحات', max_length=250)

    def __str__(self):
        return self.user.first_name + '-' + self.user.last_name

    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتریان'
