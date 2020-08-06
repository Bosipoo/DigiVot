# Generated by Django 3.0.8 on 2020-08-05 17:38

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('digivotapp', '0026_auto_20200805_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electiontype',
            name='electiontype',
            field=models.CharField(choices=[('Presidential', 'Presidential'), ('Gubernatorial', 'Gubernatorial'), ('Senatorial', 'Senatoial')], default='Presidential', max_length=100),
        ),
        migrations.AlterField(
            model_name='manageruserr',
            name='pictures',
            field=stdimage.models.StdImageField(upload_to='path/to/img'),
        ),
        migrations.AlterField(
            model_name='manageruserr',
            name='pin',
            field=models.CharField(default='MS6NT', editable=False, max_length=5),
        ),
        migrations.AlterField(
            model_name='super_registeradmin',
            name='pin',
            field=models.CharField(default='A7NEO', editable=False, max_length=5, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='voterreg',
            name='pin',
            field=models.CharField(default='V0K6M', editable=False, max_length=5),
        ),
    ]
