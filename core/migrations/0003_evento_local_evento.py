# Generated by Django 3.1.7 on 2021-03-13 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210313_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='local_evento',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
