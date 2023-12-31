# Generated by Django 4.2.7 on 2023-11-12 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Shekh_Mohafez',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, help_text='Enter phone number without country code', max_length=15, null=True, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shekh_Tester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, help_text='Enter phone number without country code', max_length=15, null=True, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('third_name', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_year', models.IntegerField(auto_created=True, default=2023)),
                ('number_of_Juze', models.CharField(choices=[('0', '-'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '30 مع التجويد')], max_length=20)),
                ('national_id', models.DecimalField(decimal_places=0, max_digits=14, unique=True)),
                ('phone_number1', models.CharField(blank=True, help_text='Enter phone number without country code', max_length=15, null=True, unique=True)),
                ('phone_number2', models.CharField(blank=True, help_text='Enter phone number without country code', max_length=15, null=True, unique=True)),
                ('result', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('basic_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
                ('student_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.country')),
                ('student_shekh_mohafez', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.shekh_mohafez')),
                ('student_shekh_tester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.shekh_tester')),
            ],
        ),
    ]
