# Generated by Django 3.2.5 on 2021-12-18 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plep_app', '0002_alter_client_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='uid',
            field=models.CharField(default=None, max_length=10),
        ),
    ]