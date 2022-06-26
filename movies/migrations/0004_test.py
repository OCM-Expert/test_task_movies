# Generated by Django 4.0.5 on 2022-06-24 21:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]