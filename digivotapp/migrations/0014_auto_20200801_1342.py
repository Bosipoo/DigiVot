# Generated by Django 3.0.8 on 2020-08-01 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digivotapp', '0013_auto_20200801_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voterreg',
            name='managerID',
        ),
        migrations.AlterField(
            model_name='manageruserr',
            name='pin',
            field=models.CharField(default='M4WJO', editable=False, max_length=5),
        ),
        migrations.AlterField(
            model_name='super_registeradmin',
            name='pin',
            field=models.CharField(default='A097H', editable=False, max_length=5, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='voterreg',
            name='pin',
            field=models.CharField(default='VEH9I', editable=False, max_length=5),
        ),
    ]