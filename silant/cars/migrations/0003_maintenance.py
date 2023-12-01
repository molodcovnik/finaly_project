# Generated by Django 4.2.7 on 2023-11-30 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_clientuser_name_company'),
        ('manuals', '0002_modeldrivingbridge_modelengine_modelsteeredbridge_and_more'),
        ('cars', '0002_alter_machine_serial_number_technique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_date', models.DateField()),
                ('operating_time', models.IntegerField()),
                ('work_order_number', models.CharField(max_length=128)),
                ('work_order_date', models.DateField()),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.machine')),
                ('maintenance_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manuals.typemaintenance')),
                ('service_company', models.ForeignKey(default='самостоятельно', limit_choices_to={'status': 'SERVICE'}, on_delete=django.db.models.deletion.CASCADE, related_name='maintenances', to='accounts.clientuser')),
            ],
        ),
    ]
