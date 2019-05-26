# Generated by Django 2.1 on 2019-05-26 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.TextField(default=None, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('B', 'Customer User'), ('A', 'Client User')], default='B', max_length=1),
        ),
    ]
