# Generated by Django 2.2 on 2019-04-29 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20190429_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.CharField(default='@', max_length=100),
        ),
    ]
