# Generated by Django 5.0.1 on 2024-02-19 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_is_approved_customuser_is_student_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_owner',
            field=models.BooleanField(default=False),
        ),
    ]