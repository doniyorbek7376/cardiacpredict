# Generated by Django 4.2.1 on 2023-05-21 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0002_predictionrequest_predictionmodel_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictionrequest',
            name='sex',
            field=models.CharField(max_length=10),
        ),
    ]
