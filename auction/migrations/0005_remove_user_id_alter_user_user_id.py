# Generated by Django 4.1.7 on 2023-03-04 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0004_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
