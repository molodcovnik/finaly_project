# Generated by Django 4.2.7 on 2023-12-01 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_alter_claim_restore_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='downtime',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]