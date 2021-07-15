from django.db import models
from django.contrib.auth import get_user_model
from users.constants import ROLES_TYPES, GRADES_TYPES, UNDEFINED, VIEWER


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True)
    technical_skills = models.TextField(null=True)
    soft_skills = models.TextField(null=True)
    language_level = models.TextField(null=True)
    role = models.CharField(max_length=30, choices=ROLES_TYPES, default=VIEWER)
    grade = models.CharField(max_length=30, choices=GRADES_TYPES, default=UNDEFINED)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f'{self.user} {self.role}'
