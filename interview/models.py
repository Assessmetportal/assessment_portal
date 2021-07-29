from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db import models

from interview import constants

User = get_user_model()


class Interview(models.Model):
    theme = models.CharField(max_length=25, default='')
    interviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="interviews_to",
                                    verbose_name=_("Interviewer"), default=None, null=True)
    interviewed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="interviews_from",
                                    verbose_name=_("Interviewed"), default=None, null=True)
    date_of_interview = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Interviewer: {self.interviewer} | Interviewed: {self.interviewed}'


class Response(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    final_grade = models.CharField(max_length=30, choices=constants.GRADES_TYPES)
    response = models.TextField()

    def __str__(self):
        return f'{self.interview} '
