# Generated by Django 4.2.6 on 2023-11-10 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_useranswer_date_answered_useranswer_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='points',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
