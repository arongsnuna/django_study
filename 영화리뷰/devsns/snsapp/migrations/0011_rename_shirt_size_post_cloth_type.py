# Generated by Django 4.0.5 on 2022-06-09 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snsapp', '0010_alter_post_shirt_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='shirt_size',
            new_name='cloth_type',
        ),
    ]
