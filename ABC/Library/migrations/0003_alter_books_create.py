# Generated by Django 4.1.1 on 2022-09-07 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Library', '0002_alter_books_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='Create',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
