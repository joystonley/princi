# Generated by Django 2.2 on 2023-10-29 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conge',
            name='jours_restants',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='conge',
            name='jours_utilises',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='typeconge',
            name='nb_jour',
            field=models.IntegerField(default=0),
        ),
    ]
