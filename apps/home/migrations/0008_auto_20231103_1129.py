# Generated by Django 2.2 on 2023-11-03 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_departement_domaine'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avancement',
            old_name='date_av',
            new_name='date_effective',
        ),
        migrations.RenameField(
            model_name='avancement',
            old_name='employe',
            new_name='employee',
        ),
        migrations.RenameField(
            model_name='avancement',
            old_name='enseignant',
            new_name='teacher',
        ),
        migrations.RemoveField(
            model_name='avancement',
            name='grade_av',
        ),
    ]