# Generated by Django 3.2.5 on 2021-12-22 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plep_app', '0010_alter_client_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='uid',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
