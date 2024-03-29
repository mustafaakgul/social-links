# Generated by Django 4.2.4 on 2023-12-08 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("links", "0003_remove_customlink_profile_customlink_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="link",
            name="title",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="link",
                to="links.socialnetwork",
            ),
        ),
    ]
