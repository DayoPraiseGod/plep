# Generated by Django 3.2.5 on 2021-12-22 20:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('plep_app', '0007_alter_client_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
