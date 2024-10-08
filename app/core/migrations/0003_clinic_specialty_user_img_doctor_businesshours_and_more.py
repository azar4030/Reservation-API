# Generated by Django 5.1.1 on 2024-10-01 22:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_user_birth_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/clinic')),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='images/specialty')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile'),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('specialties', models.ManyToManyField(to='core.specialty')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(max_length=255)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mother_name', models.CharField(max_length=255)),
                ('father_name', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('bo', 'رزرو شده'), ('ca', 'لغو شده'), ('pe', 'در انتظار تایید')], default='bo', max_length=2)),
                ('payment_status', models.CharField(choices=[('pa', 'پرداخت شده'), ('un', 'پرداخت نشده')], default='un', max_length=2)),
                ('date', models.DateField()),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.clinic')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.patient')),
            ],
        ),
        migrations.CreateModel(
            name='ClinicDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultation_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.clinic')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctor')),
            ],
            options={
                'unique_together': {('clinic', 'doctor')},
            },
        ),
        migrations.CreateModel(
            name='ClinicSpecialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.clinic')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.specialty')),
            ],
            options={
                'unique_together': {('clinic', 'specialty')},
            },
        ),
    ]
