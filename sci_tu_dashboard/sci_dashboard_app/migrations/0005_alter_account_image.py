# Generated by Django 3.2.4 on 2022-04-05 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sci_dashboard_app', '0004_reporttype_labels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='userprofile'),
        ),
    ]