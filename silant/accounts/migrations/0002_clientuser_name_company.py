# Generated by Django 4.2.7 on 2023-11-29 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientuser',
            name='name_company',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
