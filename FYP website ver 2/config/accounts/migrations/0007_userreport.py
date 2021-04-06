# Generated by Django 3.1.7 on 2021-04-06 03:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210327_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scan_data', models.CharField(max_length=100)),
                ('scan_website', models.TextField()),
                ('vulnerabilities', models.TextField()),
                ('solutions', models.TextField()),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
