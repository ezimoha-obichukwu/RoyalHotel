# Generated by Django 4.2 on 2023-05-02 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0011_rename_description_contact_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog_post',
            old_name='commentary',
            new_name='commentry',
        ),
    ]