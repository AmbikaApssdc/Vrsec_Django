# Generated by Django 3.1.7 on 2021-04-09 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddforms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='student',
            name='mobile',
            field=models.CharField(default=True, max_length=10),
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default=True, max_length=30),
        ),
        migrations.AddField(
            model_name='student',
            name='rollnumber',
            field=models.CharField(default=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(default=True, max_length=30),
        ),
    ]
