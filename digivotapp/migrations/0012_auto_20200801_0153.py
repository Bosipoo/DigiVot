# Generated by Django 3.0.8 on 2020-08-01 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digivotapp', '0011_auto_20200801_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manageruserr',
            name='pin',
            field=models.CharField(default='MW7MD', editable=False, max_length=5),
        ),
        migrations.AlterField(
            model_name='super_registeradmin',
            name='pin',
            field=models.CharField(default='AT2DX', editable=False, max_length=5, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='voterreg',
            name='pin',
            field=models.CharField(default='VMTWE', editable=False, max_length=5),
        ),
    ]