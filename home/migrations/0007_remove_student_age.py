# Generated by Django 4.1.3 on 2023-01-28 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_student_age_alter_student_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
    ]
