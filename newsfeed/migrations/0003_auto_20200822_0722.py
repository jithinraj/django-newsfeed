# Generated by Django 3.1 on 2020-08-22 07:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0002_auto_20200821_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='token',
            field=models.CharField(default=uuid.uuid4, max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='verification_sent_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]