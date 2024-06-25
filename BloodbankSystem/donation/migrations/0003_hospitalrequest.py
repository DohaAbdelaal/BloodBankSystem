# Generated by Django 5.0.3 on 2024-04-16 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0002_alter_bloodstock_bloodbankcity_alter_donor_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=255)),
                ('blood_group', models.CharField(choices=[('O', 'O'), ('A', 'A'), ('B', 'B'), ('AB', 'AB')], max_length=2)),
                ('city', models.CharField(max_length=100)),
                ('patient_status', models.CharField(choices=[('Immediate', 'Immediate'), ('Urgent', 'Urgent'), ('Normal', 'Normal')], max_length=20)),
            ],
        ),
    ]