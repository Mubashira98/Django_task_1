# Generated by Django 4.1.3 on 2023-01-28 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_student_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.IntegerField()),
                ('maths', models.IntegerField()),
                ('hindi', models.IntegerField()),
                ('science', models.IntegerField()),
                ('malayalam', models.IntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.student')),
            ],
        ),
    ]
