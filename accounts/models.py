from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver




class UserManager(BaseUserManager):
    def create_user(self, national_code, password, **extra_fields):
        
        if not national_code:
            raise ValueError(_("The national_code must be set"))
        
        user = self.model(national_code=national_code, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, national_code, password, **extra_fields):
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)


        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        

        return self.create_user(national_code, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    '''
    custom User model for our app
    '''
    national_code = models.CharField(max_length=10, unique=True, verbose_name='کد ملی')
    is_superuser = models.BooleanField(default=False, verbose_name='ادمین')
    is_teacher = models.BooleanField(default=False, verbose_name='معلم')
    is_staff = models.BooleanField(default=False, verbose_name='مدیر') 
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_student = models.BooleanField(default=False, verbose_name='دانش اموز')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'national_code'

    objects = UserManager()

    def __str__(self):
        return self.national_code
    



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    phone_number = models.CharField(max_length=11, unique=True, null=True, blank=True, verbose_name='شماره تلفن')
    first_name = models.CharField(max_length=250, default='کاربر', verbose_name='نام')
    last_name = models.CharField(max_length=250, verbose_name='نام خانوادگی')
    image = models.ImageField(upload_to='profiles', blank=True, null=True, verbose_name='تصویر')
    description = models.TextField(verbose_name='توضیحات')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.user.national_code
    




    
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)