# Generated by Django 2.0.7 on 2018-09-04 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_certifications'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notifications',
            options={'ordering': ['-pub_date', '-expiration']},
        ),
        migrations.RenameField(
            model_name='certifications',
            old_name='visibility',
            new_name='visible',
        ),
    ]
