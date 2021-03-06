# Generated by Django 3.2.5 on 2021-07-13 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(null=True)),
                ('technical_skills', models.TextField(null=True)),
                ('soft_skills', models.TextField(null=True)),
                ('language_level', models.TextField(null=True)),
                ('role', models.CharField(choices=[('INTERVIEW_PARTICIPANT', 'Interview participant'), ('VIEWER', 'Viewer'), ('TECHNICAL_EXPERT', 'Technical expert'), ('TECHNICAL_LEAD', 'Technical lead')], default='VIEWER', max_length=30)),
                ('grade', models.CharField(choices=[('UNDEFINED', 'Undefined'), ('JUNIOR', 'Junior'), ('MIDDLE', 'Middle'), ('SENIOR', 'Senior')], default='UNDEFINED', max_length=30)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
