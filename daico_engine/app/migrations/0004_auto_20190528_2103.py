# Generated by Django 2.1 on 2019-05-28 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190528_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='kinds',
        ),
        migrations.AddField(
            model_name='contact',
            name='foo',
            field=models.IntegerField(choices=[(1, 'ご注文について'), (2, '会員情報について'), (3, 'ご利用方法について'), (4, 'その他')], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('B', '女性'), ('A', '男性'), ('C', 'その他')], default=None, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('B', 'Customer User'), ('A', 'Client User')], default='B', max_length=1),
        ),
    ]
