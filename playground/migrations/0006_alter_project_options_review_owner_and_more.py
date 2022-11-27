# Generated by Django 4.1.3 on 2022-11-27 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_profile_location_skill"),
        ("playground", "0005_project_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="project",
            options={"ordering": ["created"]},
        ),
        migrations.AddField(
            model_name="review",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.profile",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="review",
            unique_together={("owner", "project")},
        ),
    ]
