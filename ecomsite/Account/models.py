from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,email,phone_number=None,password=None):
        if not email:
            raise  ValueError("User must have valid email addresss")
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name,last_name,email,phone_number=None,password=None):
        if not email:
            raise ValueError("User must have valid email addresss")
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )
        user.is_admin=True
        user.set_password(password)
        user.save(using=self._db)
        return user

class Account(AbstractUser):
    first_name =  models.CharField(max_length=50)
    last_name =  models.CharField(max_length=10)
    email = models.EmailField(unique=True,verbose_name="Email address")
    phone_number = models.CharField(max_length=15,blank=True,null=True)

    date_joined =  models.DateField(auto_now=True)
    is_active =  models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyAccountManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name','last_name',]


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


