# Generated by Django 4.2.6 on 2023-12-03 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_alter_photo_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='user_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile'),
        ),
    ]
