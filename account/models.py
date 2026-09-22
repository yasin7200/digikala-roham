from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, first_name, last_name, email, username, password, phone, national_id, birthday):
        new_user = self.model(first_name=first_name,
                              last_name=last_name,
                              email=email,
                              username=username,
                              phone=phone,
                              national_id=national_id,
                              birthday=birthday)
        
        new_user.set_password(password)
        new_user.save(using=self._db)
        return new_user
    
    def create_superuser(self, first_name, last_name, email, username, password, phone, national_id, birthday):
        new_superuser = self.create_user(first_name, last_name, email, username, password, phone, national_id, birthday)

        new_superuser.is_staff = True
        new_superuser.is_superuser = True
        new_superuser.save(using=self._db)
        return new_superuser


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True) 
    phone = models.CharField(max_length=11)
    birthday = models.DateField()
    national_id = models.CharField(max_length=10)
    username = models.CharField(max_length=100)
    last_login = models.DateTimeField(auto_now=True)
    date_join = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'username', "national_id", "birthday"]

    USERNAME_FIELD = 'email'

    objects = UserManager()
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='images/profile')
    address = models.TextField()

    def __str__(self):
        return f'{self.user.first_name}-{self.user.last_name}'                                                                                