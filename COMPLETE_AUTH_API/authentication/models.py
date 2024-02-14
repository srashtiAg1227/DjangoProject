from django.db import models
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser
from django.contrib.auth.hashers import make_password

# Create your models here.

#custom user manager
class UserManager(BaseUserManager):
  def create_user(self, email, name, password=None, password2 = None):
        """
        Creates and saves a User with the given email,name, term condition and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name = name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
 
  def create_superuser(self, email, name, password=None):
        """
        Creates and saves a superuser with the given email, name , term condition and password.
        """
        user = self.create_user(
            email,
            password=password,
            name= name,
            
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

#custom user model 
class  MyUser(AbstractBaseUser):
  email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
  name = models.CharField(max_length = 200)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
 
  objects = UserManager()

  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ["name"]

  def __str__(self):
        return self.email

  def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

  def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
  def set_password(self, raw_password):
        self.password = make_password(raw_password, salt='D;%yL9TS:5PalS/d')
        self._password = raw_password

  @property
  def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin