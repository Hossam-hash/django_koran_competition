# Generated by Django 4.2.7 on 2023-11-25 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_shekh_mohafez_user_remove_shekh_tester_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
