from django.db import models
from django.contrib.auth.models import AbstractUser

from main.utils import phone_regex
from main.managers import CustomUserManager


class User(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profession = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=13, validators=(phone_regex,))
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    profile = models.CharField(max_length=255)
    email = models.EmailField(verbose_name='Email')
    place_of_birth = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)
    hobbies = models.CharField(max_length=255)
    languages = models.ManyToManyField('Language')
    achievements = models.CharField(max_length=255)
    image = models.ImageField(upload_to='profiles/%y/%m/%d')
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Region(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.title


class Link(models.Model):
    TYPE = (
        ('Facebook', 'facebook'),
        ('LinkedIn', 'linkedin'),
        ('GitHub', 'github'),
    )
    type = models.CharField(max_length=10, choices=TYPE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField(unique=True)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Language(models.Model):
    title = models.CharField(max_length=50)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class EducationEmployment(models.Model):
    TYPE = (
        ('Education', 'education'),
        ('Employment', 'employment')
    )
    type = models.CharField(max_length=15, choices=TYPE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    starting_date = models.DateField()
    ending_date = models.DateField()
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
