# Generated by Django 4.1.3 on 2022-11-29 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_message"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Message",
            new_name="Inbox",
        ),
    ]
